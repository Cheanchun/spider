# coding:utf-8
import copy
import hashlib
import json
import random
import re
import time

import chardet
import pymongo
import redis
import requests
from lxml import etree
from lxml.etree import XMLSyntaxError

from utils.govComm import CommSession

cnn = pymongo.MongoClient('47.105.54.129', port=27017)
db = cnn.shixin
db.authenticate("chean", "scc57295729")

col = db.anjuke2020
redis_config = {
    'host': '47.105.54.129',
    'port': 6388,
    'password': 'admin'
}
user_redis = redis.StrictRedis(**redis_config)

redis_key_cookie = 'anjuke:cookies'
redis_key_detail_id = 'anjuke:id'


def read_cookies():
    cookies = {key: user_redis.hget(redis_key_cookie, key) for key in user_redis.hgetall(redis_key_cookie)}
    cookiesjar = requests.utils.cookiejar_from_dict(cookies, cookiejar=None, overwrite=True)
    return cookiesjar


def write_cookies(cookies):
    for cookie in cookies:
        user_redis.hset(redis_key_cookie, cookie.name, cookie.value)


class AnJuKe:

    def __init__(self):
        self.charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
        self.pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
        self.index_url = 'https://chengdu.anjuke.com/'
        self.session = self.instance_session(index_url=self.index_url)
        self.p_time = re.compile(r'2020年[1,2]月\d{1,2}日|今天|[1,2]月\d{1,2}日|\d{4}[-|/|.]\d{1,2}[-|/|.]\d{1,2}')
        self.detail_url = 'https://chengdu.anjuke.com/v3/ajax/map/2169/detail?str_prop_id=A{_id}&is_auction=0&is_list=1&is_pricing_top=0&click_url=&et=46cf1b&ib=1&bst=pem198'

    def _coding(self, response):
        if self.charset_re.findall(response.text):
            response.encoding = self.charset_re.findall(response.text)[0]
        elif self.pragma_re.findall(response.text):
            response.encoding = self.charset_re.findall(response.text)[0]
        else:
            temp = chardet.detect(response.content)
            response.encoding = temp['encoding']
        return response

    def _get(self, url, timeout=30, method='get', post_data=None, retry=3, **kwargs):
        """
        网页下载
        :param url:
        :return:resp
        :rtype: requests.Response
        """
        time.sleep(random.randint(15, 30))
        if method == 'get':
            for i in range(retry):
                try:
                    resp = self.session.get(url=url, timeout=timeout)
                    if resp.status_code // 100 == 2:
                        return resp
                except requests.Timeout:
                    continue
            raise requests.RequestException('requests error {}'.format(url))
        elif method == 'post' and post_data is not None:
            for i in range(retry):
                try:
                    resp = self.session.post(url=url, data=json.dumps(post_data), allow_redirects=True, timeout=timeout)
                    if resp.status_code == 200:
                        return resp
                except requests.Timeout:
                    continue
            raise requests.RequestException('requests error {}'.format(url))
        else:
            raise ValueError('func args error')

    @staticmethod
    def content2tree(response):
        if isinstance(response, requests.Response):
            return etree.HTML(response.text)
        else:
            try:
                return etree.HTML(response)
            except XMLSyntaxError as error:
                print(error)
                return response

    @staticmethod
    def instance_session(index_url=None):
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": "https://chengdu.anjuke.com/map/sale/?from=navigation",
            "x-requested-with": "XMLHttpRequest",
        }
        cookies = read_cookies()
        session = CommSession(verify=True).session(index_url=index_url, cookies=cookies) if index_url else CommSession(
            verify=True).session()
        session.headers.update(headers)
        return session

    def get_detail(self, url):
        pass

    def main(self):
        url = 'https://chengdu.anjuke.com/v3/ajax/map/sale/3671/prop_list/?room_num=-1&price_id=-1&area_id=-1&floor=-1&orientation=-1&is_two_years=0&is_school=0&is_metro=0&order_id=0&p={}&zoom=12&lat=30.229893_31.079865&lng=103.719333_104.443727&kw=&et=4dc0c0&ib=1&bst=pem152'
        for page in range(50):
            list_url = copy.copy(url).format(page)
            print 'list page {}'.format(list_url)
            data = self._get(list_url).json()
            print json.dumps(data, encoding='u8', ensure_ascii=False)
            items = data.get('val').get('props')
            for item in items:
                write_cookies(self.session.cookies)
                if not user_redis.sismember(redis_key_detail_id, item.get('id')):
                    detail = copy.copy(self.detail_url).format(_id=item.get('id'))
                    print detail
                    detail = 'https://chengdu.anjuke.com/v3/ajax/map/658/detail?str_prop_id=A1989578005&is_auction=0&is_list=1&is_pricing_top=0&click_url=&et=cc3173&ib=1&bst=pem383'
                    print 'detail url {}'.format(detail)
                    print json.dumps(item, encoding='u8', ensure_ascii=False)
                    item.update(self._get(detail).json().get('val'))
                    user_redis.sadd(redis_key_detail_id, item.get('id'))
                    item['_md5'] = self._md5(item)
                    print json.dumps(item, encoding='u8', ensure_ascii=False)
                    col.insert(item)
                    write_cookies(self.session.cookies)

    @staticmethod
    def _md5(data):
        dataStr = json.dumps(data, ensure_ascii=False).encode('u8')
        m = hashlib.md5()
        m.update(dataStr)
        _md5 = m.hexdigest()
        return _md5


if __name__ == '__main__':
    t = AnJuKe()
    t.main()
