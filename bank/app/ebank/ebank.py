# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import requests

URL = "https://wap.cebbank.com/pwap/MPFinanceRedirect.do"
post_data = {
    'trs': 'MP',
    'Channel': '0'
}
HEADERS = {
    "Host": "wap.cebbank.com",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://wap.cebbank.com",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "br, gzip, deflate",
    "Connection": "keep-alive",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.12(0x17000c2d) NetType/WIFI Language/zh_CN",
    "Referer": "https://wap.cebbank.com/personweixin/personstatic/",
    "Content-Length": "16",
    "X-Requested-With": "XMLHttpRequest",
}
# 与app比较 数据量不足
data_list = requests.post(url=URL, headers=HEADERS, data=post_data, verify=False).json()
for data in data_list.get('List'):
    print(data)
