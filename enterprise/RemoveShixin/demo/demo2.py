# -*- coding: utf-8 -*-
'''
@Date       :2018/12/28
@Author     :
@Software   :Pycharm
'''
import time

import requests
# from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By  # 选择方法
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待


class KuHang:
    def __init__(self):
        self.session = requests.Session()
        self.browser = None
        self.url = "https://makeabooking.flyscoot.com/"
        self.ip_list = []
        self.cookies = {}
        self.proxy = self.get_ip()
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "referer": "https://www.flyscoot.com/zh",
            "origin": "https://www.flyscoot.com",
        }

    def get_cookies(self):
        '''
        使用selenium 动态获取cookie中__jsluid 和 __jsl_clearance 的值
        '''
        print('[*] 1. 第一次访问或者cookies失效，状态码为521，正在通过selenium获取...')
        self.cookies = {}
        options = webdriver.ChromeOptions()
        print(self.proxy)
        options.add_argument(f"--proxy-server=http://{self.proxy}")  # 设置浏览器代理
        # options.add_argument('--disable-gpu')
        # options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(chrome_options=options)
        browser.get(self.url)
        wait_gonggao_page = WebDriverWait(browser, 20)
        for i in range(3):
            try:
                flag = wait_gonggao_page.until(
                    EC.text_to_be_present_in_element((By.XPATH,
                                                      "//form[@class='form-booking form-booking__return']//a[@class='link__promo-code hidden-xs']"),
                                                     'Use promo code'))
            except:
                flag = None
            if flag:
                break
        time.sleep(2)
        self.cookies = {cookie.get("name"): cookie.get("value") for cookie in browser.get_cookies()}
        browser.close()
        print("cookies", self.cookies)
        return self.cookies

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
        # self.options.add_argument('--disable-gpu')
        # self.options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=self.options)
        # self.browser.maximize_window()


def main():
    kh = KuHang()

    post_data = {
        "revAvailabilitySearch.SearchInfo.AdultCount": 1,
        "revAvailabilitySearch.SearchInfo.ChildrenCount": 0,
        "revAvailabilitySearch.SearchInfo.InfantCount": 0,
        "revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureStationCode": "CAN",
        "revAvailabilitySearch.SearchInfo.SearchStations[0].ArrivalStationCode": "SIN",
        "revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureDate": "02/01/2019"
    }

    cookies = {

    }
    print(kh.proxy)
    session = requests.session()
    session.proxies = kh.proxy
    resp = session.post(url="https://makeabooking.flyscoot.com/Book/?culture=zh-cn", cookies=kh.get_cookies(),
                        data=post_data,
                        headers=kh.headers)
    print(resp.text)


# main()
print("".split())
