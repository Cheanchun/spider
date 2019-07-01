# encoding: utf-8
# import redis
#
# r = redis.Redis(host='127.0.0.1', port=6379)
#
# for i in r.smembers('anjukeData'):
#     with open('./1.json', 'a+', encoding='utf-8') as w:
#         w.write(str(i.decode('utf-8')) + '\n')
import time

from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By  # 选择方法
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待

PROXY = "http://115.210.29.141:4230"
options = webdriver.ChromeOptions()
desired_capabilities = options.to_capabilities()
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
options.add_argument(u"--headless")
options.add_argument(
    u"--User-Agent=Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)")
options.add_argument(u'--disable-gpu')
options.add_argument(u'--no-sandbox')
chrome = webdriver.Chrome(chrome_options=options)
chrome.get(u"https://www.anjuke.com")
time.sleep(10)
print chrome.page_source
cookie = ""
for k, v in {cookie.get(u"name"): cookie.get(u"value") for cookie in chrome.get_cookies()}.items():
    cookie += k
    cookie += "={};".format(v)
print cookie
