# coding:utf-8
import datetime
import json
import random
import re
import time

import chardet
import requests
from lxml import etree
from lxml.etree import XMLSyntaxError
from utils.Comm import CommSession


class GuangDa():

    def __init__(self):
        self.charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
        self.pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
        self.index_url = 'https://www.cib.com.cn/cn/index.html'
        self.session = self.instance_session(self.index_url)
        self.base_url = 'http://www.cebbank.com'
        self._url_format = lambda url: self.base_url + url

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
        time.sleep(random.randint(3, 5))
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

    @staticmethod
    def products_nature_format(html, data):
        nature = ''.join(''.join(html.xpath('//ul[@class=\'fdsy_con_nr fl\']/li[4]/text()')).split())
        if not nature:
            nature = ''.join(''.join(html.xpath('//ul[@class=\'fdsy_con_nr fl\']/li[2]/text()')).split())
        data['product_nature'] = nature

    @staticmethod
    def next_open_date(html, data):
        next_open_date = ''
        date_str = '%Y年%m月%d日'
        today = datetime.datetime.now().date()
        jzxxykfr1 = html.xpath("//*[@id='jzxxykfr1']/@value")  # 开放日_1
        jzxkfr1 = html.xpath("//*[@id='jzxkfr1']/@value")  # 开放日_2
        qchkfr1 = html.xpath("//*[@id='qchkfr1']/@value")  # 开放日_3
        kfskfr1 = html.xpath("//*[@id='kfskfr1']/@value")  # 开放日_4
        kfsxykfr1 = html.xpath("//*[@id='kfsxykfr1']/@value")  # 开放日_5
        if jzxxykfr1 and u'年' in jzxxykfr1[0] and datetime.datetime.strptime(jzxxykfr1[0], date_str).date() >= today:
            next_open_date = jzxxykfr1[0]
        elif jzxkfr1 and '年' in jzxkfr1[0] and datetime.datetime.strptime(jzxkfr1[0], date_str).date() >= today:
            next_open_date = jzxkfr1[0]
        elif qchkfr1 and u'年' in qchkfr1[0] and datetime.datetime.strptime(qchkfr1[0], date_str).date() >= today:
            next_open_date = qchkfr1[0]
        elif kfskfr1 and u'年' in kfskfr1[0] and datetime.datetime.strptime(kfskfr1[0], date_str).date() >= today:
            next_open_date = kfskfr1[0]
        elif kfsxykfr1 and u'年' in kfsxykfr1[0] and datetime.datetime.strptime(kfsxykfr1[0], date_str).date() >= today:
            next_open_date = kfsxykfr1[0]
        data['next_open_date'] = next_open_date.replace(u'年', u'-').replace(u'月', '-').replace(u'日', u'')

    def parse_detail(self, data):
        # print data.get('url')
        # url = 'http://www.cebbank.com/site/gryw/yglc/lccpsj/yxl94/29834128/index.html'
        html = self.content2tree(self._coding(self._get(data.get('url'), method='get')))
        # html = self.content2tree(self._coding(self._get(url, method='get')))
        self.products_nature_format(html, data)
        data['product_type'] = ''
        file_url = ''.join(html.xpath('//div[2]/div[@class]//p/a/@href'))
        data['file_url'] = self._url_format(file_url) if file_url else ''
        # if not data.get('sales_start_date') or not data.get('sales_start_date'):
        self.next_open_date(html, data)
        # else:
        #     data['next_open_date'] = ''
        self._save_data(data)

    @staticmethod
    def final_yield_format(tr, data):
        return_yield = ''.join(''.join(tr.xpath('./td[6]/div//text()')).split())
        try:
            final_yield = return_yield[0:return_yield.index('%') + 1] if '.' in return_yield else ''
        except ValueError as e:
            print(e)
            final_yield = return_yield
        if '-' in final_yield:
            data['highest_yield'] = final_yield.split('-')[1] if '-' in final_yield else final_yield
            data['lowest_yield'] = final_yield.split('-')[0] + '%' if '-' in final_yield else final_yield
        else:
            data['highest_yield'] = data['lowest_yield'] = final_yield

    @staticmethod
    def date_format(tr, data):
        start_date = ''.join(tr.xpath('./td[3]/text()')[0].split(u'：')[1].split())
        data['sales_start_date'] = start_date + ' 00:00:00' if len(start_date) >= 9 else ''
        end_date = ''.join(tr.xpath('./td[3]/text()')[1].split(u'：')[1].split())
        data['sales_end_date'] = end_date + ' 00:00:00' if len(end_date) >= 9 else ''

    def parse_data(self, response, data):
        html = self.content2tree(response)
        trs = html.xpath('//tr[position()>1]')
        for tr in trs:
            data['product_name'] = ''.join(''.join(tr.xpath('./td[1]//text()')).strip())  # product_name
            self.date_format(tr, data)
            data['value_date'] = ''
            self.final_yield_format(tr, data)
            data['product_term'] = tr.xpath('./td[5]/text()')[0].strip()  # product_term
            data['min_purchase_amount'] = tr.xpath('./td[4]/text()')[0].strip()  # min_purchase_amount
            data['sales_target'] = ''
            data['sales_area'] = ''
            data['currency'] = tr.xpath('./td[2]/text()')[0].strip()
            data['url'] = self._url_format(''.join(''.join(tr.xpath('./td[1]/a/@href')).strip()))
            self.parse_detail(data)

    def get_page_num(self, response):
        res = re.search(pattern='class="fl">(\d+)</span> <a class=', string=response.text)
        if res:
            return res.group(1)
        raise Exception('re no match page num')

    @staticmethod
    def _save_data(data, url=None, source=None):
        temp = json.dumps(data, ensure_ascii=False)
        # fp.write(temp.encode('u8') + '\n')
        # fp.flush()
        print(temp)

    def _save_file(self, url):
        # resp = requests.get(url, stream=True)
        # self.save_file(source_stream=resp, filename='')
        pass

    def _get_channel_id(self):
        index_url = 'http://www.cebbank.com/site/gryw/yglc/lccp49/index.html'
        resp = self._get(url=index_url)
        res = re.search(pattern="Array(.+);varqgjeStr=", string=''.join(resp.text.split()))
        if res:
            return eval(res.group(1))
        raise Exception('page changed request arg get fail')

    def main(self):
        post_data = {
            "codeOrName": "",
            "TZBZMC": "",
            "SFZS": "Y",
            "qxrUp": "Y",
            "qxrDown": "",
            "dqrUp": "",
            "dqrDown": "",
            "qdjeUp": "",
            "qdjeDown": "",
            "qxUp": "",
            "qxDown": "",
            "yqnhsylUp": "",
            "yqnhsylDown": "",
            "page": "1",
            "pageSize": "5",
            "channelIds[]": self._get_channel_id()
        }
        final_data = {'issue_bank': u'光大银行'}
        url = 'http://www.cebbank.com/eportal/ui?moduleId=12073&struts.portlet.action=/app/yglcAction!listProduct.action'
        post_data['SFZS'], final_data['product_status'] = 'Y', u'在售'
        page_sale = self.get_page_num(self._get(url, method='post', post_data=post_data))
        print(page_sale)
        for i in range(1, int(page_sale) + 1):
            post_data['page'] = str(i)
            print(post_data)
            self.parse_data(self._get(url, method='post', post_data=post_data), final_data)

        post_data['SFZS'], final_data['product_status'] = 'N', u'停售'
        page_stop_sale = self.get_page_num(self._get(url, method='post', post_data=post_data))
        print(page_stop_sale)
        for i in range(1, int(page_stop_sale) + 1):
            try:
                post_data['page'] = str(i)
                print(post_data)
                self.parse_data(self._get(url, method='post', post_data=post_data), final_data)
            except Exception as e:
                # self._save_data({'error': str(e.message) + str(i)})
                print(e)


if __name__ == '__main__':
    fp = open('products0218.txt', mode='a+')
    t = GuangDa()
    t.main()
    fp.close()
