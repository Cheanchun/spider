import json
from urllib import quote

import requests
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pacs1_v1_5
from Crypto.PublicKey import RSA
from lxml import etree

key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCbJ2QYNdiFlzE0mcyq7tcZc5dPvof6696l2cJJM8kOxeXT8EonfvLzfsEGmwjNp3gvAyF14LvqT6w7oH40sFFnX358Eb+HZXx6CZ4LOkaTW0KNS6yodsRv0uwJhFMwREqEVbqd6jcCxTGKDOieendC8x1fsg3Muagyfawc+o+tewIDAQAB
-----END PUBLIC KEY-----
"""


def _rsa_encrypt(pwd):
    rsakey = RSA.import_key(key)
    cipher = Cipher_pacs1_v1_5.new(rsakey)
    res = cipher.encrypt(pwd)
    print res
    cipher_next = res
    return quote(cipher_next).replace('+', '%2B').replace('&', '%26').replace('/', '%2F')


url = 'https://ln.zhiyuanyun.com/app/user/login.php?m=login'
index_url = 'https://ln.zhiyuanyun.com/app/user/login.php'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
}
session = requests.Session()
session.headers.update(headers)
resp = session.get(index_url)
html = etree.HTML(resp.text)
seid = html.xpath('//input[@id="seid"]/@value')[0]
data = {
    'seid': seid,
    'uname': 'fushunwmb',
    'upass': 'Sdoqpt7TbbI8yvMsPCi44J4IVe2BxxsQMpVTh2+ozkWg0xvgoSkix6chErTH+ot6MG1E6TT9DjfeOfzKw4lQGuVizWddXbOaTpyuPmcBDJ0TuFb1/7U7zjMlSX8Slx0q4CM9I8n+bcTTQizkkoB4nyuI5FTIQCFfbWTYwrrCvP4=',
    'referer': 'https://ln.zhiyuanyun.com/app/user/home.php',
}
token = html.xpath('//meta[@name="csrf-token"]/@content')[0]
# session.headers.update(
#     {'x-csrf-token': token, 'x-requested-with': 'XMLHttpRequest', 'origin': 'https://ln.zhiyuanyun.com',
#      'Content-Type': 'application/x-www-form-urlencoded'})
print data
re = session.post(url, data=data)
print json.dumps(re.json(),ensure_ascii=False,encoding='u8')
