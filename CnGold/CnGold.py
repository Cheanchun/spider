# -*- coding:utf-8 -*-
import random
import time
import traceback
from multiprocessing import Process

import pymongo
import redis
import requests
from IntelligentContentParse.intelligent_parse import IntelligentParse
from utils import CommSession, url_parse, get_yaml_data, coding, content2tree

config = get_yaml_data('./config.yml')
print(config)
user_redis = redis.Redis(**config.get('redis_config'))


def cnn_mongo(mongo_config):
    cnn = pymongo.MongoClient(host=mongo_config.get('host'), port=mongo_config.get('port'))
    db = cnn['shixin']
    db.authenticate(mongo_config.get('user'), mongo_config.get('password'))
    return db


db = cnn_mongo(config.get('mongo_config'))


class CnGoldProduct(Process):
    def __init__(self):
        super(CnGoldProduct, self).__init__()
        self.index_url = config.get('site_config').get('index')
        self.session = self.instance_session()
        self.user_redis = redis.Redis(**config.get('redis_config'))

    def instance_session(self):
        return CommSession(verify=True).session(self.index_url)

    def _get(self, url, timeout=30, method='get', post_data=None, retry=3):
        """
        网页下载
        :param url:
        :return:resp
        :rtype: requests.Response
        """
        for _ in range(retry):
            try:
                time.sleep(random.randint(3, 5))
                if method == 'get':
                    resp = self.session.get(url=url, timeout=timeout)
                elif method == 'post' and post_data is not None:
                    resp = self.session.post(url=url, data=post_data, allow_redirects=True, timeout=timeout)
                else:
                    raise ValueError('request method not support')
            except requests.exceptions:
                continue
            if resp.status_code // 100 == 2:
                return resp
        raise traceback.format_exc()

    def main(self):
        if not self.user_redis.exists('list_page'):
            self.user_redis.rpush('list_page', self.index_url)
        while True:
            current_url = self.user_redis.lpop('list_page')
            if current_url:
                print('current url:{}'.format(current_url))
                self.user_redis.lrem('list_page', count=1, value=current_url)
                resp = self._get(current_url)
                # check_next_page(resp, self.user_redis)
                for url, _type in url_parse(resp):
                    self.user_redis.sadd('crawled_url', current_url)
                    if not self.user_redis.sismember('crawled_url', url):
                        if _type == 1 and not self.user_redis.sismember('crawled_url', url):
                            print('list_page_remove', self.user_redis.lrem('list_page', count=0, value=url))
                            print('list_page_add', self.user_redis.lpush('list_page', url))
                        elif _type == 2 and not self.user_redis.sismember('crawled_url', url):
                            print('detail_page_remove', self.user_redis.lrem('detail_page', count=0, value=url))
                            print('detail_page_add', self.user_redis.rpush('detail_page', url))
                        elif self.user_redis.sismember('crawled_url', url):
                            print('url crawled:{}'.format(url))
                        else:
                            print('other url:{}'.format(url))
            else:
                print('product sleep 30s...')
                time.sleep(30)

    def start(self):
        print('product start...')
        self.main()
        print('product end...')


class CnGoldCustomer(Process):
    def __init__(self):
        super(CnGoldCustomer, self).__init__()

        self.index_url = ''
        self.session = self.instance_session()

    def instance_session(self):
        return CommSession(verify=True).session(self.index_url)

    def _get(self, url, timeout=30, method='get', post_data=None, retry=3):
        """
        网页下载
        :param url:
        :return:resp
        :rtype: requests.Response
        """
        for _ in range(retry):
            try:
                time.sleep(random.randint(3, 5))
                if method == 'get':
                    resp = self.session.get(url=url, timeout=timeout)
                elif method == 'post' and post_data is not None:
                    resp = self.session.post(url=url, data=post_data, allow_redirects=True, timeout=timeout)
                else:
                    raise ValueError('request method not support')
            except requests.exceptions:
                continue
            if resp.status_code // 100 == 2:
                return resp
        raise traceback.format_exc()

    def parse_detail(self, response):
        data = {}
        html = content2tree(coding(response))
        for key, value in config.get('parse_config').items():
            data[key] = html.xpath(value) if html.xpath(value) else ''
        data['content'] = IntelligentParse(coding(response).text).intelligent_main()  # todo 正文解析调用分段
        data['url'] = response.url
        self.save_data(data)

    def save_data(self, data):
        db['CnGold'].insert(data)
        print(data.get(''),data.get('url'))
        print('=' * 100)

    def queue_handle(self):
        detail_url = user_redis.lpop('detail_page')
        if detail_url:
            user_redis.sadd('crawled_url', detail_url)
            return detail_url
        return ''

    @staticmethod
    def check_response(resp):
        pass

    def main(self):
        # url = 1
        while True:
            url = self.queue_handle()
            if url:
                resp = self._get(url)
                self.check_response(resp)
                self.parse_detail(resp)
            else:
                print('customer sleep 30s...')
                time.sleep(30)

    def start(self):
        print('customer start...')
        self.main()
        print('customer end...')


if __name__ == '__main__':
    t = CnGoldCustomer()
    # t.main()
