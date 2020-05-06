# coding:utf-8
import json
import random
import re
import time

import chardet
import requests
from lxml import etree
from lxml.etree import XMLSyntaxError

from bank.utils.Comm import CommSession


class IndustrialBank():

    def __init__(self):
        self.charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
        self.pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
        self.index_url = 'https://www.cib.com.cn/cn/index.html'
        self.session = self.instance_session(self.index_url)

    def _coding(self, response):
        if self.charset_re.findall(response.text):
            response.encoding = self.charset_re.findall(response.text)[0]
        elif self.pragma_re.findall(response.text):
            response.encoding = self.charset_re.findall(response.text)[0]
        else:
            temp = chardet.detect(response.content)
            response.encoding = temp['encoding']
        return response

    def _get(self, url, timeout=30, method='get', post_data=None, retry=3):
        """
        网页下载
        :param url:
        :return:resp
        :rtype: requests.Response
        """
        time.sleep(random.randint(2, 4))
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
                    resp = self.session.post(url=url, data=json.dumps(post_data), allow_redirects=True, timeout=timeout)
                    if resp.status_code == 200:
                        return resp
                except requests.Timeout:
                    continue
            raise requests.RequestException('requests error {}'.format(url))
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
                print(error)
                return response

    @staticmethod
    def instance_session(index_url=None):
        session = CommSession(verify=True).session(index_url) if index_url else CommSession(verify=True).session()
        return session

    def parse_data(self, response, keys_xpath):
        html = self.content2tree(response)
        xpath_table, xpath_tr, xpath_td = keys_xpath.pop('tables'), keys_xpath.pop('tr'), keys_xpath.pop('td')
        tables = html.xpath(xpath_table)
        for table in tables:
            titles = table.xpath(keys_xpath.get('titles'))
            for tr in table.xpath(xpath_tr):
                data = {}
                for index, title in enumerate(titles):
                    try:
                        data[''.join(''.join(title.xpath('.//test()')).split())] = ''.join(
                            ''.join(tr.xpath(xpath_td)[index].xpath('.//test()')).split())
                    except Exception as e:
                        print(e.message)
                # self._save_data(data)
                self._data_format(data)

    @staticmethod
    def _save_data(data, url=None, source=None):
        temp = json.dumps(data, ensure_ascii=False, encoding='u8')
        fp.write(temp.encode('u8') + '\n')
        fp.flush()
        print(temp)

    @staticmethod
    def final_yield(data, final_data):
        final_yield = data.get(u'客户年化参考净收益率', u'')
        final_yield_1 = data.get(u'比较基准')
        final_yield_2 = data.get(u'业绩比较基准')
        if final_yield:
            final_data['lowest_yield'] = final_yield if '%' in final_yield else ''
            final_data['highest_yield'] = data.get(u'大额客户参考净收益率', u'') if data.get(u'大额客户参考净收益率', u'') else final_data[
                'lowest_yield']
        elif final_yield_1:
            if '-' in final_yield_1:
                final_data['highest_yield'] = final_yield_1.split('-')[1] if '-' in final_yield_1 else final_yield_1
                final_data['lowest_yield'] = final_yield_1.split('-')[
                                                 0] + '%' if '-' in final_yield_1 else final_yield_1
            else:
                final_data['highest_yield'] = final_data['lowest_yield'] = final_yield_1
        elif final_yield_2:
            if '-' in final_yield_2:
                final_data['highest_yield'] = final_yield_2.split('-')[1] if '-' in final_yield_2 else final_yield_2
                final_data['lowest_yield'] = final_yield_2.split('-')[
                                                 0] + '%' if '-' in final_yield_2 else final_yield_2
            else:
                final_data['highest_yield'] = final_data['lowest_yield'] = final_yield_2
        else:
            final_data['highest_yield'] = final_data['lowest_yield'] = ''

    def _data_format(self, data):
        """

        :param data:
        :param final_data:
        :return:
        """
        if data.iteritems().next()[0] != data.iteritems().next()[1]:
            final_data = {u'issue_bank': u'兴业银行'}
            final_data['product_name'] = data.get(u'产品名称')
            final_data['sales_start_date'] = data.get(u'募集起始日', u'').replace('/', '-') + ' 00:00:00' if data.get(
                u'募集起始日', u'') else ''
            final_data['sales_end_date'] = data.get(u'募集截止日', u'').replace('/', '-') + ' 00:00:00' if data.get(u'募集截止日',
                                                                                                               u'') else ''
            if not final_data['sales_start_date']:
                final_data['sales_start_date'] = data.get(u'购买时间', u'')
            final_data['value_date'] = data.get(u'收益起日期', u'').replace('/', '-')
            self.final_yield(data, final_data)
            final_data['product_status'] = u'在售'
            final_data['product_term'] = data.get(u'期限（天）/投资周期', u'')
            final_data['min_purchase_amount'] = data.get(u'起购金额(元)', u'') if data.get(u'起购金额(元)', u'') else data.get(
                u'起购金额（元）', u'')
            final_data['sales_target'] = final_data.get(u'销售对象', u'')
            final_data['sales_area'] = data.get(u'销售地区', u'')
            final_data['currency'] = data.get(u'币种', u'')
            final_data['product_nature'] = data.get(u'产品类型', u'') if u'保' in data.get(u'产品类型', u'') else ''
            final_data['product_type'] = data.get(u'产品类型', u'') if u'型' in data.get(u'产品类型', u'') else ''
            final_data['file_url'] = data.get(u'产品说明', u'')
            self._save_data(final_data)

    def main(self):
        configs = {
            'http://wealth.cib.com.cn/retail/onsale/index.html': {
                'tables': '//table',
                'titles': '//tr[1]/td',
                'tr': './/tr',
                'td': './td'
            },
            # 收益率需要点击产品名称 查看最新收益细则
            'http://wealth.cib.com.cn/retail/onsale/cash.html': {
                'tables': '//table',
                'titles': './/tbody/tr[1]/td',
                'tr': './/tr',
                'td': './/td'
            },
            'http://wealth.cib.com.cn/retail/onsale/open.html': {
                'tables': '//table',
                'titles': './/tbody/tr[1]/td',
                'tr': './/tr',
                'td': './/td'
            },
            'http://wealth.cib.com.cn/retail/onsale/wht.html': {
                'tables': '//table',
                'titles': './/tbody/tr[1]/td',
                'tr': './/tr',
                'td': './/td'
            },
            'http://wealth.cib.com.cn/retail/onsale/zyb.html': {
                'tables': '//table',
                'tr': '',
                'td': '',
                'titles': ''
            }
        }
        for url, keys_xpath in configs.iteritems():
            print(url)
            self.parse_data(self._get(url), keys_xpath)


if __name__ == '__main__':
    fp = open('products0218.txt', mode='a+')
    t = IndustrialBank()
    t.main()
    fp.close()
