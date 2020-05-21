#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Alex
@date: 2020/04/23 08:46:25
@file: common_requests.py
@usage: 公共配置，超时时间，默认请求头，selenium配置等
"""
DEFAULT_TIMEOUT = 30
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
DEFAULT_HEADERS = {
    'User-Agent': USER_AGENT
}
MAX_TRY_TIMES = 3
ALLOW_METHODS = ['GET', 'POST']
ALLOW_PARAMETER = {
    # requests 请求需要
    'headers': dict,
    'timeout': int,
    'allow_redirects': bool,
    'stream': bool,
    'data': dict,
    'json': dict,
    'cookies': dict,
    'proxies': dict,
    'verify': bool,
    'cert': (str, tuple),

    # 最大尝试次数
    'max_try_times': int,
    # 睡眠时间
    'sleep_time': (tuple, list),

}

# 芝麻代理
ZHIMA_PROXY_URL = 'http://http.tiqu.alicdns.com/getip3?num=1&type=1&pro=&city=0&yys=0&port=1&pack=35251&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
# 阿布云代理
ABUYUN_PROXY = {
    'host': 'http-cla.abuyun.com',
    'port': 9030,
    'username': 'H4T896TN62PR7M0C',
    'password': '8F4FE31A5F6D25B3'
}
ABUYUN_SWITCH_IP = 'http://proxy.abuyun.com/switch-ip'
