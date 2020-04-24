# -*- coding=utf-8 -*-

import re

import chardet
import requests
from lxml import etree
from lxml.etree import XMLSyntaxError
import os


charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
default_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",

}


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


def url_parse(response: requests.Response) -> list:
    """
    解析url 并且 格式化url
    :param response:
    :return: urls  -> list
    """
    current_url = response.url
    urls = content2tree(response.text).xpath('//a/@href')
    temp_url = []
    for url in urls:
        url = url_filter(url)
        if url:
            temp_url.append(url)
    return temp_url


def url_filter(url: str):
    """

    :param url:
    :return:
    """

    if url.startswith('http') and 'cngold.com.cn' in url:
        return os.path.split(url)
