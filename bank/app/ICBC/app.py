# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import json

import requests

URL = 'https://mywap2.icbc.com.cn/ICBCWAPBank/servlet/WapAPIReqServlet'
index_url = 'https://www.icbc.com.cn/icbc/'
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
post_data = {
    "fCode": "clientNew_FinancePurchaseNoSessionOp",
    "pageMark": "25",  # 重点参数"
    "pageNumber": "4",  # 翻页开始 超过25 返回空json"
    "toPage": "5",  # 翻页截止 "
    "sortTypetemp": "",
    "orderTypetemp": "",
    "filterTypetemp": "TJ",
    "searchKey": "",
    "searchCurrKey": "0",
    "searchTermKey": "0",
    "searchProTypeKey": "0",
    "searchProRiskGradeKey": "0",
    "searchProProfitTypeKey": "4",
    "currentAreaCode": "4402",
    "dssFlag": "1",
    "nosData": "",
    "predicted_page": "/ICBCWAPBank/ebdpui/dss/aperson/mainpage/clientNew_finance_purchase_list_noSession_new.html",
    "entryFlag": "0",

}


def api_app():
    with open('icbc.txt', mode='a+', encoding='u8') as fp:
        for page in range(1, 25):
            post_data['pageNumber'] = str(page)
            post_data['toPage'] = str(page + 1)
            content = requests.post(URL, data=post_data, headers=HEADERS, verify=False).text
            content = content.strip().replace('\'', '"')
            content = json.loads(content, encoding='u8')
            for data in content.get('opdata').get('jsonData'):
                get_production_introduce(data)
                content = json.dumps(data, ensure_ascii=False)
                fp.write(content + '\n')
                print(content)


def get_production_introduce(data):
    p_id = data.get('productId')
    if p_id:
        data['file_url'] = 'https://image.mybank.icbc.com.cn/picture/Perfinancingproduct/{}.pdf'.format(p_id)
    else:
        data['file_url'] = ''


if __name__ == '__main__':
    api_app()
