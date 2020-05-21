# -*- coding: utf-8 -*-
"""
@author:white
@date: 2020/05/18
@file: white_china_safty.py
@usage: 政策智读-中国应急管理部-基础类
"""
import hashlib
import re
import time
import urlparse
from urlparse import urljoin, urlparse

import chardet
import requests
from lxml import etree
from retrying import retry

CHARSET_RE = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
PRAGMA_RE = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)


class ZczdBase():
    def __init__(self):
        # super(ZczdBase, self).__init__()
        self.file_save_path = '{}'
        self.file_pattern = re.compile(
            r'^(https?://.*(docx|doc|xls|xlsx|ppt|pptx|pdf|rar|txt|zip|7z|raw|jpg|jpeg|gif|png|bmp|tif|wps))$', re.S)
        self.handler = ''
        self.website = ''
        self.pass_list = ['javascript:void(0);', 'javascript:;']
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', }

    def parse_file(self, detail_url, html, cookie):
        """
        将得到的文件url及文件名的touple进行解析为需要的格式
        :param detail_url:
        :param html:
        :param cookie:
        :return:
        """
        file_list = self._get_file(detail_url, html)
        if not file_list:
            return {
                "attachements": [],
                "attachements_detail": []
            }
        attachements = []
        attachements_detail = []
        for singal_file_item in file_list:
            anchor_text = singal_file_item[1]
            url = singal_file_item[0]
            mfile_name = self.connect_mfile_name(url)
            _file = self.file_save_path.format(mfile_name)
            data_item = {"anchorText": anchor_text, "url": url, "file": _file}
            attachements_detail.append(data_item)
            attachements.append(_file)
            try:
                self.download_file(url, mfile_name, cookie)
            except Exception as ex:
                self.logger.error('[logger: download file error , msg: {}]'.format(ex))
        return {
            "attachements": attachements,
            "attachements_detail": attachements_detail
        }

    def _get_file(self, detail_url, html):
        """
        获取到当前详情页的所有a标签，通过正则对附件进行筛选，并返回文件url及文件名
        :param detail_url:
        :param html:
        :return:
        """
        files_list = []
        file_items = html.xpath('//a')
        for file_item in file_items:
            url = ''.join(file_item.xpath('./@href'))
            if url in self.pass_list:
                continue
            if not url.startswith('http'):
                url = urljoin(detail_url, url)
            if re.findall(self.file_pattern, url):
                file_url = re.findall(self.file_pattern, url)[0][0]
                file_name = ''.join(file_item.xpath('.//text()')).strip() if file_item.xpath(
                    './/text()') else self.make_md5(file_url)
                if len(file_name) < 3:
                    continue
                files_list.append((file_url, file_name))
        return files_list

    @retry(stop_max_attempt_number=3)
    def download_file(self, url, file_save_name, cookie):
        """
        下载文件
        :param url:
        :param file_save_name:
        :param cookie:
        :return:
        """
        if cookie:
            self.headers.update({'cookie': cookie})
        resp = requests.get(url, headers=self.headers, stream=True)
        # self.save_file(source_stream=resp, filename="{}".format(file_save_name),
        #                source_url=url)

    @staticmethod
    def coding(response):
        """
        获取页面响应的编码
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

    def connect_mfile_name(self, url):
        """
        将url的md5与文件后缀拼接，生成mfile的保存文件名
        :param url:
        :return:
        """
        suffix = url.split('.')[-1]
        url_md5 = self.make_md5(url)
        return url_md5 + suffix

    def save_data(self, detail_url, resp, category, topic_id, cookie=None):
        """
        解析详情页并保存数据
        :param detail_url:
        :param resp:
        :param category:
        :param topic_id:
        :param cookie:
        :return:
        """
        if None in [detail_url, resp, category, topic_id]:
            raise ValueError
        html = etree.HTML(resp.text)
        # 调用parse_file接口获取到文件的两个字段的数据
        file_data_dict = self.parse_file(detail_url, html, cookie)
        anchor_text = ''.join(html.xpath('//title/text()'))
        refer = detail_url
        html_data = resp.text
        html_length = len(html_data)
        inv_time = int(time.time()) * 1000
        data_id = self.make_sha256(detail_url)
        save_data = {"anchorText": anchor_text, "refer": refer, "HTML": html_data,
                     "HTML_length": html_length, "category": category,
                     "invTime": inv_time, "dataId": data_id,
                     "handler": self.handler, "website": self.website}
        save_data.update(file_data_dict)
        # self.save_topic_data(detail_url, save_data, topic_id)

    @staticmethod
    def make_md5(url):
        """
        返回md5加密后的url
        """
        md5 = hashlib.md5(url.encode()).hexdigest()
        return md5

    @staticmethod
    def make_sha256(url):
        """
        返回sha256加密后的url
        """
        sha256 = hashlib.sha256(url.encode()).hexdigest()
        return sha256

    def make_source_save_filename(self, url):
        """
        返回md5加密后的字符串作为source的文件名
        """
        suffix = '.html.txt'
        basename = self.make_md5(url)
        filename = "".join([basename, suffix])
        return filename

    @staticmethod
    def gen_file_save_path(url):
        """
        根据url拼接下载文件保存路径
        :param url:
        :return:
        """
        url = urlparse.unquote(url)
        pr = urlparse.urlparse(url)
        lf = pr.netloc + pr.path

        if pr.query:
            lf = pr.netloc + pr.path + '?' + pr.query

        return lf


if __name__ == '__main__':
    ZczdBase()
