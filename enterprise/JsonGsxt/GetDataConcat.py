# encoding=utf8
"""
@Date       :2019/4/28
@Author     :
@Software   :Pycharm
"""
import datetime
import hashlib
import json
import logging.config
import time

import os
import pymongo
import redis
import requests
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By  # 选择方法
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待

from helper.common import BaseConfig, execJS  # 相关配置

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs/getDate/")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
LOG_FILE = datetime.datetime.now().strftime("%Y-%m-%d") + "getDate.log"
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


class CompanyInfo(BaseConfig):

    def __init__(self):
        self.r = redis.Redis(host=self.HOST, port=self.PORT, db=BaseConfig.DB_INDEX, password=self.PASSWORD)
        self.info_base_url = u"http://www.gsxt.gov.cn"
        self.md5 = hashlib.md5()
        self.query_page = u"http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html"
        conn = pymongo.MongoClient(host=self.MONGODB_HOST, port=self.MONGODB_PORT)
        self.db = conn.shixin
        self.db.authenticate(self.MONGODB_USER, self.MONGODB_PWD)
        # self.conn_87 = pymongo.MongoClient(host=self.MONGODB_HOST_87, port=self.MONGODB_PORT_87)
        # self.db_87 = self.conn_87.shixin
        # self.db_87.authenticate(self.MONGODB_USER_87, self.MONGODB_PWD_87)
        self.cookies = {}
        self.info_url = None
        self.site = "http://www.gsxt.gov.cn"
        self.headers = {
            'Host': 'www.gsxt.gov.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
            'Refer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Referer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
            'Origin': 'http://www.gsxt.gov.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
        }
        self.base = "http://www.gsxt.gov.cn/affiche-query-info-afficheBaseDetailInfo-{}.html?datafrom="
        self.post_data = {
            "draw": "1",
            "start": "0",
            "length": "5"
        }

    # 获取 redis数据库中 order_company 有序集合 的一条数据
    def get_redis_data(self):
        '''
        该方法主要是获取redis中数据,取出失信企业的注册码,如果没有注册码,则匹
        配公告内容中的公司名称,使用注册码查询相对文字较为稳定,不容易ban掉.
        :return:notice_url  keyword
        '''
        self.key = self.r.zrange(self.REDIS_SET_NAME, start=0, end=0,
                                 desc=False, withscores=True, score_cast_func=int)[0][0].decode("utf-8")
        self.brief_msg = json.loads(self.key)
        notice_id = self.brief_msg.get(u"noticeId")
        company_name = self.brief_msg.get(u"company_name")
        notice_type = self.brief_msg.get(u"noticeType")
        return notice_id, company_name, notice_type

    def _get_cookies(self):
        url = "http://www.gsxt.gov.cn/index.html"
        resp = requests.get(url=url, headers=self.headers)
        self.cookies = execJS(resp.text)
        self.cookies["__jsluid"] = resp.cookies.get("__jsluid")

    def get_cookies(self):
        """
        使用selenium 动态获取cookie中__jsluid 和 __jsl_clearance 的值
        :return:
        """
        display = Display(visible=0, size=(1280, 800))  # 创建虚拟展示界面
        display.start()  # 开始
        logging.info(u'[*] 1. 第一次访问或者cookies失效，状态码为521，正在通过selenium获取...')
        self.cookies = {}
        options = webdriver.ChromeOptions()
        options.add_argument(u'--disable-gpu')
        options.add_argument(u'--no-sandbox')

        browser = webdriver.Chrome(chrome_options=options)
        browser.get(u"http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html")
        wait_gonggao_page = WebDriverWait(browser, 20)
        for i in range(3):
            try:
                flag = wait_gonggao_page.until(
                    EC.text_to_be_present_in_element((By.XPATH, u"//div[@class='page_left']/a[5]/div[@id='tab4']"),
                                                     u'严重违法失信企业名单公告'))
            except TimeoutException:
                flag = None
            if flag:
                break
        time.sleep(2)
        self.cookies = {cookie.get(u"name"): cookie.get(u"value") for cookie in browser.get_cookies()}
        browser.quit()
        display.sendstop()

    def query(self):
        notice_id, company, notice_type = self.get_redis_data()
        url = self.base.format(notice_id)
        time.sleep(1)
        resp = requests.post(url=self.base.format(notice_id), cookies=self.cookies,
                             headers=self.headers)
        while resp.status_code != 200 and resp.text:
            if resp.status_code == 521:
                logger.info("cookies expire,updating...")
                self._get_cookies()
                time.sleep(1)
            logger.info("server error,waiting for a while")
            time.sleep(60)
            resp = requests.post(url=url, cookies=self.cookies,
                                 headers=self.headers)
        try:
            data = resp.content.decode("utf-8")
            data = json.loads(data)
            data["company"] = company
            if notice_type == "21":
                self.deal_data_in(data, url)
            elif notice_type == "22":
                self.deal_data_out(data, url)
            else:
                logger.info("Notice Type Error")
        except Exception as e:
            logger.info(e.args)

    def deal_data_out(self, data, info_url):
        """
        reDecOrg_CN:信用修复发布机构  serILLRea_CN 失信列入原因  company  remExcpRes_CN 信用修复原因  remDate 修复时间  _src：{url,timestamp,site}
        abntime 列入时间   _record_id  MD5 inforType 名单类型  decOrg_CN 失信列入机构
        :param data:
        :return:
        """
        final_data = {}
        final_data["decOrg_CN"] = data.get("reDecOrg_CN")  # 执行机构
        timestamp = str(int(time.time() * 1000))
        site = "http://www.gsxt.gov.cn"
        _record_id_str = info_url + timestamp + site
        self.md5.update(_record_id_str)
        final_data["_record_id"] = self.md5.hexdigest()
        if data.get("judDate", None):
            final_data["remDate"] = time.strftime("%Y-%m-%d", time.localtime(data.get("judDate", 0) / 1000))
        elif data.get("noticeDate", None):
            final_data["remDate"] = time.strftime("%Y-%m-%d", time.localtime(data.get("noticeDate", 0) / 1000))
        else:
            final_data["remDate"] = None
        final_data["_src"] = [{"url": info_url, "timestamp": timestamp, "site": self.site}]
        b = {u"满5年": u"5年未发生列入严重违法失信企业名单情形的且企业主动申请", u"满5年未再发生": u"5年未发生列入严重违法失信企业名单情形的且企业主动申请",
             u"单位申请": ""u"5年未发生列入严重违法失信企业名单情形的且企业主动申请", u"注销": u"企业已注销，自动移出严重违法失信企业名单", }
        for i in b.keys():
            if i in data.get("noticeContent"):
                final_data["remExcpRes_CN"] = b.get(i, None)
                break
        if not final_data.get("remExcpRes_CN", None):
            final_data["remExcpRes_CN"] = data.get("noticeContent")
        final_data["company"] = data.get("company")  # 公司名称
        final_data["inforType"] = "null"
        final_data["serILLRea_CN"] = "null"
        final_data["abntime"] = "null"

        final_data["reDecOrg_CN"] = data.get("judAuth_CN", "null")  # 信用修复发布机构
        self.save_data(final_data)

    def deal_data_in(self, data, info_url):
        """
        reDecOrg_CN:信用修复发布机构  serILLRea_CN 失信列入原因  company  remExcpRes_CN 信用修复原因  remDate 修复时间  _src：{url,timestamp,site}
        abntime 列入时间   _record_id  MD5 inforType 名单类型  decOrg_CN 失信列入机构
        :param data:
        :return:
        """
        final_data = {}
        final_data["decOrg_CN"] = data.get("judAuth_CN")  # 执行机构
        if u"失信" in data.get("noticeTitle", "") or u"严重" in data.get("noticeTitle", ""):
            final_data["inforType"] = u"严重违法失信企业名单"
        else:
            final_data["inforType"] = data.get("noticeTitle")
        timestamp = str(int(time.time() * 1000))
        site = "http://www.gsxt.gov.cn"
        _record_id_str = info_url + timestamp + site
        self.md5.update(_record_id_str)
        final_data["_record_id"] = self.md5.hexdigest()
        if data.get("judDate", None):
            final_data["abntime"] = time.strftime("%Y-%m-%d", time.localtime(data.get("judDate", 0) / 1000))
        else:
            final_data["abntime"] = None
        final_data["_src"] = [{"url": info_url, "timestamp": timestamp, "site": self.site}]
        final_data["remDate"] = data.get("remDate")  # 修复日期

        final_data["remExcpRes_CN"] = data.get("remExcpRes_CN")
        final_data["company"] = data.get("company")  # 公司名称

        a = (u"被列入经营异常名录届满3年仍未履行相关义务的",
             u"被列入经营异常名录届满3年仍未履行相关义务",
             u"异常名录满三年，仍未履行",
             u"被列入经营异常名录届满3年仍未履行相关义务的",
             u"国家工商行政管理总局规定的其他违反工商行政管理法律、行政法规且情节严重的",
             u"因发布虚假广告两年内受到三次以上行政处罚的，或者发布关系消费者生命健康的商品或者服务",
             u"被列入经营异常名录届满3年公告提醒后仍未履行相关义务",
             u"提交虚假材料或者采取其他欺诈手段隐瞒重要事实，取得公司变更或者注销登记，被撤销登记的",
             u"组织策划传销的，或者因为传销行为提供便利条件两年内受到三次以上行政处罚的",
             u"因商标侵权行为五年内受到两次以上行政处罚",
             u"提交虚假材料或者采取其他欺诈手段隐瞒重要事实，取得公司变更或者注销登记，被撤销登记",
             u"因商标侵权行为五年内受到两次以上行政处罚的",
             u"其他",)

        for i in a:
            if i in data.get("noticeContent"):
                final_data["serILLRea_CN"] = i  # 列入原因
                break
        if not final_data.get("serILLRea_CN"):
            final_data["serILLRea_CN"] = u"其他"
        final_data["reDecOrg_CN"] = ""  # 信用修复发布机构
        print final_data
        self.save_data(final_data)

    def save_data(self, data):
        """
        数据保存
        :param data:
        :return:
        """
        shi_xin_set = self.db.json_shixin_datas
        shi_xin_set.insert(data)

    def change_redis(self):
        """
        改变处理数据的分数
        :return:
        """
        self.r.zincrby(BaseConfig.REDIS_SET_NAME,
                       value=self.key, amount=1)

    def start(self):
        try:
            self._get_cookies()
        except:
            self.get_cookies()
        while True:
            try:
                counts = self.r.zcount(BaseConfig.REDIS_SET_NAME, 0, 0)
                if counts:
                    logger.info("waiting get data:{}".format(counts))
                    for i in range(counts):
                        self.query()
                        self.change_redis()
                        time.sleep(2)
                logger.info("no data need deal,sleep {} s".format(self.CYCLE_WAITE_TIME))
                time.sleep(self.CYCLE_WAITE_TIME)
            except Exception as e:
                logger.info(e.args)

    def __del__(self):
        pass


if __name__ == '__main__':
    t = CompanyInfo()
    t.start()
