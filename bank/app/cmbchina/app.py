# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import json
import time

from bank.utils.utils import CommSession

headers = {
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
index = 'https://mobile.cmbchina.com/IEntrustFinance/FinanceProduct/FP_AjaxQueryList.aspx'
param = {
    "Command": "CMD_DOQUERYLISTNEW",
    "ClientNo": "85c0194367894be194bde35da6928535",
    "ListNo": "1",
    "ListNo_B": "1",
    "ListNo_C": "1",
    "ListNo_D": "1",
    "PrdTerm": "0",
    "PrdPurch": "0",
    "BobFlg": "A",
    "CcyNbr": "",
    "CltCtl": "0",
    "OdrTyp": "D",
    "OdrFld": "B",
    "AgtCtm": "N",
    "PrdTyp": "All",
    "UserInfo": "yJdnBnfi0u1MWCG7zOufUUggbW6LZTFTshIEdju2h%2Bv1VilIm68X8u5iftNLnnjHuA3TjEZ1yiU%2B%2Bo0oJ1pzIekDqM%2FhKnkAVA%2FQ6azV30gLv0xhKyJM9Za9A7XRL%2FAztmbrdjLlP0va7PSgeE6c0KJApuafsPWsjvB1X7xzz%2FwwP2FN6hi4col9yVmHTgXQh%2FFATqVsGOXNzoB9%2BbFvqZNxLqIr66q2uN8Qp%2FmMTCE6FPiZY07j%2BC%2BSTTCUpturVxOBcJd4ySfEts4b2PhV5nsSBhfXbZHzrMqJqFEmV9bw%2FEJRN4k90P3LG45gXmOBJcv%2FiCJmdrvv1TsBUc3uZFxjqNToQT8TiH4td9CisAEz3jG%2FzBm237%2FKXyTOfrfaiRjD0JcCRVxvaFRGv%2FoLqhNc5SSG%2BmNDUNuWImLYSGhbjaqfpkTM9yFgN%2BRX0o3kF5xs7UZBc0WX%2F9X%2BjtKFYTyR2bqXJ4haoEQ7C3Tr64b2spvjNi1TlD1riHMd62f%2B5Eg3f3Ri9Gz79lgQEk6T65M6PG5AXX2oyqVBUteFpTK7OkqOWgZntKQYayxpwnlTLjNux8C2GhEtndSCXr%2FxnuRiiq69o1p51YYq7A9Mpzc%3D",
    "RgnDsc": "B",
    "TimTmp": str(time.time() * 1000),
    "lastRipCod": "",
    "%24RequestMode%24": "",
}


def test(code=None, page_no=1):
    time.sleep(3)
    if code:
        param['lastRipCod'] = code
        param['ListNo'] = page_no
        param['TimTmp'] = str(time.time() * 1000)
    print(headers)
    a = CommSession(verify=False, headers=headers)
    session = a.session()
    data_json = session.get(index, params=param, ).json()
    # last_rip_code = data_json.get('$SysResult$').get('$Content$').get('DataSource').get('lastRipCod')
    # print('last_rip_code:{}'.format(last_rip_code))
    data_list = data_json.get('$SysResult$').get('$Content$').get('DataSource').get('PrdList')
    last_code = data_list[-1].get('RipCod') if data_list else ""
    for data in data_list:
        fp.write(json.dumps(data, ensure_ascii=False) + '\n')
        print(f'data save finish:{data}')
    return last_code


def get_data():
    code = 1
    page = 1
    while code:
        code = test(code=code, page_no=page)
        page += 1


if __name__ == '__main__':
    with open('./demo.txt', mode='a+', encoding='u8') as fp:
        get_data()
    #     with open('./zhaoshang.txt', mode='a+', encoding='u8') as wp:
    #         content = fp.readline()
    #         while content:
    #             data = json.loads(content, encoding='u8')
    #             data_list = data.get('$SysResult$').get('$Content$').get('DataSource').get('PrdList')
    #             for i in data_list:
    #                 wp.write(json.dumps(i, ensure_ascii=False) + '\n')
    #                 print(i)
    #             content = fp.readline()
