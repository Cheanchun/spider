# -*- coding=utf-8 -*-
import functools
import math
import re
import time

import chardet
import requests
import yaml
from lxml import etree
from lxml.etree import XMLSyntaxError

charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
default_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",

}


def get_yaml_data(yaml_file):
    print("***获取yaml文件数据***")
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    data = yaml.load(file_data, Loader=yaml.Loader)
    print("类型：", type(data))
    return data


class CommSession(object):
    def __init__(self, headers=None, verify=False):
        self._session = requests.session()
        if not headers:
            self._session.headers = default_headers
        self._session.verify = verify

    def session(self, index_url=None) -> requests.sessions:
        if index_url:
            resp = self._session.get(index_url)
            print('index page'.format(resp.status_code))
        return self._session


def coding(response):
    if charset_re.findall(response.text):
        response.encoding = charset_re.findall(response.text)[0]
    elif pragma_re.findall(response.text):
        response.encoding = pragma_re.findall(response.text)[0]
    else:
        temp = chardet.detect(response.content)
        response.encoding = temp['encoding']
    return response


def content2tree(response: requests.Response):
    """

    :param response:
    :return:
    """
    if isinstance(response, requests.Response):
        return etree.HTML(response.text)
    else:
        try:
            return etree.HTML(response)
        except XMLSyntaxError as error:
            print(error)
            return response


def url_parse(response: requests.Response) -> set:
    """
    解析url 并且 格式化url
    :param response:
    :return: urls  -> list
    """
    current_url = response.url
    urls = content2tree(response.text).xpath('//a/@href')
    temp_url = set()
    for url in urls:
        url = url_filter(url, current_url)
        if url:
            temp_url.add(url)
    return temp_url


def url_filter(url: str, current_url: str = 'http://cngold.com.cn/'):
    """

    :param url:
    :param current_url:
    :return:
    """

    if url.startswith('http') and 'cngold.com.cn' in url:
        if 'www.cngold.com.cn/dealer' in url:
            return None
        if re.search(r'http://[a-z]*?.cngold.com.cn/$', url):
            return url, 1
        if re.search(r'http://www.cngold.com.cn/[a-z]+?/$', url):
            return url, 1
        if re.search(r'http://[a-z]+\.cngold\.com\.cn[/a-z]*?/20[a-z0-9]+\.html', url):
            return url, 2
    elif 'zhanhui' in current_url and url.startswith('n_20'):
        url = current_url.split('zhanhui')[0] + 'zhanhui/' + url
        return url, 2


def run_time(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        start = time.time()
        res = func(self, *args, **kwargs)
        end = time.time()
        print('run time:{}s'.format(math.ceil(end - start)))
        return res

    return wrapper


def format_url():
    pass


def check_next_page(response: requests.Response, redis, xpath='//*[contains(@title,"下一页")]'):
    """

    :param response:
    :param xpath:
    :return:
    """
    html = content2tree(coding(response))
    r = html.xpath(xpath)
    current_url: str = response.url.strip('/')
    if r:
        r = r[0].xpath('./@href')
        if (r[0].startswith('/') and 'com.cn' in current_url) and current_url.endswith('.html'):
            next_url = current_url.rsplit('/', 1)[0] + (r[0] if not r[0].startswith('/') else r[0])
            res = redis.rpush('list_page', next_url)
            print('next page add {},{}'.format(res, next_url))
        elif not r[0].startswith('/'):
            next_url = current_url.rsplit('/', 1)[0] + '/' + r[0]
            res = redis.rpush('list_page', next_url)
            print('next page add {},{}'.format(res, next_url))
        elif current_url.endswith('com.cn') and r[0].startswith('/'):
            next_url = current_url + r[0]
            res = redis.rpush('list_page', next_url)
            print('next page add {},{}'.format(res, next_url))
        elif r[0].startswith('/'):
            next_url = current_url.rsplit('/', 1)[0] + '/' + r[0]
            res = redis.rpush('list_page', next_url)
            print('next page add {},{}'.format(res, next_url))
    elif 'zhanhui' in current_url:
        if current_url.endswith('zhanhui'):
            next_url = current_url + '/index_2.html'
        else:
            next_url = 'http://www.cngold.com.cn/zhanhui/index_{}.html'.format(
                int(re.search('\d+', current_url).group()) + 1)
        res = redis.rpush('list_page', next_url)
        print('next page add {},{}'.format(res, next_url))
    else:
        print(response.url, r)


if __name__ == '__main__':
    add_list_no_repeat(user_redis='1', key='2', value='3')
# urls = [
#     'http://www.cngold.com.cn/hangye/20200426d1703n343988513.html',
#     'http://gold.cngold.com.cn/20200426d1715n343988236.html',
#     'http://forex.cngold.com.cn/20200426d1710n343979058.html',
#     'http://forex.cngold.com.cn/20200426d1711n343987533.html',
#     'http://gold.cngold.com.cn/20200426d11141n343988893.html',
# ]
# for url in urls:
#     if url_filter(url=url):
#         print(url)
#     else:
#         print('match fail:{}'.format(url))
#     # print(url)
