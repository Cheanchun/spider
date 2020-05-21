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
            self.format_data(data)

    def format_data(self, data):
        """

        :param data:
        :return:
        """
        a = {"controFlagS": "0", "startDate": "2019-07-30", "totAmt": 92800150000.0, "realEndDate": "2099-12-31",
             "liveTime": 1, "prdGrpCode": "", "nextIncomeRate": 0.0, "preIncomeRate": 0.0, "instFlag": "0",
             "prdCode": "FSAF19189A", "openTime": "000100", "endDate": "2099-12-31", "prdName": "民生天天增利灵动款理财产品",
             "currType": "156", "benchMarkMin": 0.0, "currTypeName": "人民币", "pfirstAmt": 10000.0, "prdShortName": "",
             "isDirectSell": "0", "livTimeUnitName": "1天", "NAV": 1.0, "prdAttr": "A", "incomeType": "2",
             "isNewCustPrd": "0", "prdTypeName": "活期型",
             "controlFlag": "10110 011110010 00 00 0000   4000 0007110000000010", "nextEndDate": "", "fundMode": "2",
             "clientGroups": "0", "channels": "013789", "prdType": "5", "prdGrpName": "", "bmType": "",
             "isOnlyCust": "0", "workDateList": ["2020-05-13", "2020-05-14", "2020-05-15", "2020-05-18"],
             "firstAmt": 10000.0, "sortRate": 3.1231, "closeTime": "153000", "benchMarkMax": 0.0,
             "ipoEndDate": "2019-07-29", "limitFlag": "2", "incomeRate": 0.031231, "prdNextDate": "2020-05-15",
             "usableAmt": 1530583989.0, "renegeInterTypeName": "", "transCode": "100200", "span": 0,
             "detail_info": {"psubUnit": 100.0, "realEndDate": "2099-12-31", "liveTime": 1, "remark": "",
                             "instFlag": "0", "prdCode": "FSAF19189A", "endDate": "2099-12-31",
                             "prdName": "民生天天增利灵动款理财产品", "currType": "156", "cf42": "0", "benchMarkMin": 0.0,
                             "cf41": "0", "pfirstAmt": 10000.0, "prdShortName": "", "cashFlag": "0", "forceMode": 0,
                             "livTimeUnitName": "1天", "dirStartDate": "", "incomeType": "2", "faceValue": "0.8686000",
                             "prdAttr": "A", "prdTypeName": "活期型", "nextEndDate": "", "groupPrdlist": [],
                             "clientGroups": "0", "status": "0", "channels": "013789", "ipoStartDate": "2019-07-29",
                             "prdTrusteeName": "本行",
                             "workDateList": ["2020-05-13", "2020-05-14", "2020-05-15", "2020-05-18"],
                             "ipoEndDate": "2019-07-29", "channelsName": "柜台;网银;电话;手机;直销;", "cf": "0",
                             "pminHold": 1000.0, "renegeInterTypeName": "", "pminRed": 0.01, "startDate": "2019-07-30",
                             "totAmt": 92800150000.0, "nextIncomeRate": 0.0, "preIncomeRate": 0.0, "openTime": "000100",
                             "interestType": "1", "currTypeName": "人民币", "tssTimeMap": {
                     "list": [{"startTime": "000100", "endTime": "153000", "transCode": "100200"},
                              {"startTime": "000001", "endTime": "000100", "transCode": "100201"},
                              {"startTime": "153000", "endTime": "235959", "transCode": "100201"},
                              {"startTime": "000100", "endTime": "153000", "transCode": "100202"},
                              {"startTime": "000001", "endTime": "000100", "transCode": "100203"},
                              {"startTime": "153000", "endTime": "235959", "transCode": "100203"},
                              {"startTime": "153000", "endTime": "235959", "transCode": "100204"}]}, "pappAmt": 100.0,
                             "contractFile": "C1030519002236",
                             "controlFlag": "10110 011110010 00 00 0000   4000 0007110000000010",
                             "returnCode": {"code": "AAAAAAA", "type": "S"},
                             "protocol": [{"infoType": "1"}, {"infoType": "2"}, {"infoType": "3"}],
                             "warmTipsMap": {"tipsTitle": "支持7*24小时申赎", "prdType": "5", "prd_series": "1002041",
                                             "tipsContent": "赎回支持实时到账，工作日X2前支持全额，其余时间上限10万份。(系统清算时间除外、触碰大额赎回或快速赎回上限除外)"},
                             "predUnit": 0.01, "prdType": "5", "prdRadix": "0", "bmType": "", "firstAmt": 10000.0,
                             "closeTime": "153000", "benchMarkMax": 0.0, "incomeRate": 0.031231,
                             "prdNextDate": "2020-05-15", "riskLevelName": "较低风险(二级)",
                             "transCode": [{"transCode": "100200"}, {"transCode": "100202"}]}, }
        final_data = {}
        final_data['product_status'] = '在售'
        final_data['issue_bank'] = '民生银行'
        final_data['lowest_yield'] = data.get('sortRate', '')
        final_data['highest_yield'] = data.get('sortRate', '')
        final_data['sales_target'] = ''
        final_data['product_name'] = data.get('prdName')
        final_data['sales_target'] = ''
        final_data['url'] = ''
        final_data['file_content'] = data.get('file_content', '')
        final_data['sales_start_date'] = data.get('startDate', '')
        final_data['sales_end_date'] = data.get('realEndDate', '')
        final_data['product_type'] = data.get('prdTypeName')
        final_data['product_term'] = data.get('limit', {}).get('limit_data', '')
        final_data['product_nature'] = ''
        final_data['next_open_date'] = data.get('prdNextDate', '')
        final_data['next_two_open_date'] = data.get('nextEndDate', '')
        final_data['value_date'] = data.get('workDateList', '')
        final_data['min_purchase_amount'] = data.get('firstAmt', '')
        self.save_data(final_data)

    def save_data(self, data):
        print(json.dumps(data, ensure_ascii=False))

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