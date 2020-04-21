# -*- coding: utf-8 -*-
'''
@Date       :2018/12/28
@Author     :
@Software   :Pycharm
'''
import datetime
import logging.config
import time

import os
import random
import re
import redis
import requests
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By  # 选择方法
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待

from helper.config import BaseConfig

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs/api/")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
LOG_FILE = datetime.datetime.now().strftime("%Y-%m-%d") + "api.log"
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
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
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
api_logger = logging.getLogger(__file__)


# 获取api数据
class ParseApi(BaseConfig):
    session = requests.Session()
    display = Display(visible=0, size=(1280, 800))  # 创建虚拟展示界面
    display.start()  # 开始
    cookies = {}
    data_list = []
    ip_list = []

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

            # 129
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

            # 87
            # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',

            # windows
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36', # windows
            'Host': 'www.gsxt.gov.cn',
            'Refer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Referer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Origin': 'http://www.gsxt.gov.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Connection': 'keep - alive',

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
        # print('[*] 1. 第一次访问或者cookies失效，状态码为521，正在通过selenium获取...')
        self.cookies = {}
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(chrome_options=options)
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
        # print("cookies", self.cookies)

    def get_ip(self):
        ip_url = "http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy?spiderId=bcf4b1d29b374d10a6a1d14fd08e516f&returnType=1&count=1"
        if self.ip_list:
            return self.ip_list.pop()
        else:
            self.ip_list = requests.get(url=ip_url).text.split()
            # print(self.ip_list)
            return self.ip_list.pop()

    # 更换代理ip
    def change_proxy(self):
        self.session.proxies = self.get_ip()

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
                api_logger.info("地区ID{}".format(areaId))
                url = f'http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html?noticeType=22&areaid=100000&noticeTitle=&regOrg={areaId.decode("utf-8")}'
                for i in range(1, 6):
                    # print(post_data)
                    try:
                        company_json = requests.post(url=url, headers=self.headers, cookies=self.cookies,
                                                     data=post_data, )
                        # print(company_json.status_code)
                    except Exception as e:
                        self.session.proxies = self.get_ip()
                        company_json = requests.post(url=url, headers=self.headers, cookies=self.cookies,
                                                     data=post_data, )
                    try:
                        self.data_list.extend(company_json.json().get('data'))
                    except:
                        api_logger.info(f"[!]非json数据返回:{areaId}:{i}")
                        break
                    if company_json.status_code == 521:
                        self.get_cookies()
                    post_data['draw'] = post_data.get("draw") + 1
                    post_data['start'] = post_data.get("start") + 10
                    time.sleep(random.randint(2, 4))
                if self.data_list:
                    self.parse_data()
                else:
                    api_logger.info(f"[!]api数据列表为空{areaId}")
                areaId = self.r.lpop("areaId")

        else:
            url = 'http://www.gsxt.gov.cn/SearchItemCaptcha?t=' + str(round(time.time() * 1000))
            index_page = self.session.get(url, headers=self.headers, cookies=cookies)
            if index_page.status_code == 521:
                self.get_cookies()
                self.get_api_data()
                self.get_api_data(self.cookies)
            elif re.search("有疑似非正常访问行为", str(index_page.text)):
                api_logger.info("[!]目标网站监测出非正常访问,稍后再试!")
        api_logger.info("所有地区ID已经爬去完成")

    def parse_data(self):
        for item in self.data_list:
            item[
                "notice_url"] = f'http://www.gsxt.gov.cn/affiche-query-info-inspect.html?noticeId={item.get("noticeId")}&datafrom=&provinceid=100000'
            self.save_to_redis_as_zset(item=item)

    def save_to_redis_as_zset(self, key="order_company", item=None):
        '''匹配数据中的注册号,可能位数 13 15 18 位,'''
        score = 0
        res = re.search(pattern="([0-9A-Z]{18})[\)）/]|([0-9A-Z]{13})[\)）/]|([0-9A-Z]{15})[\)）/]",
                        string=item.get("noticeContent"))
        if res:
            reg_num = res.group()[:-1]
        else:
            reg_num = ""
            # print("注册码获取失败", score)

        title = item.get("noticeTitle")
        pattern = "关于(.+)(移出+?|的移出+?)"
        res = re.match(pattern=pattern, string=title)
        if not res:
            pattern = "(^[^关于].+)(移出+?|的移出+?)"
            res = re.match(pattern=pattern, string=title)
            try:
                name = res.group(1)
                if name[-2:] == "企业":
                    name = name[:-2]
                elif name[-1:] == "的":
                    name = name[:-1]
                # print(title, "--------", name)
            except:
                name = ""
                api_logger.info("匹配失败", title)

        else:
            try:
                name = res.group(1)
                if name[-2:] == "企业":
                    name = name[:-2]
                elif name[-1:] == "的":
                    name = name[:-1]
            except:
                name = ""
                api_logger.info(f"匹配失败{title}", )

        if name in [u"广州市荔湾区工商行政管理局", u"广州市白云区工商行政管理局", u"广州市海珠区工商行政管理局", u"广州市增城区工商行政管理局", u"广州市工商行政管理局",
                    u"辽宁省市场监督管理局", u"广州市荔湾区市场监督管理局", u"广州市天河区工商行政管理局", u"广州市天河区工商行政管理局", u"广州市市场监督管理局"]:
            # print(name)
            title = item.get("noticeContent")
            pattern_content_company = "(.+?)（统一社会信用代码/"
            result = re.match(pattern=pattern_content_company, string=title)
            try:
                name = result.group(1)
                # print(name)
            except:
                name = ""
                api_logger.info(f"匹配失败{title}")
        if name in ["吉林省工商行政管理局"]:
            # print(name)
            title = item.get("noticeContent")
            result = re.findall(pattern="(<p text-align: center font-size:16px>|<p>)(.+)</p>", string=title)
            try:
                name = result[0][1].split("</p><p>")[1]
                if "统一社会信用代码" in name:
                    name = re.match(pattern="(.+?)[\(]", string=name).group(1)
            except:
                name = ""
                api_logger.info(f"匹配失败{title}")
        data = {k: v for k, v in item.items() if v != "" or v == "None"}
        data["company_name"] = name
        data["reg_num"] = reg_num
        data = str(data)
        # print(data)
        if not self.r.zrank(self.REDIS_SET_NAME, data):
            self.r.zadd(self.REDIS_SET_NAME, {data: score})
            # print("写入结果", result)
        else:
            pass
            # print("[!]元素已存在")

    def __del__(self):
        self.display.stop()


def main():
    parseapi = ParseApi()
    parseapi.get_api_data()


if __name__ == '__main__':
    api_logger.info("开始获取json数据...")
    main()
