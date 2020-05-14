# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import json
import random
import re
import time
import traceback

import requests
import yaml

from bank.utils.utils import CommSession, content2tree

yaml_file = './config.yaml'


def get_yaml_data(yaml_file):
    print("***获取yaml文件数据***")
    with open(yaml_file, 'r', encoding="utf-8") as file:
        file_data = file.read()
        data = yaml.load(file_data, Loader=yaml.Loader)
    return data


CONFIG = get_yaml_data(yaml_file=yaml_file)
PARAM = CONFIG.get('param')
INDEX = 'https://mobile.cmbchina.com/IEntrustFinance/FinanceProduct/FP_AjaxQueryList.aspx'
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "mobile.cmbchina.com",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
}
HEADERS_DETAIL = {
    "Host": "mobile.cmbchina.com",
    "DeviceType": "D",
    "PBClient": "cmbpb-iphone",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-cn",
    "ClientVersion": "8.2.0",
    "Accept-Encoding": "br, gzip, deflate",
    "SID": "o2kb/HIYJK5+4GlwPT+cMIbsEes=",
    "Origin": "null",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MPBank/8.2.0 iPhone/12.2 Scale/3.0 AID/kwKtuBYeYza5fbSMBj3L1sFhjPc= SID/o2kb/HIYJK5+4GlwPT+cMIbsEes= WebView/WKWebView APPTag/1.0(N;44;321)",
    "Content-Length": "240",
    "Connection": "keep-alive",
    "SystemVersion": "12.2",
    "Content-Type": "application/x-www-form-urlencoded",
    "AID": "kwKtuBYeYza5fbSMBj3L1sFhjPc=",
    "Cookie": "pgv_pvi=4890748928",
}
FILE_URL = 'https://mobile.cmbchina.com/IEntrustFinance/FinanceProduct/FP_PrdInstruction.aspx?version=8.2.0'
RATE_URL = 'https://mobile.cmbchina.com/IEntrustFinance/FinanceProduct/FP_AjaxQueryRate.aspx'


class CMBChinaApp(object):
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
        if _headers:
            self.session.headers = _headers
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

    def test(self, code=None, page_no=1):
        if code:
            PARAM['lastRipCod'] = code
            PARAM['ListNo'] = page_no
            PARAM['TimTmp'] = str(time.time() * 1000)
        data_json = self._get(INDEX, data=PARAM, ).json()
        data_list = data_json.get('$SysResult$').get('$Content$').get('DataSource').get('PrdList')
        last_code = data_list[-1].get('RipCod') if data_list else ""
        for data in data_list:
            self.get_rate_data(data.get('RipCod'), data=data)
            self.production_introduce(data.get('RipCod'), data)
            print(json.dumps(data, ensure_ascii=False))
        return last_code

    def get_rate_data(self, ripcode: str, data: json):
        time.sleep(1)
        post_data = CONFIG.get('rate_post_data')
        post_data['RipCod'] = ripcode
        resp = self._get(url=RATE_URL, data=post_data, method='post')
        rate_data = resp.json().get('$SysResult$').get('$Content$').get('RatData')
        data['RatData'] = rate_data

    def production_introduce(self, code, data):
        """

        :return:
        """

        post_data = CONFIG.get('book_post_data')
        post_data['Code'] = code
        resp = self._get(url=FILE_URL, _headers=headers_detail, data=post_data,method='post')
        html = content2tree(resp.text)
        pdf_url = html.xpath('string(//div[@id="ctl00_cphBody_info_PDF"]/@onclick)')
        res = re.search(r'(http.+[doc|pdf|docx])\'', pdf_url)
        if res:
            data['file_url'] = res.group(1)
        else:
            pass
        # print(resp.text)

    def main(self):
        code = 1
        page = 1
        while code:
            code = self.test(code=code, page_no=page)
            page += 1


if __name__ == '__main__':
    c = CMBChinaApp()
    c.main()
