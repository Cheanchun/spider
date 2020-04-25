# -*- coding=utf-8 -*-

import re

import chardet
import requests
from lxml import etree
from lxml.etree import XMLSyntaxError
import yaml


charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
default_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",

}


def get_yaml_data(yaml_file):
    # 打开yaml文件
    print("***获取yaml文件数据***")
    file = open(yaml_file, 'r', encoding="utf-8")
    file_data = file.read()
    file.close()
    print("***转化yaml数据为字典或列表***")
    data = yaml.load(file_data, Loader=yaml.Loader)
    print(data)
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
        response.encoding = charset_re.findall(response.text)[0]
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
    :return:
    """

    if url.startswith('http') and 'cngold.com.cn' in url:
        if re.search(r'http://[a-z]*?.cngold.com.cn/$', url):
            return url, 1
        if re.search(r'http://www.cngold.com.cn/[a-z]+?/$', url):
            return url, 1
        if current_url in url:
            return url, 2


def format_url():
    pass


def check_next_page(response):
    pass
