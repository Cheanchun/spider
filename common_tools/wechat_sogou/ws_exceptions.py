#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Alex
@date: 2020/08/18 16:39:52
@file: ws_exceptions.py
@usage: 搜狗微信异常文件
"""
from common_tools.exception import BaseError


class WechatSogouIdentifyImgError(BaseError):
    """
    识别验证码错误
    """
    pass


class WechatSogouRequestsError(BaseError):
    """
    请求错误
    """
    pass


class WechatSogouArticleContentError(BaseError):
    """
    文章类错误
    """
    pass


class WechatSogouUrlExpireError(WechatSogouArticleContentError):
    """
    链接失效
    """
    pass


class WechatSogouArticleDeletedError(WechatSogouArticleContentError):
    """
    文章被删除
    """
    pass


class WechatSogouAccountCancelError(WechatSogouArticleContentError):
    """
    账号被注销
    """
    pass

