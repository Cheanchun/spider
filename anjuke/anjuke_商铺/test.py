# encoding: utf-8
import time

import redis
import requests
from selenium import webdriver

PROXY = "http://115.210.29.141:4230"
options = webdriver.ChromeOptions()
# desired_capabilities = options.to_capabilities()
# desired_capabilities['acceptSslCerts'] = True
# desired_capabilities['acceptInsecureCerts'] = True
# options.add_argument("window-size=1024,768")
# desired_capabilities['proxy'] = {
#     "httpProxy": PROXY,
#     "ftpProxy": PROXY,
#     "sslProxy": PROXY,
#     "noProxy": None,
#     "proxyType": "MANUAL",
#     "class": "org.openqa.selenium.Proxy",
#     "autodetect": False,
# }
REDIS_KEY = 'anjuke_SP_url'
r = redis.StrictRedis(host='127.0.0.1', port=6388, password="admin")
res = requests.get(
    "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=&city=0&yys=0&port=1&pack=28170&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=").text
print res
proxy = {'http': 'http://47.105.111.198:4111'}
print proxy
options.add_argument(u"--headless")
options.add_argument(
    u"--user-agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)")
options.add_argument(u'--disable-gpu')
options.add_argument(u'--no-sandbox')
options.add_argument(u"--proxy-server={}".format(proxy.get("http")))
chrome = webdriver.Chrome(chrome_options=options)
cnt = 0
url = r.spop(REDIS_KEY)
while True:
    cnt += 1
    chrome.get(url)
    # chrome.get("http://httpbin.org/get")
    print chrome.page_source
    print "---------------------{}-----------------".format(cnt)
    time.sleep(5)
    if u"请输入验证码" in chrome.page_source:
        break
# cookie = ""
# for k, v in {cookie.get(u"name"): cookie.get(u"value") for cookie in chrome.get_cookies()}.items():
#     cookie += k
#     cookie += "={};".format(v)
# print cookie
# time.sleep(3)
# chrome.quit()
