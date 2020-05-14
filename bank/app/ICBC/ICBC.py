# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import json
import random
import time
import traceback

import requests
import yaml

from bank.utils.utils import CommSession

file_path = './config.yaml'


def get_yaml_data(yaml_file):
    print("***获取yaml文件数据***")
    with open(yaml_file, 'r', encoding="utf-8") as file:
        file_data = file.read()
        data = yaml.load(file_data, Loader=yaml.Loader)
    return data


CONFIG = get_yaml_data(file_path)
POST_DATA = CONFIG.get('post_data')
BASE_FORMAT = CONFIG.get('base_format')
URL = CONFIG.get('url')
INDEX_URL = CONFIG.get('index_url')

HEADERS = {
    "Host": "mywap2.icbc.com.cn",
    "Accept": "*/*",
    "X-ICBC-Channel-Client": "AsyncRequest",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "br, gzip, deflate",
    "Cache-Control": "no-cache",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://mywap2.icbc.com.cn",
    "User-Agent": "ICBCiPhoneBSNew F-WAPB 3.0.1.3 fullversion:3.0.1.3 newversion:5.1.0.4.0 iPhone10,3 12.2 CE95C2AC-3C65-4FAA-9634-9A59CFE4E2D5 4G Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BSComponentVersion:5.1",
    "Referer": "https://mywap2.icbc.com.cn/ICBCWAPBank/ebdpui/dss/aperson/mainpage/clientNew_finance_purchase_list_noSession_new.html",
    "Content-Length": "405",
    "Connection": "keep-alive",
    "Cookie": "SRV_WAPB-PUBLIC_WEB=rs282|XrZcD|XrZbr; BIGipServerWAPB_NanFangYeWu_SLB_PAAS_80_POOL_IPV4V6=1762763018.20480.0000; JSESSIONID=0000iHsVrXkQA7IPuDttsWv1EEm:-1; area_1002=1002",
}


class ICBC(object):
    def __init__(self):
        self.session = self.instance_session()

    def instance_session(self):

        return CommSession().session()

    def _get(self, url, timeout=30, method='get', data=None, retry=3, _headers=None):
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
                    resp = self.session.get(url=url, timeout=timeout, params=data)
                elif method == 'post':
                    resp = self.session.post(url=url, data=data, allow_redirects=True, timeout=timeout)
                else:
                    raise ValueError('request method not support')
            except requests.exceptions:
                continue
            if resp.status_code // 100 == 2:
                return resp
        raise traceback.format_exc()

    def main(self):
        for page in range(1, 25):
            print('current page:{}'.format(page))
            POST_DATA['pageNumber'] = str(page)
            POST_DATA['toPage'] = str(page + 1)
            content = self._get(URL, data=POST_DATA, _headers=HEADERS, method='post').text
            content = content.strip().replace('\'', '"')
            content = json.loads(content, encoding='u8')
            if not content.get('opdata').get('jsonData'):
                break
            for data in content.get('opdata').get('jsonData'):
                self.get_production_introduce(data)

    def get_production_introduce(self, data):
        p_id = data.get('productId')
        if p_id:
            data['file_url'] = BASE_FORMAT.format(p_id)
        else:
            data['file_url'] = ''
        self.save_data(data)

    def save_data(self, data):
        print(json.dumps(data, ensure_ascii=False))


if __name__ == '__main__':
    t = ICBC()
    t.main()
