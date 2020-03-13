# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
import random

import requests
from requests.exceptions import ProxyError

_proxy = {
    # "http://117.44.11.157:4276": 0,
    # "http://14.106.106.18:4237": 0,
    # "http://121.57.166.196:4245": 0,
    # "http://119.116.97.72:4284": 0,
    # "http://58.52.50.41:4282": 0,
    # "http://114.237.41.113:4256": 0,
    # "http://223.242.175.128:4227": 0,
    "http://59.63.52.12:4282": 0,
}


def get_proxy():
    # proxy = random.choice(self._proxy)
    proxy = random.sample(_proxy.keys(), 1)[0]
    # print(proxy)
    proxies = {
        # "http": proxy,
        "https": proxy,
    }
    return proxies


def _request_http(url, headers):
    retry_count = 3
    while retry_count:
        retry_count -= 1
        try:
            proxies = get_proxy()
            print(proxies)
            print(url)
            response = requests.get(url=url, headers=headers, timeout=10, proxies=proxies)
            # response = requests.get(url=url, headers=headers, timeout=3)
            if response.content and response.status_code == 200:
                if not response.encoding or response.encoding == 'ISO-8859-1':
                    response.encoding = requests.utils.get_encodings_from_content(response.text)[0]
                if response.encoding == 'gb2312':
                    response.encoding = 'gbk'
                return response
            else:
                print(u'error-请求失败：{}'.format(response.status_code))
        except ProxyError as e:
            # _proxy[proxies['http']] += 1
            print(u'代理异常{}'.format(e))
        except Exception as e:
            print(u'error-请求异常：{}'.format(e))


if __name__ == '__main__':
    url_list = ['http://news.sina.com.cn/c/2019-06-27/doc-ihytcitk8014709.shtml',
                'https://baijiahao.baidu.com/s?id=1636641069851277053&wfr=spider&for=pc',
                u'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=保利&pn=0']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    for url in url_list:
        res = _request_http(url, headers)
        print(res.status_code)
