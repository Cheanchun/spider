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


def get_yaml_data(yaml_file):
    print("***获取yaml文件数据***")
    with open(yaml_file, 'r', encoding="utf-8") as file:
        file_data = file.read()
        data = yaml.load(file_data, Loader=yaml.Loader)
    return data


FILE_PATH = 'config.yaml'
CONFIG = get_yaml_data(FILE_PATH)
API_POST_DATA = CONFIG.get('api_post_data')
INTRODUCE_POST_DATA = CONFIG.get('introduce_post_data')
DETAIL_POST_DATA = CONFIG.get('detail_post_data')
HEADERS = {
    "Host": "m1.cmbc.com.cn",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Connection": "keep-alive",
    "Cookie": "BIGipServerUEB_tongyidianziqudao_app_41002_pool=!dOotnGlznuHJAxyu7VmpjXDjWZnrfiFlytScIplQAHJNSu8DRyIzrlILBetSpAZZwTnpAi31SFiOjg==; RSESSIONID=8AB45CF0D5237AACD038EE549252315A; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; BIGipServershoujiyinhang_geren_app_8000_pool=!WQUtb0xmVyhTPWuu7VmpjXDjWZnrfvwJyuq83lOCPHjWyu1UmlpMpWvaQiu1oB3Bd6VRr9OfxkM56XI=; JSESSIONID=aT7-9qL_YDFopRH1Ng-QnnCBz___v3PFcbEZlkgWYJUBmVe8Jb5Y!1782036385; bigipW_http_m1_cookie=!W68Y4if8zVCh0DdUCAg1OdjEE0PQjeaZNiE1lPJ4lK1eF2B/5zbLbFnlpEj/l2GOUSCCZHxK1Eim3Q8=",
    "User-Agent": "CMBCPersonBank/5.30 (iPhone; iOS 12.2; Scale/3.00)",
    "Accept-Language": "zh-Hans-CN;q=1",
    "Accept-Encoding": "br, gzip, deflate",
    "Content-Length": "587",
}

introduce_post_data = CONFIG.get('introduce_post_data')
BOOK_URL = 'https://m1.cmbc.com.cn/gw/m_app/QryProductProtocol.do'
PROD_URL = 'https://m1.cmbc.com.cn/gw/m_app/QryProdListOnMarket.do'
DETAIL_URL = 'https://m1.cmbc.com.cn/gw/m_app/QueryPrdBuyInfo.do'


class PeopleLive(object):
    def __init__(self):
        self.session = self.instance_session()

    def instance_session(self):

        return CommSession(verify=False, headers=HEADERS).session()

    def get_product_introduce(self, prdCode, data):
        introduce_post_data['request']['body']['prdCode'] = prdCode
        resp = self._get(BOOK_URL, data=json.dumps(introduce_post_data, ensure_ascii=False), method='post')
        if resp.headers.get('Content-Type') == 'application/json;charset=UTF-8':
            content = resp.json()
            data['file_content'] = content.get('response').get('content')
        else:
            print('introduce return error:{}'.format(resp.text))

    def _get(self, url, timeout=30, method='get', data=None, retry=3):
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

    def api_data(self, post_data):
        json_data = self._get(PROD_URL, data=json.dumps(post_data, ensure_ascii=False), method='post').json()
        pr_list = json_data.get('response').get('prdList')
        for data in pr_list:
            self.get_detail_data(data.get('prdCode'), data)
            self.get_product_introduce(data.get('prdCode'), data)
            print(data)

    def get_detail_data(self, prdCode, data):
        DETAIL_POST_DATA['request']['body']['prdCode'] = prdCode
        resp = self._get(DETAIL_URL, data=json.dumps(DETAIL_POST_DATA, ensure_ascii=False), method='post').json()
        data['detail_info'] = resp.get('response')

    def main(self):
        for page in range(1, 5):
            API_POST_DATA['request']['body']['pageNo'] = page
            API_POST_DATA['request']['body']['pageSize'] = 20
            self.api_data(API_POST_DATA)


if __name__ == '__main__':
    p = PeopleLive()
    p.main()
