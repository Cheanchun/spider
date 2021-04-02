# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import json
import time

import redis
from lxml import etree

from common_tools.chrome_handle import ChromeHandle

sites = [
    "https://dc.simuwang.com/product/HF00005V8X.html?cid=CO0000029C",
    "https://dc.simuwang.com/product/HF0000122L.html?cid=CO000003IH",
    "https://dc.simuwang.com/product/HF00004XUU.html",
    "https://dc.simuwang.com/product/HF00003HHM.html",
    "https://dc.simuwang.com/product/HF00002EZG.html?cid=CO00000HZI",
    "https://dc.simuwang.com/product/HF00005VB1.html",
    "https://dc.simuwang.com/product/HF00005KIM.html",
    "https://dc.simuwang.com/product/HF000060GV.html?cid=CO0000029C",
    "https://dc.simuwang.com/product/HF00001DIK.html",
    "https://dc.simuwang.com/product/HF00005OQ3.html",
    "https://dc.simuwang.com/product/HF00005DNX.html",
    "https://dc.simuwang.com/product/HF00001GW7.html?cid=CO000008MM",
    "https://dc.simuwang.com/product/HF00005VHV.html",
    "https://dc.simuwang.com/product/HF00005GL2.html?cid=CO000001N7",
    "https://dc.simuwang.com/product/HF00004X9M.html?cId=",
    "https://dc.simuwang.com/product/HF00004OEZ.html",
    "https://dc.simuwang.com/product/HF00005205.html",
    "https://dc.simuwang.com/product/HF00003LPV.html",
    "https://dc.simuwang.com/product/HF00003YU0.html",
    "https://dc.simuwang.com/product/HF00005DP0.html",
    "https://dc.simuwang.com/product/HF00005G7J.html?cid=CO00000DOE",
    "https://dc.simuwang.com/product/HF00001BST.html",
    "https://dc.simuwang.com/product/HF00003HHR.html",
    "https://dc.simuwang.com/product/HF00002D45.html",
    "https://dc.simuwang.com/product/HF000069RI.html?cid=CO000000S4",
    "https://dc.simuwang.com/product/HF000010XY.html?cid=CO000001HJ",
    "https://dc.simuwang.com/product/HF0000186X.html",
    "https://dc.simuwang.com/product/HF000045IC.html",
    "https://dc.simuwang.com/product/HF00004MHJ.html",
    "https://dc.simuwang.com/product/HF00001D50.html",
    "https://dc.simuwang.com/product/HF00004AEM.html",
    "https://dc.simuwang.com/product/HF000052K1.html",
    "https://dc.simuwang.com/product/HF00002G7U.html",
    "https://dc.simuwang.com/product/HF000017G4.html",
    "https://dc.simuwang.com/product/HF00003YYL.html",
    "https://dc.simuwang.com/product/HF00004OCX.html?cId=",
    "https://dc.simuwang.com/product/HF00004C06.html",
    "https://dc.simuwang.com/product/HF000025N7.html",
    "https://dc.simuwang.com/product/HF00002K18.html?cid=CO000000GN",
    "https://dc.simuwang.com/product/HF00005C1Y.html",
    "https://dc.simuwang.com/product/HF00001GYF.html",
    "https://dc.simuwang.com/product/HF000045FB.html",
    "https://dc.simuwang.com/product/HF00001GPG.html",
    "https://dc.simuwang.com/product/HF00005CG8.html",
    "https://dc.simuwang.com/product/HF00003MH1.html",
    "https://dc.simuwang.com/product/HF00004J0A.html",
    "https://dc.simuwang.com/product/HF00006EV1.html",
    "https://dc.simuwang.com/product/HF000058E2.html",
    "https://dc.simuwang.com/product/HF00006CAE.html",
    "https://dc.simuwang.com/product/HF00005LLF.html?cId=",
    "https://dc.simuwang.com/product/HF000060V0.html",
    "https://dc.simuwang.com/product/HF0000586H.html",
    "https://dc.simuwang.com/product/HF00003XZS.html?cid=CO00000JE2",
    "https://dc.simuwang.com/product/HF00005QZ0.html",
    "https://dc.simuwang.com/product/HF00005PGQ.html?cid=CO00000178",
    "https://dc.simuwang.com/product/HF000051XT.html",
    "https://dc.simuwang.com/product/HF00002HED.html",
    "https://dc.simuwang.com/product/HF00003Y04.html",
    "https://dc.simuwang.com/product/HF00004C4X.html",
    "https://dc.simuwang.com/product/HF00002FDW.html",
    "https://dc.simuwang.com/product/HF00001NQS.html",
    "https://dc.simuwang.com/product/HF00001CFO.html?cid=CO000009RM",
    "https://dc.simuwang.com/product/HF00004GCH.html",
]
user_redis = redis.Redis(host='47.105.54.129', port=6388, password='admin')
cookie = [{'name': 'Hm_lvt_c3f6328a1a952e922e996c667234cdae', 'value': '1617098359,1617261604'},
          {'name': 'need_update_password', 'value': '1'}, {'name': 'smppw_tz_auth', 'value': '1'},
          {'name': 'http_tK_cache', 'value': 'a71ab2beb738b91c113ee3491c0de05f9881b79b'},
          {'name': 'cur_ck_time', 'value': '1617262764'},
          {'name': 'ck_request_key', 'value': 'jHhggNiAN2cq85XLsVHeRSHXSmFYf2Q5qjxeN69aBBY%3D'}, {'name': 'passport',
                                                                                                  'value': '1033896%09u3960723742121%09BQUFBQwAAQldUwQBWlBWDFJcAQEGCgkJAFZeXgYHAVY%3D9710d4c4e7'},
          {'name': 'certification', 'value': '1'}, {'name': 'qualified_investor', 'value': '1'},
          {'name': 'evaluation_result', 'value': '2'}, {'name': 'focus-certification-pop', 'value': '-1'},
          {'name': 'sensorsdata2015jssdkcross',
           'value': '%7B%22distinct_id%22%3A%221033896%22%2C%22first_id%22%3A%221033896%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221788292c1ad34e-018aa92c391987-5c173a1b-1049088-1788292c1ae527%22%7D'},
          {'name': 'Hm_lpvt_c3f6328a1a952e922e996c667234cdae', 'value': '1617277407'}]

chrome = ChromeHandle()
chrome.get_page(sites[0])
chrome.delete_cookies()
for item in cookie:
    new = dict(item, **{
        "domain": ".simuwang.com",
        "expires": "",
        'path': '/',
        'httpOnly': False,
        'HostOnly': False,
        'Secure': False,
    })
    chrome.add_cookie(new)
    sites.reverse()
for url in sites:
    time.sleep(10)
    print(url)
    p_code = url.rsplit('/')[-1].split('.')[0]
    page = chrome.get_page(url, page_source=True, waiting={'id': 'ENCODE_STYLE'})
    html = etree.HTML(page)
    css = ''.join(html.xpath('//div[@id="ENCODE_STYLE"]/style/text()'))
    items = css.strip('.').split('.')
    final_css = {}
    for item in items:
        code, style = item.split('{')
        if 'font' in style:
            final_css[code] = 0
        else:
            final_css[code] = 1
    user_redis.set(p_code, json.dumps(final_css, ensure_ascii=False))
