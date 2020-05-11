# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import json
import time

import requests

URL = 'https://m1.cmbc.com.cn/gw/m_app/QryProdListOnMarket.do'
post_data = {"request": {
    "body": {"pageSize": 20, "pageNo": 1, "orderFlag": "6", "prdChara": "4", "currentIndex": 0, "prdTypeNameList": [],
             "pfirstAmtList": [], "currTypeList": [], "fundModeList": []},
    "header": {"reqSeq": "0", "appExt": "1", "feature": "", "net": {"ip": "192.168.2.174"}, "appId": "1",
               "custType": "100", "signedMicroFlag": "0", "cityCode": "1101", "ffVersion": "4.0", "transId": "",
               "appVersion": "5.3", "device": {"osType": "01", "osVersion": "12.2", "model": "iPhone",
                                               "uuid": "EF67D148-4F0C-4782-9558-F75911131A27", "isBreakOut": "0",
                                               "deviceID": "EF67D148-4F0C-4782-9558-F75911131A27", "brand": "iPhone",
                                               "deviceModel": "iPhone10,3"}}}}
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


def live_api(post_data):
    json_data = requests.post(URL, data=json.dumps(post_data, ensure_ascii=False), verify=False, headers=HEADERS).json()
    pr_list = json_data.get('response').get('prdList')
    for data in pr_list:
        get_detail_data(data.get('prdCode'), data)
        get_product_introduce(data.get('prdCode'), data)
        print(data)
        fp.write(json.dumps(data, ensure_ascii=False) + '\n')


def get_detail_data(prdCode, data):
    time.sleep(3)
    url = 'https://m1.cmbc.com.cn/gw/m_app/QueryPrdBuyInfo.do'
    post_data = {
        "request": {
            "body": {
                "prdCode": prdCode,
                "getVipFlag": "1",
                "GroupFlag": "1"
            },
            "header": {
                "reqSeq": "0",
                "appExt": "1",
                "feature": "",
                "net": {"ip": "192.168.43.3"},
                "appId": "1",
                "custType": "100",
                "signedMicroFlag": "0",
                "cityCode": "1101",
                "ffVersion": "4.0",
                "transId": "",
                "appVersion": "5.3",
                "device": {
                    "osType": "01",
                    "osVersion": "12.2",
                    "model": "iPhone",
                    "uuid": "EF67D148-4F0C-4782-9558-F75911131A27",
                    "isBreakOut": "0",
                    "deviceID": "EF67D148-4F0C-4782-9558-F75911131A27",
                    "brand": "iPhone",
                    "deviceModel": "iPhone10,3"
                }
            }
        }
    }
    resp = requests.post(url, data=json.dumps(post_data, ensure_ascii=False), headers=HEADERS, verify=False).json()
    data['detail_info'] = resp.get('response')


def get_product_introduce(prdCode, data):
    url = 'https://m1.cmbc.com.cn/gw/m_app/QryProductProtocol.do'
    headers = {
        "Host": "m1.cmbc.com.cn",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://m1.cmbc.com.cn",
        "Cookie": "org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; BIGipServerUEB_tongyidianziqudao_app_41002_pool=!pzlp04WN08XQUJuu7VmpjXDjWZnrfsHT6noSOT4MiS7okemUJ0NFYcaUjXuXK8ZlSCNd+E12ANrS2Q==; RSESSIONID=3F6DE20DB0F4455EADADFE6B397B99E3; BIGipServershoujiyinhang_geren_app_8000_pool=!4WXPwHw2CH5PXKeu7VmpjXDjWZnrfie+poqHKYgZiyxm/BKsZTvc1geOY+/e649MwKmd9eum+QlHWeQ=; JSESSIONID=1ToDDzt2M8B8tn80ONG-higzJGRDMdDoAu3NIMDlPnh0YEbc-sUu!144497199; bigipW_http_m1_cookie=!X9Hwj3yWQlTfBsVUCAg1OdjEE0PQjUQpedOhxMNBH4/oaYXCgbXYqt25crhPd2dk2qxHrh8AeaxggNk=",
        "Content-Length": "177",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/requestByNative/cmbc.geren.5.3/UIMode=0",
        "Referer": "https://m1.cmbc.com.cn/CMBC_MBServer/new/app/mobile-bank/finance/reading?prdCode=FSAF19189A&type=3",
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "br, gzip, deflate",
    }
    post_data = {
        "request": {
            "header": {
                "appId": "",
                "appVersion": "5.3",
                "appExt": "1",
                "device": {
                    "appExt": "1",
                    "osType": "01",
                    "osVersion": "",
                    "uuid": ""
                }
            },
            "body": {
                "prdCode": prdCode,
                "infoType": "3"
            }
        }
    }
    introductione_content = requests.post(url, data=json.dumps(post_data, ensure_ascii=False), headers=headers).json()
    data['file_content'] = introductione_content.get('response').get('content')


if __name__ == '__main__':
    with open('mingsheng{}.txt'.format(int(time.time())), mode='a+', encoding='u8') as fp:
        for page in range(1, 5):
            post_data['request']['body']['pageNo'] = page
            live_api(post_data)
