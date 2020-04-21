# encoding: utf-8
import time

import random
import re
import redis
import requests
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By  # 选择方法
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待

from helper.config import BaseConfig


class Search(BaseConfig):
    def __init__(self):
        self.display = Display(visible=0, size=(1280, 800))  # 创建虚拟展示界面
        self.display.start()  # 开始
        self.session = requests.Session()
        self.browser = None
        self.info_base_url = "http://www.gsxt.gov.cn"
        self.brief_msg = None
        self.keyword = None
        self.headers = None
        self.success = None
        self.gt = None
        self.challenge = None
        self.validate = None
        self.info_url = None
        self.ip_list = []
        self.query_page = "http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html"
        self.cookies = {}
        self.r = redis.Redis(host=self.HOST, port=self.PORT, db=self.DB_INDEX, password=self.PASSWORD)
        self.headers = {
            'Host': 'www.gsxt.gov.cn',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36',
            'Refer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Referer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Origin': 'http://www.gsxt.gov.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
        }

    def open_chrome(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')
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
        wait_gonggao_page = WebDriverWait(self.browser, 20)
        for i in range(3):  # 出现知道创宇监测页面/和ip检测页面   --->time.sleep()减缓访问速度
            flag = False
            try:
                flag = wait_gonggao_page.until(
                    EC.text_to_be_present_in_element((By.XPATH, "//div[@class='page_left']/a[5]/div[@id='tab4']"),
                                                     '严重违法失信企业名单公告'))
            except TimeoutException:
                time.sleep(random.randint(2, 5))
                # self.change_chrome_proxy()
                self.browser.get(self.query_page)

            if flag:
                break
            elif i == 2:
                raise EOFError("[!]cookies 页面刷新失败!")
            else:
                pass
        self.cookies = {cookie.get("name"): cookie.get("value") for cookie in self.browser.get_cookies()}
        print(self.cookies)
        # print(self.browser.page_source)

    def get_data(self):
        with open("./rework/doing/3-3.txt", "r", encoding="utf-8") as fp:
            titles = fp.readlines()
        print(titles)
        for title in titles:
            print(title)
            url = f'http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html?noticeType=21&areaid=100000&noticeTitle={title.strip()}&regOrg='

            resp = self.session.post(url=url, data="", cookies=self.cookies, headers=self.headers,
                                     allow_redirects=False)
            while resp.status_code != 200:
                time.sleep(5)
                resp = self.session.post(url=url, data="", cookies=self.cookies, headers=self.headers,
                                         allow_redirects=False)
            print(resp.status_code)
            print(resp.json().get("datas", None))
            if resp.json().get("datas", None):
                items = resp.json().get("datas", None)
            else:
                items = resp.json().get("data", None)
            if not items:
                with open("out_of_query.txt", mode="a+", encoding="utf-8") as fp:
                    fp.write(title)
            for item in items:
                item[
                    "notice_url"] = f'http://www.gsxt.gov.cn/affiche-query-info-inspect.html?noticeId={item.get("noticeId")}&datafrom=&provinceid=100000'
                self.save_to_redis_as_zset(item=item)
            time.sleep(2)

    def save_to_redis_as_zset(self, key="order_company", item=None):
        '''匹配数据中的注册号,可能位数 13 15 18 位,'''
        score = 0
        res = re.search(pattern="([0-9A-Z]{18})[\)）/]|([0-9A-Z]{13})[\)）/]|([0-9A-Z]{15})[\)）/]",
                        string=item.get("noticeContent"))
        if res:
            reg_num = res.group()[:-1]
        else:
            reg_num = ""
            print("注册码获取失败", score)

        title = item.get("noticeTitle")
        pattern = "关于(.+)(列入+?|的列入+?)"
        res = re.match(pattern=pattern, string=title)
        if not res:
            pattern = "(^[^关于].+)(列入+?|的列入+?)"
            res = re.match(pattern=pattern, string=title)
            try:
                name = res.group(1)
                if name[-2:] == "企业":
                    name = name[:-2]
                elif name[-1:] == "的":
                    name = name[:-1]
                print(title, "--------", name)
            except:
                name = ""
                print("匹配失败", title)
        else:
            try:
                name = res.group(1)
                if name[-2:] == "企业":
                    name = name[:-2]
                elif name[-1:] == "的":
                    name = name[:-1]
                print(title, "--------", name)
            except:
                name = ""
                print("匹配失败", title)
        if name in ["广州市荔湾区工商行政管理局", "广州市白云区工商行政管理局", "广州市海珠区工商行政管理局", "广州市增城区工商行政管理局", "广州市工商行政管理局", "辽宁省市场监督管理局"]:
            print(name)
            title = item.get("noticeContent")
            pattern_content_company = "(.+?)（统一社会信用代码/"
            result = re.match(pattern=pattern_content_company, string=title)
            try:
                name = result.group(1)
            except:
                name = ""
                print("匹配失败", title)
        if name in ["吉林省工商行政管理局"]:
            print(name)
            title = item.get("noticeContent")
            result = re.findall(pattern="(<p text-align: center font-size:16px>|<p>)(.+)</p>", string=title)
            try:
                name = result[0][1].split("</p><p>")[1]
                if "统一社会信用代码" in name:
                    name = re.match(pattern="(.+?)[\(]", string=name).group(1)
            except:
                name = ""
                print("匹配失败", title)
        data = {k: v for k, v in item.items() if v != "" or v == "None"}
        data["company_name"] = name
        data["reg_num"] = reg_num
        data = str(data)
        print(data)
        if not self.r.zrank(key, data):
            result = self.r.zadd(key, {data: score})
            print("写入结果", result)
        else:
            print("[!]元素已存在")

    def read_redis(self):
        counts = self.r.zcount("order_company", 0, 2)
        print(counts)
        for i in range(counts):
            data = \
                self.r.zrange("order_company", start=i, end=i, desc=False, withscores=True, score_cast_func=int)[0][
                    0].decode("utf-8")
            print(data, "\n", i)
            with open("./name.txt", "a+", encoding="utf-8") as fp:
                fp.write(eval(data).get("company_name", 0) + "\n")


s = Search()
s.open_chrome()
s.get_cookies()
s.get_data()
# s.read_redis()
