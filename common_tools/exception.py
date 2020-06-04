#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Alex
@date: 2020/04/23 08:46:25
@file: common_requests.py
@usage: 自定义异常库
"""


class BaseError(Exception):
    """
    基础异常类
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return '{}'.format(self.msg)


class MethodError(BaseError):
    """
    请求方式异常
    """
    # def __init__(self, msg):
    #     super(MethodError, self).__init__(msg)
    pass


class GetProxyError(BaseError):
    """
    获取代理异常
    """
    pass


class DownloadError(BaseError):
    """
    下载异常
    """
    pass


if __name__ == '__main__':
    def test():
        raise MethodError(u'测试')
