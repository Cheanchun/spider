# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import json

import requests

URL = 'https://m1.cmbc.com.cn/gw/m_app/QryProdListOnMarket.do'
post_data = {"request": {
    "body": {"pageSize": 10, "pageNo": 1, "orderFlag": "6", "prdChara": "4", "currentIndex": 0, "prdTypeNameList": [],
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
print(requests.post(URL, data=json.dumps(post_data, ensure_ascii=False), verify=False, headers=HEADERS).text)
