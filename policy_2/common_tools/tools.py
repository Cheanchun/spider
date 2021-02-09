#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Alex
@date: 2020/04/23 08:46:25
@file: common_requests.py
@usage: 工具方法，随机睡眠, 去除特殊字符等
"""
import sys

import chardet
import re


PRAGMA_RE = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
CHARSET_RE = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/home/work/data/crawler3/crawler3_py/develop_jobs')

import hashlib
import random
import re
import six
import time

import requests

from policy.common_tools import config, exception

def random_sleep_time(start=1, stop=5):
    """
    随机睡眠
    :param start: 最少时间，默认1
    :param stop: 最大时间，默认5
    :return:
    """
    if not (isinstance(start, int) and isinstance(stop, int)):
        raise TypeError('start or stop value must be a integer.')
    if start > stop:
        raise ValueError('start value must be less than stop value.')
    # assert isinstance(start, int), 'start must be a integer.'
    # assert isinstance(stop, int), 'stop must be a integer.'
    # assert start <= stop, 'start value must be less than stop value.'

    time.sleep(random.randint(start, stop))

def coding(response):
    """
    设置编码
    :param response:
    :return:
    """
    if CHARSET_RE.findall(response.text):
        response.encoding = CHARSET_RE.findall(response.text)[0]
    elif PRAGMA_RE.findall(response.text):
        response.encoding = PRAGMA_RE.findall(response.text)[0]
    else:
        temp = chardet.detect(response.content)
        response.encoding = temp['encoding']
    return response
def make_md5(text):
    """
    对字符串进行md5加密
    :param text:
    :return:
    """
    md5_text = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_text


def make_sha256(text):
    """
    对字符串进行sha256加密
    :param text:
    :return:
    """
    sha256_text = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return sha256_text


def replace_escape_chars(text, which_ones=('\n', '\t', '\r',u'\u3000',u'\xa0','\v','&nbsp;'), replace_by=u'', encoding=None):
    """
    #去除\n,\t,\r等特殊字符
    """
    def to_unicode(text, encoding=None, errors='strict'):
        if isinstance(text, six.text_type):
            return text
        if not isinstance(text, (bytes, six.text_type)):
            raise TypeError('to_unicode must receive a bytes, str or unicode '
                            'object, got %s' % type(text).__name__)
        if encoding is None:
            encoding = 'utf-8'
        return text.decode(encoding, errors)
        
    text = to_unicode(text, encoding)
    for ec in which_ones:
        text = text.replace(ec, replace_by)
    return text


def get_zhima_proxy():
    """
    获取芝麻代理
    :return:
    """
    proxy_url = config.ZHIMA_PROXY_URL
    # 芝麻代理URL，处理成 每次去一个IP，以\r\n为分隔符，数据返回格式为txt
    proxy_url = re.sub(r'num=\d+', r'num=1', proxy_url)
    proxy_url = re.sub(r'type=\d+', r'type=1', proxy_url)
    proxy_url = re.sub(r'lb=\d+', r'lb=1', proxy_url)

    try:
        res = requests.get(proxy_url, headers=config.DEFAULT_HEADERS)
        if '"success":false' not in res.text:
            proxy = {'http': 'http://{}'.format(res.text.split('\r\n')[0])}
            return proxy
        else:
            res_data = res.json()
            raise exception.GetProxyError(
                'get proxy error, code: {}, msg: {}'.format(res_data.get('code'), res_data.get('msg')))
    except requests.RequestException as ex:
        raise exception.GetProxyError('get proxy error: {}'.format(ex))


def get_abuyun_proxy():
    """
    设置阿布云代理
    :return:
    """
    proxy_meta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": config.ABUYUN_PROXY.get('host'),
        "port": config.ABUYUN_PROXY.get('port'),
        "user": config.ABUYUN_PROXY.get('username'),
        "pass": config.ABUYUN_PROXY.get('password'),
    }
    proxies = {
        "http": proxy_meta,
        "https": proxy_meta,
    }
    return proxies


def switch_ip(proxy):
    """
    阿布云隧道，手动切换IP
    :param proxy:
    :return:
    """
    if not proxy:
        raise exception.GetProxyError('switch ip error, proxy is wrong')
    try:
        requests.get(config.ABUYUN_SWITCH_IP, proxies=proxy, headers=config.DEFAULT_HEADERS)
    except requests.RequestException as ex:
        raise exception.GetProxyError('requests switch ip error, {}'.format(ex))


if __name__ == '__main__':
    random_sleep_time(5, 2)
