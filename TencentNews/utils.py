# -*- coding=utf-8 -*-
import functools
import json
import math
import re
import time

import chardet
import requests
import yaml

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


def url_parse(response: requests.Response) -> set:
    """
    解析url 并且 格式化url
    :param response:
    :return: urls  -> list
    """
    json_str = coding(response).text
    json_dict = json.loads(json_str[json_str.index('{'):json_str.rindex('}') + 1])
    urls = set()
    for data in json_dict.get('data'):
        urls.add(data.get('vurl'))
    print(urls)
    return urls


def next_page(url: bytes, redis, redis_key, page=5):
    url = url.decode('u8')
    res = re.search(r'(page=\d+)', url)
    if res:
        page_str = res.group()
        page_num = page_str.split('=')[1]
        if int(page_num) < page:
            url = url.replace(page_str, 'page={}'.format(int(page_num) + 1))
            redis.rpush(redis_key, url)
    else:
        print('next page format error:{}'.format(url))


def run_time(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        start = time.time()
        res = func(self, *args, **kwargs)
        end = time.time()
        print('run time:{}s'.format(math.ceil(end - start)))
        return res

    return wrapper


if __name__ == '__main__':
    pass
