#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Alex
@date: 2020/06/02 11:41:21
@file: parser.py
@usage: TODO
"""
import re
from urlparse import urljoin

import requests
from lxml import etree

from common_tools import tools
from policy_module import configuration


class Parser(object):
    def __init__(self, list_parse_type, list_parse_rule, content_format, attach_xpath=None, logger=None):
        self.list_parse_type = list_parse_type
        self.list_parse_rule = list_parse_rule
        self.content_format = content_format
        self.attach_xpath = attach_xpath
        self.logger = logger

    def parse_list(self, response):
        """
        解析列表
        :param response:
        :return:
        """
        if self.list_parse_type.lower() == 'xpath':
            if isinstance(response, unicode):
                html = etree.HTML(response)
            else:
                response = tools.coding(response=response)
                html = etree.HTML(response.text)
            temps = html.xpath(self.list_parse_rule)
        elif self.list_parse_type.lower() == 're':
            temps = self.list_parse_rule.finditer(response.text)
            temps = [temp.groupdict() for temp in temps]
        else:
            temps = []
        content_urls = []
        for temp in temps:
            if self.list_parse_type.lower() == 'xpath':
                url = ''.join(temp.xpath('./@href'))
                if temp.xpath('./@title'):
                    title = ''.join(temp.xpath('./@title'))
                else:
                    title = ''.join(temp.xpath('.//text()'))
            else:
                url = temp.get('url')
                if self.content_format:
                    url = self.content_format.format(url)
                title = temp.get('title')
            if isinstance(response, requests.Response) and not url.startswith('http'):
                url = urljoin(response.url, url)
            title = re.sub(configuration.NOT_NEED_PATTERN, '', ''.join(title))
            content_urls.append({'url': url, 'title': title})
        return content_urls

    def parse_content(self, response, base_url=''):
        """
        通过内容页response解析出附件数据
        :param response:
        :param base_url:
        :return:
        """
        if isinstance(response, unicode):
            html = etree.HTML(response)
        else:
            response = tools.coding(response=response)
            html = etree.HTML(response.text)

        attach_temps = html.xpath(self.attach_xpath or '//a')
        attaches = []
        for temp in attach_temps:
            attach_url = ''.join(temp.xpath('./@href')).strip()
            # 过滤，排除非法的
            if attach_url in configuration.FILTER_URL:
                continue
            # 格式化URL
            if not attach_url.startswith('http'):
                attach_url = urljoin(base_url, attach_url)
            # 验证URL
            if not configuration.ATTACH_RE.findall(attach_url):
                continue
            # 排除重复的
            if attach_url in [tmp.get('url') for tmp in attaches]:
                continue

            attach_title = re.sub(configuration.NOT_NEED_PATTERN, '', ''.join(temp.xpath('.//text()')).strip())
            attaches.append({'title': attach_title, 'url': attach_url})
        return attaches
