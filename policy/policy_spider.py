#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Alex
@date: 2020/05/20 11:11:04
@file: policy_spider.py
@usage: 政策解读公共类，通过配置文件爬取
"""
import sys

import redis

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/home/work/data/crawler3/crawler3_py/develop_jobs')

import datetime
import json
import re
import socket
import time
from urlparse import urljoin

import chardet
from lxml import etree

# from api_develop.develop_job_base import DevelopJobBase
from common_tools import exception, tools
from common_tools.common_requests import CommonRequests
from config import UrlConfig
from policy import config

ITEM = {
    'website': '',
    'refer': '',
    'category': '',
    'HTML': '',
    'HTML_length': '',
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
FILTER_URL = ['javascript:void(0);', 'javascript:;']
CHARSET_RE = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
PRAGMA_RE = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
ATTACH_RE = re.compile(r'(https?://.*.(doc|docx|xls|xlsx|pdf|zip|rar|7z|gif|jpg|jpeg|png|bmp).*?)')

redis_config = {'host': '47.105.54.129', 'port': 6388, 'password': 'admin', 'db': 10}


class PolicyCommon():
    """
    政策解读公共类，通过配置文件爬取
    """

    def __init__(self):
        # super(PolicyCommon, self).__init__()
        self.topic_id = 'b31d8e04-eba3-4670-969a-ead93d27464e'
        self.user_redis = redis.Redis(**redis_config)

        self.website = None
        self.category = None
        self.handler = None

        self.list_xpath = None  # 列表解析内容URL的xpath
        self.title_xpath = None  # 标题xpath
        self.attach_xpath = None  # 附件xpath
        self.second_num = None  # 列表页第二页的页码数字
        self.max_pages = None  # 列表最大页数
        self.index = None  # 首页url
        self.list_format = None  # 翻页format

        self.is_finished = None  # 是否爬完全量
        self.list_redis = 'policy:all_list'
        self.crawled_urls = 'policy:crawled_urls'

        self.error_list = 'policy:error_list'

        self.common_requests = None  # 实例化请求类

    def main(self):
        """
        程序入口, 可重写
        :return:
        """
        self._initialize()
        self._start_crawl()
        self.user_redis.set(self.is_finished, '1')

    def save_all_list(self):
        """
        将url配置存入redis
        :return:
        """
        for url_config in config.CONFIG:
            self.user_redis.rpush(self.list_redis, str(url_config))

    def _initialize(self):
        """
        获取基础数据
        :return:
        """
        # 第一次时将config中的配置存入redis
        if not self.user_redis.exists(self.list_redis):
            self.save_all_list()

        # 从redis中取一个url
        url_config = self.user_redis.lpop(self.list_redis)
        self.user_redis.rpush(self.list_redis, url_config)
        url_config = eval(url_config)
        if not isinstance(url_config, UrlConfig):
            return None

        # 判断是否需要proxy
        proxy_type = url_config.proxy_type or None
        self.common_requests = CommonRequests(proxy_type=proxy_type)

        # 获取一些基础数据
        self.index = url_config.index
        self.list_format = url_config.list_format
        self.list_xpath = url_config.list_xpath
        self.website = url_config.website
        self.handler = url_config.handler
        self.category = url_config.category
        self.title_xpath = url_config.title_xpath
        self.attach_xpath = url_config.attach_xpath
        self.second_num = int(url_config.second_num or 1)
        self.is_finished = url_config.redis_key

        # 获取列表页码
        self.max_pages = int(url_config.max_pages or 1)
        if self.user_redis.exists(self.is_finished):
            self.max_pages = 1
        if self.second_num == 1:
            self.max_pages = self.max_pages - 1 or 1

    def _start_crawl(self):
        """
        开始爬取
        :return:
        """
        page = 1
        while page <= self.max_pages:
            list_url = self.index
            if page > 1:
                if self.second_num == 1:
                    list_url = self.list_format.format(page - 1)
                else:
                    list_url = self.list_format.format(page)

            response = self.crawl_page(page_url=list_url)
            if response is not None:
                content_urls = self.parse_list(response=response)
                for content_url in content_urls:
                    # 判断是否已经爬取过
                    if self._is_crawl_url(url=content_url):
                        continue

                    response = self.crawl_page(page_url=content_url)
                    if response is None:
                        continue
                    try:
                        data = self.parse_content(response=response)
                        # self.save_topic_data(content_url, data, self.topic_id)
                        print(json.dumps(data, ensure_ascii=False))
                        print('parse content success and save!')

                        # save this url to redis
                        self.user_redis.sadd(self.crawled_urls, content_url)
                    except Exception as ex:
                        print('get content error, {}'.format(ex))
            else:
                self._save_error_list(error_url=list_url)
            page += 1

    def _save_error_list(self, error_url):
        """
        将出错的列表url存入redis
        :param error_url:
        :return:
        """
        error = {
            'website': self.website,
            'index': self.index,
            'error_url': error_url,
            'error_time': '{}'.format(datetime.datetime.now()),  # 获取出错时间
            'hostname': socket.gethostname()  # 获取主机名
        }
        self.user_redis.lpush(self.error_list, json.dumps(error))

    def _is_crawl_url(self, url):
        """
        是否已经爬取过
        :param url:
        :return:
        """
        try:
            if self.user_redis.exists(self.crawled_urls) and self.user_redis.sismember(self.crawled_urls, url):
                return True
        except Exception as ex:
            print('operate redis error! reason: {}'.format(ex.message))
        return False

    def crawl_page(self, page_url, param=None):
        """
        爬取页面
        :param page_url:
        :param param:
        :return:
        """
        print(u'crawl page: {}, param: {}'.format(page_url, param))
        if param is None:
            param = {}
        try:
            response = self.common_requests.retry_download_page(url=page_url, **param)
            if response is not None:
                return response
        except exception.BaseError as ex:
            print('download page error, {}'.format(ex))
        except Exception as ex:
            print('crawl page error: {}'.format(ex))
        return None

    @staticmethod
    def _coding(response):
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

    def parse_list(self, response):
        """
        解析列表
        :param response:
        :return:
        """
        html = etree.HTML(response.text)
        temps = html.xpath(self.list_xpath)
        urls = []
        for temp in temps:
            if not temp.startswith('http'):
                temp = urljoin(response.url, temp)
            urls.append(temp)
        return urls

    def parse_content(self, response):
        """
        解析内容页
        :param response:
        :return:
        """
        response = self._coding(response)
        item = dict(ITEM)
        item['website'] = self.website
        item['category'] = self.category
        item['handler'] = self.handler
        item['HTML'] = response.text
        item['HTML_length'] = len(response.text)
        item['refer'] = response.url
        item['invTime'] = int(time.time() * 1000)
        item['dataId'] = tools.make_sha256(text=item['refer'])

        html = etree.HTML(response.text)
        item['anchorText'] = ''.join(html.xpath(self.title_xpath or '//title/text()')).strip()

        attach_temps = html.xpath(self.attach_xpath or '//a')
        item['attachments'], item['attachments_detail'] = self._parse_attach(attaches=attach_temps,
                                                                             base_url=response.url)
        return item

    def _parse_attach(self, attaches=None, base_url=''):
        """
        解析附件
        :param attaches:
        :param base_url:
        :return:
        """
        attachments = []
        attachments_detail = []
        if attaches is not None:
            for temp in attaches:
                attach_url = ''.join(temp.xpath('./@href')).strip()
                # 过滤，排除非法的
                if attach_url in FILTER_URL:
                    continue
                # 格式化URL
                if not attach_url.startswith('http'):
                    attach_url = urljoin(base_url, attach_url)
                # 验证URL
                if not ATTACH_RE.findall(attach_url):
                    continue

                md5_url = tools.make_md5(text=attach_url)
                suffix = attach_url.split('.')[-1].split('?')[0]
                filename = '{}.{}'.format(md5_url, suffix)
                # 判断是否已经添加过
                if filename in attachments:
                    continue

                # resp = self.crawl_page(page_url=attach_url, param={'stream': True})
                # if resp is None:
                #     continue
                print(attach_url, filename)
                # self.save_file(source_stream=resp, filename=filename, source_url=attach_url)

                # attachments
                attachments.append(filename)

                # attachments_detail
                attachment = dict(ATTACHMENT)
                # 当anchorText没有文件名时，用附件url的md5
                attachment['anchorText'] = ''.join(temp.xpath('.//text()')).strip() or md5_url
                attachment['file'] = filename
                attachment['url'] = attach_url
                attachments_detail.append(attachment)
        return attachments, attachments_detail


if __name__ == '__main__':
    PolicyCommon().main()
