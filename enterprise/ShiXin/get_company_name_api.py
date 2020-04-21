# -*- coding: utf-8 -*-
'''
@Date       :2018/12/28
@Author     :
@Software   :Pycharm
'''
import random
import re
import time
import traceback

import redis
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By  # 选择方法
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待


from helper.config import BaseConfig


# 获取api数据
class ParseApi(BaseConfig):
    session = requests.Session()
    cookies = {}
    data_list = []

    def __init__(self):
        '''
        areaId 对照
        北京:110000 天津:120000(空) 河北:130000 山西:140000 内蒙古:150000
        辽宁:210000	吉林:210000 黑龙江:230000
        上海:310000 江苏:320000 浙江:330000 安徽:340000 福建:350000 江西:360000 山东:370000
        河南:410000 湖北:420000 湖南:430000 广东:440000 广西:450000 海南:460000 重庆:500000
        四川:510000	贵州:520000	云南:530000 西藏:540000
        陕西:610000 甘肃:620000 青海:630000 宁夏:640000 新疆:650000
        '''
        self.headers = {
            'Host': 'www.gsxt.gov.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36',
            #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.11',
            'Refer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Referer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Origin': 'http://www.gsxt.gov.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01'
        }
        self.r = redis.Redis(host=self.HOST, port=self.PORT, db=self.DB_INDEX, password=self.PASSWORD)

        if not self.r.llen("areaId"):
            areaIds = [110000, 130000, 140000, 150000, 210000, 220000, 230000, 310000, 320000, 330000,
                       340000, 350000, 350000, 360000, 370000, 410000, 420000, 430000, 440000, 450000, 460000,
                       500000, 510000, 520000, 530000, 540000, 610000, 620000, 630000, 640000, 650000]
            for areaId in areaIds:
                self.r.rpush("areaId", areaId)
        else:
            pass

    def get_cookies(self):
        '''
        使用selenium 动态获取cookie中__jsluid 和 __jsl_clearance 的值
        '''
        print('[*] 1. 第一次访问或者cookies失效，状态码为521，正在通过selenium获取...')
        self.cookies = {}
        option = webdriver.ChromeOptions()
        option.headless = True
        browser = webdriver.Chrome()
        browser.get("http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html")
        wait_gonggao_page = WebDriverWait(browser, 20)
        for i in range(3):
            try:
                flag = wait_gonggao_page.until(
                    EC.text_to_be_present_in_element((By.XPATH, "//div[@class='page_left']/a[5]/div[@id='tab4']"),
                                                     '严重违法失信企业名单公告'))
            except:
                flag = None
            if flag:
                break
        time.sleep(2)
        self.cookies = {cookie.get("name"): cookie.get("value") for cookie in browser.get_cookies()}
        browser.close()
        print("cookies", self.cookies)

    # 更换代理ip
    def change_proxy(self):
        self.session.proxies = random.choice(self.PROXIES)

        # 获得失信企业名单

    def get_api_data(self, cookies={}):
        if self.cookies:
            areaId = self.r.lpop("areaId")
            while areaId:
                post_data = {
                    "draw": 1,
                    "start": 0,
                    "length": 10,
                }
                self.data_list = []
                print("地区ID", areaId)
                url = f'http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html?noticeType=21&areaid=100000&noticeTitle=&regOrg={areaId.decode("utf-8")}'
                for i in range(1, 6):
                    print(post_data)
                    self.change_proxy()  # 请求一次切换ip
                    try:
                        company_json = requests.post(url=url, headers=self.headers, cookies=self.cookies,
                                                     data=post_data, )
                    except Exception as e:
                        self.session.proxies = random.choice(self.PROXIES)
                        company_json = requests.post(url=url, headers=self.headers, cookies=self.cookies,
                                                     data=post_data, )
                    try:
                        self.data_list.extend(company_json.json().get('data'))
                    except:
                        print("[!]非json数据返回")
                        traceback.format_exc()
                    if company_json.status_code == 521:
                        self.get_cookies()
                    time.sleep(random.randint(1, 2))
                    post_data['draw'] = post_data.get("draw") + 1
                    post_data['start'] = post_data.get("start") + 10
                if self.data_list:
                    self.parse_data()
                else:
                    print("[!]api数据列表为空")
                areaId = self.r.lpop("areaId")
            print("所有地区ID已经爬去完成")
        else:
            url = 'http://www.gsxt.gov.cn/SearchItemCaptcha?t=' + str(round(time.time() * 1000))
            index_page = self.session.get(url, headers=self.headers, cookies=cookies)
            if index_page.status_code == 521:
                self.get_cookies()
                self.get_api_data()
                self.get_api_data(self.cookies)

            elif re.search("有疑似非正常访问行为", str(index_page.text)):
                print("[!]目标网站监测出非正常访问,稍后再试!")

    def parse_data(self):
        for item in self.data_list:
            item[
                "notice_url"] = f'http://www.gsxt.gov.cn/affiche-query-info-inspect.html?noticeId={item.get("noticeId")}&datafrom=&provinceid=100000'
            self.save_to_redis_as_zset(item=item)

    def save_to_redis_as_zset(self, key="order_company", item=None):
        '''匹配数据中的注册号,可能位数 13 15 18 位,'''
        score = 0
        # res = re.search(pattern="([0-9A-Z]{18}[)）/])|([0-9A-Z]{13}[)）/])|([0-9A-Z]{15}[)）/])",
        #                 string=item.get("noticeContent"))
        res = re.search(pattern="([0-9A-Z]{18})[\)）/]|([0-9A-Z]{13})[\)）/]|([0-9A-Z]{15})[\)）/]",
                        string=item.get("noticeContent"))
        if res:
            reg_num = res.group()[:-1]
        else:
            reg_num = ""
            print("注册码获取失败", score)
        data = {k: v for k, v in item.items() if v != "" or v == "None"}
        data["reg_num"] = reg_num
        data = str(data)
        print(data)
        if not self.r.zrank(key, data):
            result = self.r.zadd(key, {data: score})
            print("写入结果", result)
        else:
            print("[!]元素已存在")


def main():
    parseapi = ParseApi()
    parseapi.get_api_data()


def unittest():
    pass


if __name__ == '__main__':
    main()
