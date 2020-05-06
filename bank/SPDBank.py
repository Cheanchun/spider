# coding:utf-8
import datetime
import json
import random
import re
import time
from copy import deepcopy

import redis
import requests
from lxml import etree
from lxml.etree import XMLSyntaxError
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from bank.utils.Comm import CommSession

redis_info = {
    'host': '47.105.54.129',
    'port': 6388,
    'password': 'admin'
}
user_redis = redis.StrictRedis(**redis_info)


class GuangDa():

    def __init__(self):
        self.charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
        self.pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
        self.USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
        self.post_url = 'https://per.spdb.com.cn/was5/web/search'
        self.user_redis = user_redis
        self.financial_type = {'0': u'保证收益', '1': u'保本浮动收益', '2': u'非保本浮动收益'}
        # 汇理财
        self.limit = {'235': u'35天', '101': u'一月', '103': u'三月', '106': u'六月',
                      '001': u'一年', '002': u'二年', '003': u'三年', '005': u'五年'
                      }
        self.financial_type_hui = {'2': u'保本浮动收益', '8': u'非保本浮动收益', '3': u'保证收益', }
        self.session = CommSession(verify=False).session()
        self.change_cookie()
        self.redis_key = 'financial_pufa'
        self.currency = {'finance_currency = 01 ': '人民币', 'finance_currency = 12 ': '英镑',
                         'finance_currency = 13 ': '港币', 'finance_currency = 14 ': '美元',
                         'finance_currency != 01 and finance_currency != 12 and finance_currency != 13 amd finance_currency != 14 ': '其他'}

    def change_cookie(self):
        headers = {
            "Accept": "application/json, test/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "per.spdb.com.cn",
            "Origin": "https://per.spdb.com.cn",
            "Referer": "https://per.spdb.com.cn/bank_financing/financial_product/",
            "X-Requested-With": "XMLHttpRequest",
            'User-Agent': self.USER_AGENT,
            'Cookie': self.get_cookies()
        }
        self.session.headers = headers

    def get_cookies(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument('--no-sandbox')
        options.add_argument("--headless")
        c = DesiredCapabilities.CHROME.copy()
        c['acceptSslCerts'] = True
        c['acceptInsecureCerts'] = True
        options.add_argument("--user-agent={}".format(self.USER_AGENT))
        chrome = webdriver.Chrome(chrome_options=options, desired_capabilities=c)
        products_url = 'https://per.spdb.com.cn/bank_financing/financial_product/'
        chrome.get(products_url)
        time.sleep(3)
        cookies = chrome.get_cookies()
        chrome.quit()
        return ';'.join([item.get('name') + '=' + item.get('value') for item in cookies])

    def _get(self, url, timeout=30, method='get', post_data=None, retry=3):
        """
        网页下载
        :param url:
        :return:resp
        :rtype: requests.Response
        """
        time.sleep(random.randint(7, 10))
        if method == 'get':
            for i in range(retry):
                try:
                    resp = self.session.get(url=url, timeout=timeout)
                    if resp.status_code // 100 == 2:
                        return resp
                except requests.Timeout:
                    continue
            raise requests.RequestException('requests error {}'.format(url))
        elif method == 'post' and post_data is not None:
            for i in range(retry):
                try:
                    resp = self.session.post(url=url, data=post_data, allow_redirects=True, timeout=timeout)
                    if resp.status_code // 100 == 2:
                        return resp
                except requests.Timeout:
                    continue
                except Exception:
                    self.change_cookie()
            raise requests.RequestException(
                'requests error {},post data{}'.format(url, json.dumps(post_data, ensure_ascii=False)))
        else:
            raise ValueError('func args error')

    @staticmethod
    def content2tree(response):
        if isinstance(response, requests.Response):
            return etree.HTML(response.text)
        else:
            try:
                return etree.HTML(response)
            except XMLSyntaxError as error:
                print error
                return response

    def product_term(self, data, final_data, kind):
        if kind == u'现金管理类':
            temp = data.get('finance_lmttime_info')
            res_temp = temp if temp != '-' else u'无固定期限'
        elif kind == u'汇理财':
            temp = data.get('finance_limittime')
            res_temp = self.limit.get(temp, '')
        else:
            res_temp = data.get('finance_lmttime_info', '')
        final_data['product_term'] = res_temp

    def product_nature(self, data, final_data, _type):
        if _type == u'汇理财':
            final_data['product_nature'] = self.financial_type_hui.get(data.get('finance_type', '3'), u'保证收益')
        else:
            final_data['product_nature'] = self.financial_type.get(data.get('finance_type', '3'), u'保证收益')

    def date_format(self, data, _type, currency_type):
        final_data = {}
        for item in data:
            final_data['currency'] = currency_type
            final_data['issue_bank'] = u'浦发银行'
            final_data['product_name'] = item.get('finance_allname')
            final_data['sales_start_date'] = ''
            final_data['sales_end_date'] = ''
            final_data['product_status'] = item.get('finance_state')
            final_data['value_date'] = ''
            temp_rate = item.get('finance_anticipate_rate')
            final_data['highest_yield'] = temp_rate if temp_rate.split('.')[0] in ['1', '0'] else temp_rate + '%'
            final_data['lowest_yield'] = final_data['highest_yield']
            self.product_term(item, final_data, _type)
            final_data['min_purchase_amount'] = item.get('finance_indi_ipominamnt')
            final_data['sales_target'] = ''
            final_data['sales_area'] = ''
            self.product_nature(item, final_data, _type)
            final_data['product_type'] = _type
            final_data['file_url'] = item.get('product_attr')
            self._save_data(final_data)
            final_data.clear()

    @staticmethod
    def _save_data(data, url=None, source=None):
        temp = json.dumps(data, ensure_ascii=False, encoding='u8')
        fp.write(temp.encode('u8') + '\n')
        fp.flush()
        print temp

    def post_data_from_redis(self):
        if not self.user_redis.exists(self.redis_key):
            type_list = [
                {
                    "metadata": "finance_allname|finance_anticipate_rate|finance_limittime|finance_indi_ipominamnt|finance_type|finance_no|finance_state|docpuburl|finance_risklevel|product_attr",
                    "channelid": "263468",
                    "page": "1",
                    "searchword": "finance_limittime = %*({currency})*(finance_state='{state}')",
                    'kind': '汇理财'
                },
                {
                    "metadata": "finance_state|finance_no|finance_allname|finance_anticipate_rate|finance_limittime|finance_lmttime_info|finance_type|docpuburl|finance_ipo_enddate|finance_indi_ipominamnt|finance_indi_applminamnt|finance_risklevel|product_attr|finance_ipoapp_flag|finance_next_openday",
                    "channelid": "266906",
                    "page": "1",
                    "searchword": "(product_type=3)*finance_limittime = %*({currency})*(finance_state='{state}')",
                    'kind': '固定期限'
                },
                {
                    "metadata": "finance_state|finance_no|finance_allname|finance_anticipate_rate|finance_limittime|finance_lmttime_info|finance_type|docpuburl|finance_ipo_enddate|finance_indi_ipominamnt|finance_indi_applminamnt|finance_risklevel|product_attr|finance_ipoapp_flag|finance_next_openday",
                    "channelid": "266906",
                    "page": "1",
                    "searchword": "(product_type=4)*finance_limittime = %*({currency})*(finance_state='{state}')",
                    'kind': '现金管理类'
                },
                {
                    "metadata": "finance_state|finance_no|finance_allname|finance_anticipate_rate|finance_limittime|finance_lmttime_info|finance_type|docpuburl|finance_ipo_enddate|finance_indi_ipominamnt|finance_indi_applminamnt|finance_risklevel|product_attr|finance_ipoapp_flag|finance_next_openday",
                    "channelid": "266906",
                    "page": "1",
                    "searchword": "(product_type=2)*finance_limittime = %*({currency})*(finance_state='{state}')",
                    'kind': '净值类'
                },
                {
                    "metadata": "finance_state|finance_no|finance_allname|finance_anticipate_rate|finance_limittime|finance_lmttime_info|finance_type|docpuburl|finance_ipo_enddate|finance_indi_ipominamnt|finance_indi_applminamnt|finance_risklevel|product_attr|finance_ipoapp_flag|finance_next_openday",
                    "channelid": "266906",
                    "page": "1",
                    "searchword": "(product_type=0)*finance_limittime = %*({currency})*(finance_state='{state}')",
                    'kind': '私行专属'
                },
                {
                    "metadata": "finance_state|finance_no|finance_allname|finance_anticipate_rate|finance_limittime|finance_lmttime_info|finance_type|docpuburl|finance_ipo_enddate|finance_indi_ipominamnt|finance_indi_applminamnt|finance_risklevel|product_attr|finance_ipoapp_flag|finance_next_openday",
                    "channelid": "266906",
                    "page": "1",
                    "searchword": "(product_type=1)*finance_limittime = %*({currency})*(finance_state='{state}')",
                    'kind': '专属产品'
                }
            ]
            status_list = ['即将发售', '可购买', '不可购买', '已过期']
            for post_data in type_list:
                for stat in status_list:
                    for currency_code, currency in self.currency.iteritems():
                        try:
                            temp_post_data = deepcopy(post_data)
                            temp_post_data['searchword'] = post_data.get('searchword').format(
                                currency=currency_code, state=stat)
                            kind = temp_post_data.pop('kind')
                            resp = self._get(self.post_url, method='post', post_data=temp_post_data)
                            if 'json' not in resp.headers.get('Content-Type'):
                                print 'no data : kind:{}，currency {},post data {}'.format(kind, currency,
                                                                                          json.dumps(temp_post_data,
                                                                                                     ensure_ascii=False))
                                continue
                            temp_post_data['pageTotal'] = resp.json().get('pageTotal')
                            temp_post_data['currency'] = currency
                            temp_post_data['kind'] = kind
                            temp = json.dumps(temp_post_data, ensure_ascii=False)
                            print 'data :post data {};'.format(temp)
                            self.user_redis.sadd(self.redis_key, temp)
                        except Exception as req_error:
                            print req_error
                            continue
        return json.loads(self.user_redis.spop(self.redis_key), encoding='utf-8')

    def crawl(self, post_data, start_page, end_page):
        kind = post_data.pop('kind')
        post_data.pop('pageTotal')
        currency = post_data.pop('currency')
        print 'start page {};end page {}'.format(start_page, end_page)
        for page_num in range(start_page, end_page):
            try:
                print 'page num:{}'.format(page_num)
                post_data['page'] = str(page_num)
                resp = self._get(self.post_url, method='post', post_data=post_data)
                json_data = resp.json()
                self.date_format(json_data.get('rows'), _type=kind, currency_type=currency)
            except Exception as e:
                print e
        self.session.close()

    def main(self):
        batch_size = 50
        try:
            post_data = self.post_data_from_redis()
            total_page = int(post_data.get('pageTotal'))
            current_page = int(post_data.get('page'))
            print u'post data {}'.format(json.dumps(post_data, ensure_ascii=False))
            if total_page > batch_size:
                end_page = current_page + batch_size if current_page + batch_size < total_page else total_page + 1
                if end_page != total_page + 1:
                    post_data['page'] = end_page
                    self.user_redis.sadd(self.redis_key, json.dumps(post_data, encoding='u8', ensure_ascii=False))
                self.crawl(post_data, start_page=current_page, end_page=end_page)
            else:
                end_page = post_data.get('pageTotal') + 1
                self.crawl(post_data, start_page=current_page, end_page=end_page)
        except Exception as e:
            print e


if __name__ == '__main__':
    while user_redis.exists('financial_pufa'):
        time.sleep(60)
        fp = open('./datas/pufa{}.txt'.format(str(datetime.date.today())), mode='a+')
        t = GuangDa()
        t.main()
        fp.close()
