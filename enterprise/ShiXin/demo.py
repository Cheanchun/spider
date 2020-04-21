# encoding: utf-8

# encoding: utf-8
import json
import re
import time

import execjs
import redis
import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By  # 选择方法
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待

from helper.config import BaseConfig  # 相关配置


def exec_js2(resp):
    js = "function dd(){var json=" + resp + ";return json.map( function(item){ return String." \
                                            "fromCharCode(item);}).join('');}"
    ctx = execjs.compile(js)
    return ctx.call("dd")


class test(BaseConfig):

    def __init__(self):
        self.ip_list = []
        self.session = requests.Session()
        self.browser = None
        self.r = redis.Redis(host=self.HOST, port=self.PORT, db=self.DB_INDEX, password=self.PASSWORD)
        self.info_base_url = "http://www.gsxt.gov.cn"
        self.brief_msg = None
        self.keyword = None
        self.headers = None
        self.success = None
        self.gt = None
        self.challenge = None
        self.validate = None
        self.info_url = None
        self.query_page = "http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html"
        self.cookies = {}
        self.headers = {
            'Host': 'www.gsxt.gov.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/'
                          '537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36',
            'Refer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Referer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Origin': 'http://www.gsxt.gov.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
        }

    def get_ip(self):
        ip_url = "http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy?spiderId=bcf4b1d29b374d10a6a1d14fd08e516f&returnType=1&count=1"
        if self.ip_list:
            return self.ip_list.pop()
        else:
            self.ip_list = requests.get(url=ip_url).text.split()
            print(self.ip_list)
            return self.ip_list.pop()

    def open_chrome(self):
        self.options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(chrome_options=self.options)
        self.browser.maximize_window()

    # 获取cookies
    def get_cookies(self):
        '''
        使用selenium 动态获取cookie中__jsluid 和 __jsl_clearance 的值,目标
        网站主要验证cookies中这两个字段信息,__jsl_clearance js代码动态生成
        '''

        print('[*] 1. 第一次访问或者cookies失效，状态码为521，正在通过selenium获取...')
        self.browser.get(self.query_page)
        wait_gonggao_page = WebDriverWait(self.browser, 10)
        for i in range(3):  # 出现知道创宇监测页面和ip监测页面
            flag = False
            try:
                flag = wait_gonggao_page.until(
                    EC.text_to_be_present_in_element((By.XPATH, "//div[@class='page_left']/a[5]/div[@id='tab4']"),
                                                     '严重违法失信企业名单公告'))
            except TimeoutException:
                self.change_proxy()
                self.browser.get(self.query_page)

            if flag:
                break
        self.cookies = {cookie.get("name"): cookie.get("value") for cookie in self.browser.get_cookies()}
        print(self.cookies)

    def change_proxy(self):
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
        self.session.proxies = {"http": proxy},  # 设置 session 静态请求代理

    # 获取验证码信息
    def get_image_gif(self):
        url = f'http://www.gsxt.gov.cn/SearchItemCaptcha?t={time.time()*1000}'
        resj = self.session.get(url, headers=self.headers, cookies=self.cookies)
        for_test_error = resj.text  # 用于错误捕获打印
        try:
            resj = resj.json()
            url = "http://www.gsxt.gov.cn/corp-query-custom-geetest-image.gif?v="
            local_time = time.localtime(time.time())
            url = url + str(local_time.tm_min + local_time.tm_sec)
            resp = self.session.get(url, headers=self.headers, cookies=self.cookies)
            self.success = resj['success']
            self.gt = resj['gt']
            self.challenge = resj['challenge']
            try:
                aaa = exec_js2(resp.text)
                matchObj = re.search('location_info = (\d+);', aaa)
            except execjs._external_runtime.ProcessExitedWithNonZeroStatus:
                print("重新执行get_image_gif()")
                self.get_image_gif()
            if matchObj:
                return matchObj.group(1)
            else:
                raise RuntimeError("RuntimeError:没有找到location_info")
        except json.JSONDecodeError as e:
            print("[!]image_gif获取失败,重新获取")
            print(e)
            print(for_test_error)
            self.get_image_gif()

    # 获取token
    def get_token(self):
        url = "http://www.gsxt.gov.cn/corp-query-geetest-validate-input.html?token=" + self.get_image_gif()
        resp = self.session.get(url, headers=self.headers, cookies=self.cookies)
        aaa = exec_js2(resp.text)
        matchObj = re.search('value: (\d+)}', aaa)
        if matchObj:
            location_info = matchObj.group(1)
            self.token = str(int(location_info) ^ 536870911)
            print('[*] 3. 获取token: ' + self.token)
        else:
            raise RuntimeError("RuntimeError:没有找到location_info")

    # 调用JiYan 打码平台进行验证码验证
    def get_validate(self):
        url = f'http://jiyanapi.c2567.com/shibie?gt={self.gt}&challenge={self.challenge}&referer=http://www.gsxt.gov.cn&user={self.USER}&pass={self.PASSWD}&return=json&format=utf8'
        if not self.success:
            url = url + '&model=1'
        res = self.session.get(url=url).text
        resj = json.loads(res)
        if resj['status'] == 'ok':
            print('[*] 4. 对接极验打码平台，获取validate成功')
            print(resj)
            self.validate = resj['validate']
        else:
            raise RuntimeError("RuntimeError:打码平台", resj['msg'])


def main():
    fotest = test()
    fotest.open_chrome()
    fotest.change_proxy()
    fotest.get_cookies()
    fotest.get_token()
    fotest.get_validate()


if __name__ == '__main__':
    main()
