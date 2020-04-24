# -*- coding:utf-8 -*-
import random
import re
import time
import traceback

import chardet
import requests
from lxml import etree
from lxml.etree import XMLSyntaxError

from CnGold.utils import CommSession, url_parse


class CnGoldSpider(object):
    def __init__(self):
        self.index_url = 'http://www.cngold.com.cn/'
        self.session = self.instance_session()

    def instance_session(self):
        return CommSession(verify=True).session(self.index_url)

    def _get(self, url, timeout=30, method='get', post_data=None, retry=3):
        """
        网页下载
        :param url:
        :return:resp
        :rtype: requests.Response
        """
        for _ in range(retry):
            try:
                time.sleep(random.randint(3, 5))
                if method == 'get':
                    resp = self.session.get(url=url, timeout=timeout)
                elif method == 'post' and post_data is not None:
                    resp = self.session.post(url=url, data=post_data, allow_redirects=True, timeout=timeout)
                else:
                    raise ValueError('request method not support')
            except requests.exceptions:
                continue
            if resp.status_code // 100 == 2:
                return resp
        raise traceback.format_exc()

    def main(self):
        print(url_parse(self._get(self.index_url)))


if __name__ == '__main__':
    t = CnGoldSpider()
    t.main()
