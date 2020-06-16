#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Alex
@date: 2020/06/02 16:32:29
@file: configuration.py
@usage: TODO
"""
import re

FILTER_URL = ['javascript:void(0);', 'javascript:;']
ATTACH_RE = re.compile(r'(https?://.*.(doc|docx|xls|xlsx|pdf|zip|rar|7z|gif|jpg|jpeg|png|bmp).*?)')
NOT_NEED_PATTERN = re.compile(ur'\n| |Â|\\')

ITEM = {
    'website': '',
    'refer': '',
    'category': '',
    'HTML': '',
    'HTML_length': 0,
    'attachments': [],  # 附件路径列表
    'attachments_detail': [],  # 附件详细列表  ATTACHMENT
    'anchorText': '',
    'handler': '',
    'invTime': '',
    'dataId': '',  # sha256(url)
    # 'publish_time': '',  # 已废弃
}
ATTACHMENT = {
    'anchorText': '',
    'file': '',
    'url': ''
}
