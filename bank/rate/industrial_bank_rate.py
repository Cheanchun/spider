# coding=utf-8
import datetime
import hashlib
import json
import random
import re
import time
import traceback


import chardet
import requests
from lxml import etree
from lxml.etree import XMLSyntaxError

from bank.utils.Comm import CommSession

KEYS_MAP = {
    u"到期日": u"due_date",  # 1
    u"年化收益（较产品起息日）": u"annual_yield_last_value_date",  # 3
    u"近3月到期年化参考收益率": u"3month_reference_rate",  # 4
    u"近3月年化参考收益率": u"3month_reference_rate",
    u"近2月到期年化参考收益率": u"2year_reference_rate",  #
    u"近2月年化参考收益率": u"2year_reference_rate",
    u"近30日到期年化参考收益率": u"30days_maturity_annualized_reference_rate",
    u"近一年到期年化参考收益率": u"1year_reference_rate",
    u"年化收益（较上一开放日）": u"annual_yield_last_open_date",  # 5
    u"最近30日参考收益率（年化）": u"1month_reference_rate",  # 6
    u"近30日年化参考收益率": u"1month_reference_rate",  #
    u"申购价格": u"buy_price",  #
    u"赎回价格": u"call_price",  #
    u"份额累计净值": u"cumulative_net_share_value",  #
    u"业绩比较基准(%)": u"performance_comparison_benchmark",  #
    u"业绩比较基准（上一投资周期）": u"performance_comparison_benchmark_last_week",
    u"单位份额净值": u"net_value_per_share",  #
    u"开放日": u"open_date",
    u"期限(天)": u"deadline",
    u"产品代码": u"product_code",
    u"估值日": u"appraisement_date",
    u"产品名称": u"product_name",
    u"当期业绩比较基准(%)（投资周期起始日）": u"benchmark",  # 2
    u"起息日": u"value_date",
    u"产品类型": u"product_type"}


class IndustrialRate():
    def __init__(self):
        self.index_page = 'http://wealth.cib.com.cn'
        self.session = self.instance_session()
        self.charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
        self.pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
        self.cash_url = 'http://wealth.cib.com.cn/retail/duration/cash/'
        self.open_wlb__url = 'http://wealth.cib.com.cn/retail/duration/open-wlb/'

    def instance_session(self):
        return CommSession().session(self.index_page)

    def _get(self, url, timeout=30, method='get', post_data=None, retry=3):
        """
        网页下载
        :param url:
        :return:resp
        :rtype: requests.Response
        """
        for _ in range(retry):
            try:
                time.sleep(random.randint(3, 5))
                if method == 'get':
                    resp = self.session.get(url=url, timeout=timeout)
                elif method == 'post' and post_data is not None:
                    resp = self.session.post(url=url, data=post_data, allow_redirects=True, timeout=timeout)
                else:
                    raise ValueError('request method not support')
            except requests.exceptions:
                continue
            if resp.status_code // 100 == 2:
                return resp
        raise traceback.format_exc()

    def _coding(self, response):
        if self.charset_re.findall(response.text):
            response.encoding = self.charset_re.findall(response.text)[0]
        elif self.pragma_re.findall(response.text):
            response.encoding = self.charset_re.findall(response.text)[0]
        else:
            temp = chardet.detect(response.content)
            response.encoding = temp['encoding']
        return response

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

    @staticmethod
    def filter_url(data):
        if data[0].endswith('.html') and u'净值' in data[1]:
            return data

    def _parse_url(self, response, url_xpath='//li[@class=\'clearfix\']//@href',
                   title_xpath='//li[@class=\'clearfix\']/a/text()'):
        """
        解析cash页面 每个产品的url
        :param response:
        :param xpath:
        :return: urls -> list
        """
        urls = self.content2tree(response).xpath(url_xpath)
        titles = self.content2tree(response).xpath(title_xpath)
        temp = [(url, title) if url.startswith('http') else (self.index_page + url, title) for url, title in
                zip(urls, titles)]
        return filter(self.filter_url, temp)

    def _check_rate_page(self, response):
        """
        检查该产品跳转页是否为历史净值页
        如果是则返回该响应
        如不是则匹配出相应的历史净值url，并请求返回
        :param response:被检查页面响应
        :return:response
        """
        html = self.content2tree(response)
        if html.xpath(u'//a[contains(text(),\'参考净值/收益率\')]/@class') == u'selected':
            return response
        else:
            rate_url = html.xpath(u'//a[contains(text(),\'参考净值/收益率\')]/@href')
            assert rate_url
            return self._get(rate_url[0] if rate_url[0].startswith('http') else self.index_page + rate_url[0])

    @staticmethod
    def parse_table(table, keys_xpath):
        table_list = []
        xpath_tr, xpath_td = keys_xpath.get(u'tr'), keys_xpath.get(u'td')
        titles = table.xpath(keys_xpath.get(u'titles'))
        for tr in table.xpath(xpath_tr):
            table_data = {}
            for index, title in enumerate(titles):
                try:
                    table_data[''.join(''.join(title.xpath(u'.//text()')).split())] = ''.join(
                        ''.join(tr.xpath(xpath_td)[index].xpath(u'.//text()')).split())
                except Exception as e:
                    table_data[''.join(''.join(title.xpath(u'.//text()')).split())] = u''
                    # print traceback.format_exc()
            table_list.append(table_data)
        return table_list

    def parse_detail(self, response, keys_xpath):
        """
        历史净值详情页解析
        :param response: 详情页响应
        :param keys_xpath: 详情页xpath 解析信息
        :return: None
        """
        html = self.content2tree(response)
        tables = html.xpath(keys_xpath.get(u'tables'))
        data = {}
        product_name = html.xpath(u'//div[@id=\'main-text\']/h1//text()')
        data[u'产品名称'] = product_name[0] if product_name else ''
        tables = tables[:2] if len(tables) > 2 else tables
        for _, table in enumerate(tables):
            if len(tables) == 2 and _ == 0:
                temp = self.parse_table(table, keys_xpath)
                data.update(temp[0])
            if len(tables) == 2 and _ == 1:
                for item in self.parse_table(table, keys_xpath):
                    data.update(item)
                    self.data_format(data)
            if len(tables) == 1:
                data.update(self.parse_table(table, keys_xpath)[0])
                self.data_format(data)

    def data_format(self, source_data, final_data={}):
        """
        将表格数据和 KEYS_MAP 映射 格式化数据
        :param source_data: 网页数据
        :param final_data: 最终入库数据
        :return: None
        """
        temp = json.dumps(source_data, ensure_ascii=False, encoding=u'u8')
        print temp

        if len(source_data) > 5:
            m = hashlib.md5()
            m.update(temp.encode('u8'))
            print m.digest()
            for source_key, data_key in KEYS_MAP.iteritems():
                final_data[data_key] = source_data.get(source_key, u'')
            self._save_data(final_data)

    def _save_data(self, data):
        """
        数据存储
        :param data: 最终数据
        :return: None
        """
        temp = json.dumps(data, ensure_ascii=False, encoding=u'u8')
        print temp
        fp.write(temp.encode(u'utf-8') + '\n')
        fp.flush()

    def rate_page_url(self, response):
        """
        解析产品历史净值url
        :param response: 产品历史净值页面（包含不同时期历史净值链接）
        :return: urls -> list
        """
        html = self.content2tree(response)
        detail_urls = html.xpath(u'//div[@class=\'middle\']/ul/li/a/@href')
        return [url if url.startswith('http') else self.index_page + url for url in detail_urls]

    def _check_next_page(self, response):
        """
        检查历史净值页面是否有下一页，存在则返回url，不存在返回0
        :param response: 历史净值页
        :return: url or 0
        """
        html = self.content2tree(response)
        if not html.xpath(u'//a[contains(@class,\'next-disabled\')]'):
            next_page_url = html.xpath(u'//a[@class=\'next\']/@href')
            return next_page_url[0] if next_page_url[0].startswith(u'http') else self.index_page + next_page_url[0]
        return 0

    def main(self):
        """
        平台调用入口函数
        :return: None
        """
        configs = {u'tables': u'//table', u'titles': u'.//tr[1]/td', u'tr': u'.//tr[position()>1]', u'td': u'./td'}
        product_urls = self._parse_url(self._get(self.open_wlb__url))
        for p_url, title in product_urls:
            print u'product url {}'.format(p_url)
            rate_list_page = self._get(p_url)
            rate_list_response = self._check_rate_page(rate_list_page)
            next_page = 1  # 起始页 默认为 1
            while next_page:  # 当next_page 为0时，停止循环
                if next_page != 1:
                    rate_list_response = self._get(next_page)
                next_page = self._check_next_page(rate_list_response)
                print u'next page:{}'.format(next_page)
                detail_urls = self.rate_page_url(rate_list_response)
                print u'detail_page:', detail_urls
                for detail_url in detail_urls:
                    print u'detail_url: {}'.format(detail_url)
                    self.parse_detail(self._get(detail_url), keys_xpath=configs)


if __name__ == '__main__':
    fp = open('rate{}.txt'.format(str(datetime.date.today())), mode='a+')
    t = IndustrialRate()
    t.main()
    fp.close()
