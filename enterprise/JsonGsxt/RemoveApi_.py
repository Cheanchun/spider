# -*- coding: utf-8 -*-
"""
@Date       :2019/4/28
@Author     :
@Software   :Pycharm
"""
import datetime
import json
import logging.config
import random
import time

import os
import re
import requests

from GetInApi_ import ParseApi
from helper.common import BaseConfig

SCORE = 0
REDIS_KEY = "shixin:remove"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs/remove/")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
LOG_FILE = datetime.datetime.now().strftime("%Y-%m-%d") + "reApi.log"
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
logger = logging.getLogger(__file__)


# 获取api数据
class ParseRemoveApi(ParseApi):
    # 获得失信企业名单
    def get_api_data(self):
        for areaId in self.AREA_ID:
            print "areaID:{}".format(areaId)
            time.sleep(random.randint(1, 7))
            self.data_list = []
            logging.info(u"地区ID:{}".format(areaId))
            url = 'http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html?noticeType=22&areaid=100000&noticeTitle=&regOrg={}'.format(
                areaId)
            for i in range(1, 3):
                time.sleep(random.randint(1, 7))
                post_data = {
                    "draw": i,
                    "start": (i - 1) * 10,
                    "length": 10,
                }
                try:
                    company_json = requests.post(url=url, headers=self.headers, cookies=self.cookies,
                                                 data=post_data, )
                    request_num = 0
                    while company_json.status_code != 200 and request_num < 3:
                        print(company_json.status_code)
                        if company_json.status_code == 521:
                            try:
                                self._get_cookies()
                            except:
                                self.get_cookies()
                        time.sleep(random.randint(1, 7))
                        company_json = requests.post(url=url, headers=self.headers, cookies=self.cookies,
                                                     data=post_data, )
                        request_num += 1
                except Exception as e:
                    logging.info(u"请求失败{}：{}".format(e, url))
                    company_json = requests.post(url=url, headers=self.headers, cookies=self.cookies,
                                                 data=post_data, )
                try:
                    self.data_list.extend(company_json.json().get('data'))
                except Exception as e:
                    print "data getting error!:{}".format(e.args)
                    time.sleep(300)
                time.sleep(random.randint(2, 7))
            if self.data_list:
                self.parse_data()

    def save_to_redis_as_zset(self, key=BaseConfig.REDIS_SET_NAME, item=None):
        '''匹配数据中的注册号,可能位数 13 15 18 位,'''

        res = re.search(pattern=u"([0-9A-Z]{18})[\)）/]|([0-9A-Z]{13})[\)）/]|([0-9A-Z]{15})[\)）/]",
                        string=item.get("noticeContent"))
        if res:
            reg_num = res.group()[:-1]
        else:
            reg_num = ""
        title = item.get(u"noticeTitle")
        pattern = u"关于(.+)(移出+?|的移出+?)"
        res = re.match(pattern=pattern, string=title)
        if not res:
            pattern = u"(^[^关于].+)(移出+?|的移出+?)"
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
        res = self.r.zadd(key, {data: SCORE})
        if res:
            print "write in status:{}".format(res)

    def start(self):
        try:
            self._get_cookies()
        except:
            self.get_cookies()
        while True:
            try:
                print "start new cycle data getting..."
                self.get_api_data()
                print "remove api one cycle finish,sleep {} s".format(self.CYCLE_WAITE_TIME)
            except Exception as e:
                logger.info(e.args)
            time.sleep(self.CYCLE_WAITE_TIME)


if __name__ == '__main__':
    remove = ParseRemoveApi()
    remove.start()
