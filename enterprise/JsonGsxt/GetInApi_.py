# -*- coding: utf-8 -*-
"""
@Date       :2019/4/28
@Author     :
@Software   :Pycharm
"""
import datetime
import json
import logging.config
import os
import random
import re
import sys
import time

import execjs
import redis
import requests
# from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By  # 选择方法
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待

from helper.common import BaseConfig, execJS

print sys.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs/in/")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
LOG_FILE = datetime.datetime.now().strftime("%Y-%m-%d") + "inApi.log"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            'format': '%(asctime)s [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },

        "default": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": os.path.join(LOG_DIR, LOG_FILE),
            'mode': 'w+',
            "maxBytes": 1024 * 1024 * 1,  # 5 MB
            "backupCount": 10,
            "encoding": "utf8"
        },
    },

    "root": {
        'handlers': ['default'],
        'level': "INFO",
        'propagate': False
    }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__file__)


# 获取api数据
class ParseApi(BaseConfig):
    REDIS_KEY = "shixin:in"
    SCORE = 0
    AREA_ID = (110000, 130000, 140000, 150000, 210000, 220000, 230000, 310000, 320000, 330000,
               340000, 350000, 350000, 360000, 370000, 410000, 420000, 430000, 440000, 450000, 460000,
               500000, 510000, 520000, 530000, 540000, 610000, 620000, 630000, 640000, 650000)

    # AREA_ID = (110000, 130000, 140000)

    def __init__(self):
        """
        areaId 对照
        北京:110000 天津:120000(空) 河北:130000 山西:140000 内蒙古:150000
        辽宁:210000	吉林:210000 黑龙江:230000
        上海:310000 江苏:320000 浙江:330000 安徽:340000 福建:350000 江西:360000 山东:370000
        河南:410000 湖北:420000 湖南:430000 广东:440000 广西:450000 海南:460000 重庆:500000
        四川:510000	贵州:520000	云南:530000 西藏:540000
        陕西:610000 甘肃:620000 青海:630000 宁夏:640000 新疆:650000
        """

        self.headers = {
            'Host': 'www.gsxt.gov.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
            'Refer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Referer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Origin': 'http://www.gsxt.gov.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
        }
        self.url = "http://www.gsxt.gov.cn/index.html"
        self.cookies = {u'__jsluid': u'50c88b7e60482b47adb0df8bc74294f2', u'SECTOKEN': u'6989081476903733867',
                        u'JSESSIONID': u'C5D6DC79A0AB90DA9D30D5E54E918890-n1:0',
                        u'__jsl_clearance': u'1561444042.725|0|hXh54u7L%2FSsq6%2BaZGm2Y2SuHBv8%3D',
                        u'CNZZDATA1261033118': u'1572964249-1561442912-http%253A%252F%252Fwww.gsxt.gov.cn%252F%7C1561442912',
                        u'UM_distinctid': u'16b8d514946512-0fdd931b28cefd-591c3314-100200-16b8d514947420',
                        u'tlb_cookie': u'S172.16.12.69'}
        self.r = redis.Redis(host=self.HOST, port=self.PORT, db=self.DB_INDEX, password=self.PASSWORD)
        self.r1 = redis.Redis(host=self.HOST, port=self.PORT, db=0, password=self.PASSWORD)
        proxies = self.r1.zrangebyscore("proxy", 100, 100)
        self.proxy = {"http:": "http://{}".format(random.choice(proxies))}

    def get_cookies(self):
        """
        使用selenium 动态获取cookie中__jsluid 和 __jsl_clearance 的值
        :return:
        """
        # display = Display(visible=0, size=(1280, 800))  # 创建虚拟展示界面
        # display.start()  # 开始
        logging.info(u'[*] 1. 第一次访问或者cookies失效，状态码为521，正在通过selenium获取...')
        self.cookies = {}
        options = webdriver.ChromeOptions()
        options.add_argument(u"--headless")
        options.add_argument(u'--disable-gpu')
        options.add_argument(u'--no-sandbox')
        options.add_argument(
            u"--user-agent={}".format(self.headers.get("User-Agent")))
        browser = webdriver.Chrome(chrome_options=options,executable_path=)
        browser.get(self.url)
        wait_gonggao_page = WebDriverWait(browser, 20)
        for i in range(3):
            try:
                flag = wait_gonggao_page.until(
                    EC.element_to_be_clickable((By.XPATH, u"//button[@id='btn_query']")))
            except TimeoutException:
                flag = None
            if flag:
                break
        self.cookies = {cookie.get(u"name"): cookie.get(u"value") for cookie in browser.get_cookies()}
        browser.quit()
        print "cookies_selenium:{}".format(self.cookies)

    def _get_cookies(self):
        jsl_clearance = None
        while not jsl_clearance:
            self.url = "http://www.gsxt.gov.cn/index.html"
            resp = requests.get(url=self.url, headers=self.headers)
            self.jsluid = resp.cookies.get("__jsluid")
            second_js = self._first_decryption(resp.text)
            try:
                try:
                    jsl_clearance = self._second_decryption_one(second_js)
                    self.cookies["__jsluid"] = self.jsluid
                    self.cookies["__jsl_clearance"] = jsl_clearance
                    print "get cookies", self.cookies, 1
                except:
                    jsl_clearance = self._second_decryption_two(second_js)
                    self.cookies["__jsluid"] = self.jsluid
                    self.cookies["__jsl_clearance"] = jsl_clearance
                    print "get cookies", self.cookies, 2
            except:
                continue

    def _first_decryption(self, first_js):
        """
        解密js,获得第二层加密的js
        :param first_js:
        :return:
        """
        f = open(r'wc_js.js')
        wc_js = f.read()
        self.wc_js = execjs.compile(wc_js)
        x = re.findall('var x="(.*?)"', first_js)[0]
        y = re.findall(',y="(.*?)"', first_js)[0]
        second_js = self.wc_js.call('once_js', x, y)
        # second_js = self.wc_js.call('get_js', x, y, z)
        f.close()
        return second_js

    def _second_decryption_one(self, second_js):
        """
        把第二层js准换成本地可以运行的js
        !!!此处可能会出错!!!
        :param second_js: 第一次解密的js
        :return: __jsl_clearance的值
        """
        # 转义字符
        js = second_js.replace('\\\\', '\\')

        # 切割
        js = 'cookie' + js.split('document.cookie')[1]
        js = js.split('GMT;Path=/;')[0] + "'"

        # 替换1
        # 取出两个变量名
        _3d = re.findall("(var .{0,5}=)document\.createElement\('div'\);", js)
        _2b = re.findall("(var .{0,5}=).{0,5}\.match\(/https\?:\\\/\\\//\)\[0\];", js)

        # 替换成要访问的url
        js = re.sub("var .{0,5}=document\.createElement\('div'\);",
                    _3d[0] + '"{}";'.format(self.url.replace("http://", "")), js)
        js = re.sub("_.{0,5}\.innerHTML='<a href=.{0,25}</a>';", "", js)
        js = re.sub("_.{0,5}=.{0,5}\.firstChild\.href;", "", js)
        js = re.sub("var .{0,5}=.{0,5}\.match\(/https\?:\\\/\\\//\)\[0\];", _2b[0] + '"http://";', js)
        js = re.sub("_.{0,5}=.{0,5}\.substr\(.{0,5}\.length\)\.toLowerCase\(\);", "", js)

        # 替换可能出现的window
        js = re.sub("!!window\['__p' \+ 'hantom' \+ 'as'\]", 'false', js)
        js = re.sub("!!window\['_p'\+'hantom'\]", 'false', js)
        js = re.sub("!window\['_p' \+ 'hantom'\]", 'true', js)
        s = """
            function cook() {
            %s
            return cookie
            }
            """
        new_js = s % js
        ctx = execjs.compile(new_js)
        # 切割获得的__jsl_clearance
        jsl = ctx.call('cook')
        jsl = jsl.split(';')[0]
        jsl_clearance = jsl.split('=')[1]
        return jsl_clearance

    def _second_decryption_two(self, second_js):
        """
        把第二层js准换成本地可以运行的js
        !!!此处可能会出错!!!
        :param second_js: 第一次解密的js
        :return: __jsl_clearance的值
        """
        # 转义字符
        js = second_js.replace('\\\\', '\\')

        # 切割
        js = 'cookie' + js.split('document.cookie')[1]
        js = js.split('GMT;Path=/;')[0] + "'"

        # 替换可能出现的window
        js = re.sub("!!\s*?window\['__p' \+ 'hantom' \+ 'as'\]", 'false', js)
        js = re.sub("!!\s*?window\['_p'\+'hantom'\]", 'false', js)
        js = re.sub("!window\['_p' \+ 'hantom'\]", 'true', js)

        s = """
            function cook() {
            %s
            return cookie
            }
            """
        new_js = s % js

        ctx = execjs.compile(new_js)
        # 切割获得的__jsl_clearance
        jsl = ctx.call('cook')
        jsl = jsl.split(';')[0]
        jsl_clearance = jsl.split('=')[1]
        return jsl_clearance

    # 获得失信企业名单
    def get_api_data(self):
        for areaId in self.AREA_ID:
            # print "areaID:{}".format(areaId)
            time.sleep(random.randint(1, 5))
            self.data_list = []
            url = u'http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html?noticeType=21&areaid=100000&noticeTitle=&regOrg={}'.format(
                areaId)
            for i in range(1, 6):
                time.sleep(random.randint(2, 4))  # 降低访问频率
                post_data = {
                    "draw": i,
                    "start": (i - 1) * 10,
                    "length": 10,
                }
                try:
                    company_json = requests.post(url=url, headers=self.headers, cookies=self.cookies,
                                                 data=post_data, allow_redirects=False)
                    request_num = 0
                    # print("------------")
                    # time.sleep(100)
                    while company_json.status_code != 200 and request_num < 3:
                        if company_json.status_code == 521:
                            self._get_cookies()
                            try:
                                self._get_cookies()
                            except:
                                self.get_cookies()
                        time.sleep(1)
                        company_json = requests.post(url=url, headers=self.headers, cookies=self.cookies,
                                                     data=post_data, allow_redirects=False)
                        request_num += 1
                except Exception as e:
                    logger.info(u"请求失败{}：{}".format(e, url))
                    company_json = requests.post(url=url, headers=self.headers, cookies=self.cookies,
                                                 data=post_data, allow_redirects=False)
                try:
                    self.data_list.extend(company_json.json().get('data'))
                except Exception as e:
                    logger.info("response page error:{}".format(e.args))
                    time.sleep(random.randint(5, 10))
            if self.data_list:
                self.parse_data()

    def parse_data(self):
        for item in self.data_list:
            item[
                u"notice_url"] = u'http://www.gsxt.gov.cn/affiche-query-info-inspect.html?noticeId={}&datafrom=&provinceid=100000'.format(
                item.get(u"noticeId"))
            self.save_to_redis_as_zset(item=item)

    def save_to_redis_as_zset(self, key=BaseConfig.REDIS_SET_NAME, item=None):
        '''匹配数据中的注册号,可能位数 13 15 18 位,'''

        res = re.search(pattern=u"([0-9A-Z]{18})[\)）/]|([0-9A-Z]{13})[\)）/]|([0-9A-Z]{15})[\)）/]",
                        string=item.get("noticeContent"))
        if res:
            reg_num = res.group()[:-1]
        else:
            reg_num = ""
        title = item.get(u"noticeTitle")
        pattern = u"关于(.+)(列入+?|的列入+?)"
        res = re.match(pattern=pattern, string=title)
        if not res:
            pattern = u"(^[^关于].+)(列入+?|的列入+?)"
            res = re.match(pattern=pattern, string=title)
            try:
                name = res.group(1)
                if name[-2:] == u"企业":
                    name = name[:-2]
                elif name[-1:] == u"的":
                    name = name[:-1]
            except:
                name = ""

        else:
            try:
                name = res.group(1)
                if name[-2:] == u"企业":
                    name = name[:-2]
                elif name[-1:] == u"的":
                    name = name[:-1]
            except:
                name = ""
        # 从特殊区域的公告中获取公司名称
        if name in [u"广州市荔湾区工商行政管理局", u"广州市白云区工商行政管理局", u"广州市海珠区工商行政管理局", u"广州市增城区工商行政管理局", u"广州市工商行政管理局",
                    u"辽宁省市场监督管理局", u"广州市荔湾区市场监督管理局", u"广州市天河区工商行政管理局", u"广州市天河区工商行政管理局", u"广州市市场监督管理局",
                    u"广州市越秀区工商行政管理局", u"广州市番禺区市场监督管理局", u"广州市海珠区市场监督管理局"]:
            title = item.get(u"noticeContent")
            pattern_content_company = u"(.+?)（统一社会信用代码/"
            result = re.match(pattern=pattern_content_company, string=title)
            try:
                name = result.group(1)
            except:
                name = ""
        if name in [u"吉林省工商行政管理局"]:
            title = item.get(u"noticeContent")
            result = re.findall(pattern=u"(<p text-align: center font-size:16px>|<p>)(.+)</p>", string=title)
            try:
                name = result[0][1].split("</p><p>")[1]
                if u"统一社会信用代码" in name:
                    name = re.match(pattern="(.+?)[\(]", string=name).group(1)
            except:
                name = ""
        data = {k: v for k, v in item.items() if v != "" or v != "None"}
        data["company_name"] = name
        data["reg_num"] = reg_num
        data = json.dumps(data, skipkeys=True, ensure_ascii=False, encoding="utf-8")
        print data
        res = self.r.zadd(key, {data: self.SCORE})
        if res:
            print data
            print "write in status:{}".format(res)
        else:
            print "write in fail"
            print data

    def start(self):
        try:
            self.get_cookies()
        except:
            self._get_cookies()
        while True:
            logger.info("start new cycle data getting...")
            try:
                self.get_api_data()
            except Exception as e:
                logger.info(e.args)

    def __del__(self):
        pass


if __name__ == '__main__':
    api_data = ParseApi()
    api_data.start()
