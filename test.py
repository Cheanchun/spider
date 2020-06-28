# import json
# from urllib import quote
#
# import requests
# from Crypto.Cipher import PKCS1_v1_5 as Cipher_pacs1_v1_5
# from Crypto.PublicKey import RSA
# from lxml import etree
#
# key = """-----BEGIN PUBLIC KEY-----
# MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCbJ2QYNdiFlzE0mcyq7tcZc5dPvof6696l2cJJM8kOxeXT8EonfvLzfsEGmwjNp3gvAyF14LvqT6w7oH40sFFnX358Eb+HZXx6CZ4LOkaTW0KNS6yodsRv0uwJhFMwREqEVbqd6jcCxTGKDOieendC8x1fsg3Muagyfawc+o+tewIDAQAB
# -----END PUBLIC KEY-----
# """
#
#
# def _rsa_encrypt(pwd):
#     rsakey = RSA.import_key(key)
#     cipher = Cipher_pacs1_v1_5.new(rsakey)
#     res = cipher.encrypt(pwd)
#     print res
#     cipher_next = res
#     return quote(cipher_next).replace('+', '%2B').replace('&', '%26').replace('/', '%2F')
#
#
# url = 'https://ln.zhiyuanyun.com/app/user/login.php?m=login'
# index_url = 'https://ln.zhiyuanyun.com/app/user/login.php'
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
# }
# session = requests.Session()
# session.headers.update(headers)
# resp = session.get(index_url)
# html = etree.HTML(resp.text)
# seid = html.xpath('//input[@id="seid"]/@value')[0]
# data = {
#     'seid': seid,
#     'uname': 'fushunwmb',
#     'upass': 'Sdoqpt7TbbI8yvMsPCi44J4IVe2BxxsQMpVTh2+ozkWg0xvgoSkix6chErTH+ot6MG1E6TT9DjfeOfzKw4lQGuVizWddXbOaTpyuPmcBDJ0TuFb1/7U7zjMlSX8Slx0q4CM9I8n+bcTTQizkkoB4nyuI5FTIQCFfbWTYwrrCvP4=',
#     'referer': 'https://ln.zhiyuanyun.com/app/user/home.php',
# }
# token = html.xpath('//meta[@name="csrf-token"]/@content')[0]
# # session.headers.update(
# #     {'x-csrf-token': token, 'x-requested-with': 'XMLHttpRequest', 'origin': 'https://ln.zhiyuanyun.com',
# #      'Content-Type': 'application/x-www-form-urlencoded'})
# print data
# re = session.post(url, data=data)
# print json.dumps(re.json(),ensure_ascii=False,encoding='u8')
import json

import requests


def zc_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
        # 'cookie': 'acw_tc=76b20ff415922769405186120e74fdda04dbb35c2124642f070dd5edaf054c; _zcy_log_client_uuid=bca23ab0-af7e-11ea-b093-c3aca5c27b8d; districtCode=439900; _dg_playback.bbc15f7dfd2de351.63bf=1; _dg_abtestInfo.bbc15f7dfd2de351.63bf=1; _dg_check.bbc15f7dfd2de351.63bf=-1; districtName=%E6%B9%96%E5%8D%97%E7%9C%81%E6%9C%AC%E7%BA%A7; _dg_id.bbc15f7dfd2de351.63bf=760fa7bcf0af7013%7C%7C%7C1592276949%7C%7C%7C0%7C%7C%7C1592277053%7C%7C%7C1592277052%7C%7C%7C%7C%7C%7C8f7e0cb5dfd0655b%7C%7C%7C%7C%7C%7C%7C%7C%7C1%7C%7C%7Cundefined'
    }
    tsp = time.time() * 1000
    res = requests.get(
        'https://hunan.zcygov.cn/supplier/open-api/baseinfo/list?timestamp={}&pageNo=1&pageSize=1&tenantCode=430000'.format(
            tsp), headers=headers).json()
    print res
    total = res.get('result').get('total')

    print total
    url = 'https://hunan.zcygov.cn/supplier/open-api/baseinfo/list?pageNo={}&pageSize=2000&tenantCode=430000'
    total_page = total // 2000 + 1
    with open('zc.txt', mode='a+') as fp:
        for page in range(1, total_page + 1):
            resp = requests.get(url.format(page), headers=headers).json()
            data_list = resp.get('result').get('data')
            for data in data_list:
                fp.write(json.dumps(data, encoding='u8', ensure_ascii=False).encode('u8') + '\n')


import time


class Dict(dict):

    def __init__(self, **kw):
        super(dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


v = Dict(a='1', b=3)
print v.a
