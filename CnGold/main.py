# -*- coding:utf-8 -*-
import random
import time
import traceback

import redis
import yaml

import requests

from CnGold.utils import CommSession, url_parse, get_yaml_data

config = get_yaml_data('./config.yml')

print(config)


class CnGoldSpider(object):
    def __init__(self):
        self.index_url = 'http://www.cngold.com.cn/'
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
        if not self.user_redis.exists('first_level'):
            self.user_redis.sadd('first_level', self.index_url)
        for url, _type in url_parse(self._get(self.user_redis.spop('first_level'))):
            if _type == 1:
                self.user_redis.sadd('second_level', url)
            elif _type == 2:
                self.user_redis.sadd('third_level', url)
            else:
                print('other')


if __name__ == '__main__':
    t = CnGoldSpider()
    t.main()
