# -*- coding:utf-8 -*-
import random
import time
import traceback

import pymongo
import redis
import requests
from IntelligentContentParse.intelligent_parse import IntelligentParse
from utils import CommSession, url_parse, get_yaml_data, run_time, coding, content2tree, next_page

config = get_yaml_data('./config.yml')
print(config)
user_redis = redis.Redis(**config.get('redis_config'))
ColKey = 'TencentNews:column'
DetailKey = 'TencentNews:detail'
CrawlKey = 'TencentNews:crawled'


def cnn_mongo(mongo_config):
    cnn = pymongo.MongoClient(host=mongo_config.get('host'), port=mongo_config.get('port'))
    db = cnn['shixin']
    db.authenticate(mongo_config.get('user'), mongo_config.get('password'))
    col = db['tencentnews']
    return col


tencentnews = cnn_mongo(config.get('mongo_config'))


class TencentNewsProducer(object):
    def __init__(self):
        super(TencentNewsProducer, self).__init__()
        self.index_url = config.get('site_config').get('index')
        self.session = self.instance_session()
        self.user_redis = redis.Redis(**config.get('redis_config'))

    def instance_session(self):
        return CommSession(verify=False).session(self.index_url)

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

    def get_redis_url(self):
        if not self.user_redis.exists(ColKey):
            self.user_redis.rpush(ColKey, *config.get('nav_url'))
        return self.user_redis.lpop(ColKey)

    @run_time
    def main(self):
        current_url = self.get_redis_url()
        if current_url:
            print('current url:{}'.format(current_url))
            try:
                self.user_redis.lrem(ColKey, count=1, value=current_url)
                self.user_redis.sadd(CrawlKey, current_url)
                resp = self._get(current_url)
                next_page(current_url, self.user_redis, ColKey)
                for url in url_parse(resp):
                    if not self.user_redis.sismember(CrawlKey, url):
                        self.user_redis.lrem(DetailKey, count=0, value=url)
                        self.user_redis.rpush(DetailKey, url)
            except Exception:
                print(traceback.format_exc())

    def start(self):
        print('product start...')
        while True:
            self.main()
            print('product end...sleep 5s,waiting next running')
            # time.sleep(5)


class TencentNewsConsumer(object):
    def __init__(self):
        self.user_redis = user_redis
        self.index_url = config.get('site_config').get('index')
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

    @run_time
    def main(self):
        for _ in range(config.get('max_page')):
            try:
                detail_info = self.user_redis.lpop(DetailKey)
                self.user_redis.sadd(CrawlKey, detail_info)
                detail_info = detail_info.decode('u8').split('|')
                detail_url, source, publish_time = detail_info[0], detail_info[1], detail_info[2]
                resp = self._get(detail_url)
                self.parse_data(resp=resp, source=source, publish_time=publish_time)
            except Exception:
                print(traceback.format_exc())

    def parse_data(self, resp, source, publish_time):
        data = {}
        resp = coding(resp)
        html = content2tree(response=resp)
        for key, xpath in config.get('parse_config').items():
            data[key] = html.xpath(xpath)
        data['content'] = IntelligentParse(html=coding(resp).text).intelligent_main()
        data['source'] = source
        data['publish_time'] = publish_time
        data['url'] = resp.url
        self.save_data(data)

    def save_data(self, data):
        tencentnews.insert(data)
        print(data)


if __name__ == '__main__':
    # t = TencentNewsProducer()
    # t.start()
    t = TencentNewsConsumer()
    t.main()
