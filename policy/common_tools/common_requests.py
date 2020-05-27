#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Alex
@date: 2020/04/23 08:46:25
@file: common_requests.py
@usage: 公共的requests，用于下载页面
"""
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/home/work/data/crawler3/crawler3_py/develop_jobs')

import requests

from policy.common_tools import config
from policy.common_tools import exception
from policy.common_tools import tools

PROXY_METHOD = {
    'zhima': tools.get_zhima_proxy,
    'abuyun': tools.get_abuyun_proxy,
}


class CommonRequests(object):
    def __init__(self, max_try_times=0, timeout=0, headers=None, proxy_type=None, session='no'):
        """
        初始化
        :param max_try_times: 最大尝试次数， 默认3次
        :param timeout: 超时时间，默认30秒
        :param headers: 请求头，默认只有User-Agent
        :param proxy_type: IP代理方式，zhima\abuyun等
        :param session: 是否使用session方式请求， yes or no
        """
        self.max_try_times = max_try_times or config.MAX_TRY_TIMES
        self.timeout = timeout or config.DEFAULT_TIMEOUT
        self.headers = headers or config.DEFAULT_HEADERS

        if proxy_type and proxy_type not in PROXY_METHOD:
            raise ValueError('proxy type value error.')
        self.proxy_type = proxy_type
        self.proxy = None
        self.get_proxy = PROXY_METHOD.get(self.proxy_type, None)

        self.session = session
        if self.session == 'yes':
            self.request_session = requests.Session()

    @staticmethod
    def _check_parameters(**kwargs):
        """
        检查 kwargs 参数
        :param kwargs:
        :return:
        """
        parameters = {}
        for key, val in kwargs.iteritems():
            if key not in config.ALLOW_PARAMETER:
                raise KeyError('parameter {} is not allowed.'.format(key))
            if val is None:
                continue
            if not isinstance(val, config.ALLOW_PARAMETER.get(key)):
                if isinstance(config.ALLOW_PARAMETER.get(key), (tuple, list)):
                    text = ' or '.join(['{}'.format(t) for t in config.ALLOW_PARAMETER.get(key)])
                else:
                    text = ''.format(config.ALLOW_PARAMETER.get(key))
                raise TypeError('parameter {} must be {}.'.format(key, text))
            parameters[key] = val
        # sleep_time 的特殊判断
        sleep_time = kwargs.get('sleep_time', None)
        if sleep_time is not None:
            if not (len(sleep_time) == 2 and isinstance(sleep_time[0], int) and isinstance(sleep_time[1], int)):
                raise ValueError('sleep time must be a list or tuple, contains two int element.')
            elif sleep_time[0] >= sleep_time[1]:
                raise ValueError('first element must be less than the second in sleep time.')
        return parameters

    def init_session(self, url, method='get', **kwargs):
        """
        初始化session，使其拥有某些状态
        :param url: 请求url
        :param method: 请求方式
        :param kwargs: 参数：headers\timeout\allow_redirects\stream\data\json_\cookies\proxies\verify\cert\max_try_times\sleep_time
        :return:
        """
        self.retry_download_page(url=url, method=method, session=self.session, **kwargs)

    def retry_download_page(self, url, method='get', session='no', **kwargs):
        """
        下载页面，失败后尝试，最多max_try_times次
        :param url: 请求url
        :param method: 请求方式
        :param session: 是否使用session方式， yes or no
        :param kwargs: 参数：headers\timeout\allow_redirects\stream\data\json_\cookies\proxies\verify\cert\max_try_times\sleep_time
        :return:
        """
        if method.upper() not in config.ALLOW_METHODS:
            raise exception.MethodError('{} is not allowed.'.format(method))

        parameters = self._check_parameters(**kwargs)

        if 'timeout' not in parameters:
            parameters['timeout'] = getattr(self, 'timeout')
        if 'headers'not in parameters:
            parameters['headers'] = getattr(self, 'headers')

        max_try_times = getattr(self, 'max_try_times')
        if 'max_try_times' in parameters:
            max_try_times = parameters.pop('max_try_times')

        sleep_time = None
        if 'sleep_time' in parameters:
            sleep_time = parameters.pop('sleep_time')

        if self.get_proxy is not None and self.proxy is None:
            self.proxy = self.get_proxy()
        parameters['proxies'] = self.proxy

        try_times = 1
        while try_times <= max_try_times:
            try:
                if session == 'yes':
                    response = self.request_session.request(method=method, url=url, **parameters)
                else:
                    response = requests.request(method=method, url=url, **parameters)
                if response.status_code / 100 == 2:
                    return response
                try_times += 1
            except requests.RequestException as ex:
                try_times += 1
                if try_times > max_try_times:
                    raise exception.DownloadError('requests download page error: {}'.format(ex))

                if self.get_proxy is not None:
                    self.proxy = self.get_proxy()
                    parameters['proxies'] = self.proxy
                if self.proxy_type in ['abuyun']:
                    # 阿布云等隧道需要手动切换IP
                    tools.switch_ip(proxy=self.proxy)
            finally:
                if sleep_time:
                    tools.random_sleep_time(*sleep_time)


if __name__ == '__main__':
    CommonRequests().retry_download_page(url='', sleep_time=(0, 1))
