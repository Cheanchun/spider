# coding=utf-8

import fake_useragent
import requests


def get_proxy():
    resp = requests.get(
        "http://http.tiqu.alicdns.com/getip3?num=1&type=1&pro=&city=0&yys=0&port=1&pack=58416&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=").text.strip()
    print resp
    return resp


ua = fake_useragent.UserAgent()
proxy = {"https": "https://{}".format(get_proxy())}
headers = {
    "User-Agent": ua.random
}
resp = requests.get(url="https://cd.sydc.anjuke.com/sp-zu/?from=navigation", headers=headers, proxies=proxy)
# resp = requests.get(url="https://cd.sydc.anjuke.com/sp-zu/?from=navigation", headers=headers)
print resp.text
if u"请输入验证码" in resp.text:
    print "-----ban------"
