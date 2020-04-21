import time

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 等待

headers = {
    'Host': 'www.gsxt.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36',
    'Refer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
    'Referer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
    'Origin': 'http://www.gsxt.gov.cn',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}
query_page = "http://www.gsxt.gov.cn/index.html"


class T:
    ip_list = []
    options = webdriver.ChromeOptions()
    session = requests.session()
    browser = webdriver.Chrome()

    def get_ip(self):
        ip_url = "http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy?spiderId=bcf4b1d29b374d10a6a1d14fd08e516f&returnType=1&count=1"
        if self.ip_list:
            return self.ip_list.pop()
        else:
            self.ip_list = requests.get(url=ip_url).text.split()
            print(self.ip_list)
            return self.ip_list.pop()

    def change_chrome_proxy(self):
        '''
        ip代理切换,requests和selenium需要更换相同的ip,否则静态请求会导致失败!
        :return:None
        '''
        proxy = self.get_ip()
        print(proxy)
        self.browser.quit()  # 退出当前浏览器
        self.options.add_argument(f"--proxy-server=http://{proxy}")  # 设置浏览器代理
        self.browser = webdriver.Chrome(chrome_options=self.options)
        self.browser.maximize_window()

    def change_requests_proxy(self):
        proxy = self.get_ip()
        print(proxy)
        self.session.proxies = {"http": proxy},  # 设置 session 静态请求代理

    def get_cookies(self):
        '''
        使用selenium 动态获取cookie中__jsluid 和 __jsl_clearance 的值,目标
        网站主要验证cookies中这两个字段信息,__jsl_clearance js代码动态生成
        '''

        print('[*] 1. 第一次访问或者cookies失效，状态码为521，正在通过selenium获取...')
        self.browser.get(query_page)
        wait_gonggao_page = WebDriverWait(self.browser, 10)
        cookies = {cookie.get("name"): cookie.get("value") for cookie in self.browser.get_cookies()}
        print(cookies)
        return cookies

    def request_page(self):
        resp = self.session.get(url=query_page, headers=headers, cookies=self.get_cookies())
        return resp


te = T()
# te.change_chrome_proxy()
te.change_requests_proxy()
while True:
    resp = te.request_page()
    print(resp.text)
    print(resp.status_code)
    time.sleep(1)
    if resp.status_code != 200:
        te.change_requests_proxy()
