#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Alex
@date: 2020/06/09 14:57:43
@file: formatter.py
@usage: 格式化数据
"""
import time

from common_tools import tools
from policy_module import configuration


class Formatter(object):
    def __init__(self, website, category, handler, parser):
        self.website = website
        self.category = category
        self.handler = handler
        self.parser = parser

    def format_data(self, content_url, content_title, response):
        """
        格式化数据，响应不为空，表示为正常内容页，否则是附件
        :param content_url:
        :param content_title:
        :param response:
        :return:
        """
        html = ''
        if response:
            if isinstance(response, unicode):
                html = response
            else:
                response = tools.coding(response)
                html = response.text
        data = dict(configuration.ITEM)
        data['website'] = self.website
        data['refer'] = content_url
        data['category'] = self.category
        data['anchorText'] = content_title
        data['handler'] = self.handler
        data['invTime'] = int(time.time() * 1000)
        data['dataId'] = tools.make_sha256(content_url)
        data['HTML'] = html
        data['HTML_length'] = len(data.get('HTML'))
        if html:
            # 从正常内容页中解析出附件信息
            attach_temps = self.parser.parse_content(response=html, base_url=content_url)
        else:
            # 构造附件信息
            attach_temps = [{'attach_title': content_title, 'attach_url': content_url}]
        # 格式化附件信息
        data['attachments'], data['attachments_detail'] = self.format_attach(attaches=attach_temps)
        return data

    @staticmethod
    def format_attach(attaches):
        """
        格式化附件
        :param attaches:
        :return:
        """
        attachments = []
        attachments_detail = []
        for attach in attaches:
            attach_url = attach.get('attach_url')
            md5_url = tools.make_md5(text=attach_url)
            suffix = attach_url.split('.')[-1].split('?')[0]
            filename = '{}.{}'.format(md5_url, suffix)
            attachments.append(filename)

            attachment = dict(configuration.ATTACHMENT)
            attachment['anchorText'] = attach.get('attach_title') or md5_url
            attachment['file'] = filename
            attachment['url'] = attach_url
            attachments_detail.append(attachment)
        return attachments, attachments_detail
