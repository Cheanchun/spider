# -*- coding: utf-8 -*-
'''
@Date       :2018/12/28
@Author     :
@Software   :Pycharm
'''
import datetime
import json
import logging.config
import time

import fake_useragent
import hashlib
import os
import random
import re
import requests
from copy import copy
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待

from JsonGsxt.helper.config import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs/api/")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
LOG_FILE = datetime.datetime.now().strftime("%Y-%m-%d") + "gsxt.api.log"
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
            "maxBytes": 1024 * 1024 * 1,  # 1 MB
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

ua = fake_useragent.UserAgent()
USER_AGENT = ua.random


class ApiEnterprise(BaseConfig):

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
            "User-Agent": USER_AGENT,
            'Refer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Referer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Origin': 'http://www.gsxt.gov.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
        }
        cnn = MongoClient(host=self.HOST, port=self.PORT)
        db = cnn['shixin']
        db.authenticate('chean', 'scc57295729')
        self.col = db['gsxt_data']
        # self.r = redis.Redis(host=self.HOST, port=self.PORT, db=self.DB_INDEX, password=self.PASSWORD)
        self.proxy = {}
        self.proxies = []
        self.areaIds = (110000, 130000, 140000, 150000, 210000, 220000, 230000, 310000, 320000, 330000,
                        340000, 350000, 350000, 360000, 370000, 410000, 420000, 430000, 440000, 450000,
                        460000, 500000, 510000, 520000, 530000, 540000, 610000, 620000, 630000, 640000,
                        650000)

    def _get_proxy(self):
        """
        :return:ip ->dict
        """
        if not self.proxies:
            self.delay(1, 3)
            logger.info(requests.get(
                'http://wapi.http.cnapi.cc/index/index/save_white?neek=64539&appkey=aa8aee21bfe8659af426549a0ccece21&white=47.105.54.129').json())
            resp = requests.get(PROXY_URL).json()
            if isinstance(resp, dict) and resp.get("code") != 0:
                logger.info("ProxyError:{}".format(resp.get("msg")))
                print("ProxyError:", resp.get("msg"))
                sys.exit()
            self.proxies = [{"http": "http://" + str(proxy.get("ip")) + ":" + str(proxy.get("port"))} for proxy in
                            resp.get("data")]
        print("ips:", len(self.proxies))
        return random.choice(self.proxies)

    def _get_cookies(self):
        """
        使用selenium 动态获取cookie中__jsluid 和 __jsl_clearance 的值
        :return:
        """
        self.cookies = {}
        options = webdriver.ChromeOptions()
        if USE_PROXY_API:
            self.proxy = self._get_proxy()
            print(self.proxy)
            options.add_argument("--proxy-server={}".format(self.proxy.get("http")))  # todo 添加代理
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument("--user-agent={}".format(self.headers.get("User-Agent")))
        options.add_argument("--headless")
        browser = webdriver.Chrome(chrome_options=options)
        browser.get("http://www.gsxt.gov.cn/")
        try:
            WebDriverWait(browser, 20).until(EC.title_is("国家企业信用信息公示系统"))
            self.cookies = {cookie.get("name"): cookie.get("value") for cookie in browser.get_cookies()}
            print(self.cookies)
            browser.quit()
        except Exception as e:
            print(e.args)
            browser.quit()
            self._get_cookies()

    def _get_data(self, url: str, data: dict, timeout: int = 20):
        error = []
        for i in range(3):
            try:
                resp = requests.post(url=url, headers=self.headers, cookies=self.cookies,
                                     data=data, proxies=self.proxy, timeout=timeout, allow_redirects=False)
                if self._check_ban(resp.text) and resp.status_code == 200 and resp.json():
                    return [0, resp]
                elif resp.status_code == 521:
                    self._get_cookies()
            except Exception as e:
                error.append(e.args)
        return [1, error]

    def _paras_data(self, data_list: list):
        for data in data_list:
            final_data = self._paras_enterprise_name_by_title(
                self._format_url(
                    self._paras_enterprise_registration_code(
                        self._data_filter(data)
                    )
                )
            )
            self._save_data(final_data)

    @staticmethod
    def _data_filter(data: dict):
        temp: dict = {}
        for k, v in data.items():
            if v:
                temp[k] = v
        return temp

    def _paras_enterprise_name_by_title(self, data: dict):
        res = []
        try:
            title = data.get("noticeTitle")
            if not res:
                title = data.get("noticeTitle")
                res = re.match(pattern=TITLE_PATTERN_1, string=title)
            if not res:
                res = re.match(pattern=TITLE_PATTERN_2, string=title)
            if res and res.group(1) not in self.SPECIAL_AREA:
                if res.group(1).endswith("企业"):
                    print(res.group(1)[:-2])
                    data["company_name"] = res.group(1)[:-2]
                    return data
                else:
                    print(res.group(1))
                    data["company_name"] = res.group(1)
                    return data
            else:
                return self._paras_enterprise_name_by_content(data)  # 在内容中解析
        except Exception as e:
            logger.error(e.args)
            return data

    def _paras_enterprise_name_by_content(self, data: dict):
        result = []
        try:
            content = data.get("noticeContent")
            patterns = copy(self.SPECIAL_AREA_PATTERNS)
            while not result and patterns:
                result = re.findall(pattern=patterns.pop(0), string=content)
                if result:
                    print(result[0])
                    data["company_name"] = result[0]
                    return data
            if not result:
                data["company_name"] = ""
                logger.info(str(data))
            return data
        except Exception as e:
            data["company_name"] = ""
            logger.error(e.args)
            return data

    @staticmethod
    def _format_url(data: dict):
        try:
            data["notice_url"] = NOTICE_BASE_URL % data.get("noticeId")
            return data
        except Exception as e:
            print(e.args)
            return data

    @staticmethod
    def _paras_enterprise_registration_code(data: dict):
        """匹配数据中的注册号,可能位数 13 15 18 位,"""
        try:
            # 公告可能没有正文
            if data.get("noticeContent"):
                try:
                    res = re.search(pattern=REG_NUM_PATTERN,
                                    string=data.get("noticeContent"))
                    if res:
                        reg_num = res.group()[:-1]
                    else:
                        reg_num = ""
                    data["reg_num"] = reg_num
                    return data
                except Exception as e:
                    print(e.args)
                    return data
            else:
                data["reg_num"] = ""
                return data
        except Exception as e:
            logger.error(e.args)
            data["reg_num"] = ""
            return data

    def _save_data(self, data: dict, key=None):
        """
        将数据存入mongo，
        设置主键：根据主键更新或者新增操作,，存在则更新，不存在则新增
        :param data:
        :return:
        """
        if not key:
            key = data.get('noticeTitle') + data.get('noticeId')
        data_md5 = hashlib.md5()
        key_md5 = hashlib.md5()
        data_md5.update(json.dumps(data, ensure_ascii=False))
        key_md5.update(json.dumps(key, ensure_ascii=False))
        _record_md5 = data_md5.hexdigest()
        _key_md5 = key_md5.hexdigest()
        data['key_md5'], data['_record_md5'] = _key_md5, _record_md5
        # self.col.update({'key_md5': _key_md5) and

    def _check_ban(self, content: str):
        if "访问疑似夹带攻击行为" in content:
            logger.info("访问疑似夹带攻击行为~,exit~")
            self.delay(60, 80)  # todo  反爬处理
        else:
            return True

    @staticmethod
    def delay(start_time: int = 1, end_time: int = 3):
        time.sleep(random.randint(start_time, end_time))

    def main(self):
        self._get_cookies()
        for areaId in self.areaIds:
            data_list = []
            logging.info(f"地区ID:{areaId}")
            url = Remove_URL % areaId
            for i in range(1, 2):
                self.delay(2, 5)  # todo 调整抓取时间
                post_data = {
                    "draw": i,
                    "start": (i - 1) * 10,
                    "length": 10,
                }
                result = self._get_data(url, post_data)
                if result[0] == 0:
                    data_list += result[1].json().get("data")
                elif result[0] == 1:
                    logger.info("请求失败{}:{}".format(url, result[1]))
            if data_list:
                self._paras_data(data_list)
            else:
                logger.info(f"api数据列表为空:{areaId}:{i}")
                print("no data")
        logger.info("所有地区ID已经爬去完成")


if __name__ == '__main__':
    t = ApiEnterprise()
    t.main()
