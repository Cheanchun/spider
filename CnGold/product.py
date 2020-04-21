# -*- coding:utf-8 -*-
import random
import time
import traceback

import redis
import requests

from CnGold.utils import CommSession, url_parse, get_yaml_data, check_next_page

config = get_yaml_data('./config.yml')

print(config)


class CnGoldSpider(object):
    def __init__(self):
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
        current_url = self.user_redis.lpop('list_page')
        print('current url:{}'.format(current_url))
        self.user_redis.lrem('list_page', count=1, value=current_url)
        resp = self._get(current_url)
        check_next_page(resp, self.user_redis)
        for url, _type in url_parse(resp):
            if not self.user_redis.sismember('crawled_url', url):
                if _type == 1 and not self.user_redis.sismember('crawled_url', url):
                    print('list_page_remove', self.user_redis.lrem('list_page', count=0, value=url))
                    print('list_page_add', self.user_redis.lpush('list_page', url))
                    print(1, url)
                elif _type == 2 and not self.user_redis.sismember('crawled_url', url):
                    print('list_page_remove', self.user_redis.lrem('detail_page', count=0, value=url))
                    print('list_page_add', self.user_redis.rpush('detail_page', url))
                    print(2, url)
                elif self.user_redis.sismember('crawled_url', url):
                    print('url crawled:{}'.format(url))
                else:
                    print('other url:{}'.format(url))
        self.user_redis.sadd('crawled_url', current_url)


if __name__ == '__main__':
    t = CnGoldSpider()
    t.main()
