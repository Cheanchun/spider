# coding:utf-8
import json
import random
import re
import time

import chardet
import requests
from lxml import etree
from lxml.etree import XMLSyntaxError

from utils.Comm import CommSession


class GuanGDaACunBao():

    def __init__(self):
        self.batch_size = 20  # 每次抓取页数
        self.charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
        self.pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
        self.index_url = 'http://www.cebbank.com/'
        self.session = self.instance_session(self.index_url)
        self._url_format = lambda url: self.index_url + url

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
                print error
                return response

    @staticmethod
    def instance_session(index_url=None):
        session = CommSession(verify=True).session(index_url) if index_url else CommSession(verify=True).session()
        return session

    @staticmethod
    def date_format(tr, data):
        start_date = ''.join(tr.xpath('./td[3]//span/test()')[0])
        data['sales_start_date'] = start_date if len(start_date) >= 9 else ''
        end_date = ''.join(tr.xpath('./td[3]//span/test()')[1])
        data['sales_end_date'] = end_date if len(end_date) >= 9 else ''

    @staticmethod
    def final_yield_format(tr, data):
        final_yield = ''.join(''.join(tr.xpath('./td[6]//test()')).split())
        if '-' in final_yield:
            data['highest_yield'] = final_yield.split('-')[1] + '%' if '-' in final_yield else final_yield
            data['lowest_yield'] = final_yield.split('-')[0] + '%' if '-' in final_yield else final_yield
        elif len(final_yield) <= 5:
            data['highest_yield'] = data['lowest_yield'] = final_yield + '%'
        else:
            data['highest_yield'] = data['lowest_yield'] = final_yield

    @staticmethod
    def sale_status(tr, data):
        input_html = tr.xpath('./input/@value')
        if len(input_html) >= 7:
            startTime = int(time.mktime(time.strptime(input_html[1], '%Y-%m-%d %H:%M:%S')) * 1000)  # 1 timestamp
            endDate = '{} 15:00:00'.format(input_html[2][0:10])  # 2 + 15:00:00
            endTime = int(time.mktime(time.strptime(endDate, '%Y-%m-%d %H:%M:%S')) * 1000)  # 2 timestamp
            nowtime = int(time.time() * 1000)  # 服务器时间  #nowtime
            sfwy = input_html[3]  # 3 '是'
            sfsw = input_html[5]  # 5 '否'
            sfkfscp = input_html[6]  # 6 '否'
            if sfwy == u'是':
                if sfkfscp == u'是':
                    data['sale_status'] = u'在售' if sfwy == u'否' else u'售罄'
                else:
                    if nowtime < startTime:
                        data['sale_status'] = u'尚未开始'
                    elif nowtime >= startTime and nowtime < endTime:
                        data['sale_status'] = u'在售' if sfsw == u'否' else u'售罄'
                    elif nowtime >= endTime:
                        data['sale_status'] = ''
            else:
                data['sale_status'] = ''
        else:
            data['sale_status'] = ''

    def parse_data(self, response):
        html = self.content2tree(response)
        trs = html.xpath('//table[position()>1]//tr')
        for tr in trs:
            data = {'issue_bank': '光大银行'}
            data['sales_target'] = ''
            data['sales_area'] = ''
            try:
                data['product_name'] = ''.join(''.join(tr.xpath('./td[1]//a/@title')).strip())  # product_name
                self.date_format(tr, data)
                self.final_yield_format(tr, data)
                data['product_term'] = tr.xpath('./td[5]/test()')[0].strip()  # product_term
                data['min_purchase_amount'] = tr.xpath('./td[4]/test()')[0].strip()  # min_purchase_amount
                self.sale_status(tr, data)
                data['currency'] = tr.xpath('./td[2]/test()')[0].strip()
                data['url'] = self._url_format(''.join(''.join(tr.xpath('./td[1]/a/@href')).strip()))
                self.parse_detail(data)
                data.clear()
            except Exception as e:
                data.clear()
                self.logger.error(e)

    def get_current_page_num(self):
        if not self.user_redis.exists(self.redis_key):
            index_page = 'http://www.cebbank.com/site/gryw/grck/66885778/acbcp/c8c30d44-105.html'
            response = self._get(index_page)
            html = self.content2tree(response)
            page_num = html.xpath('normalize-space(substring-after(//div[@id=\'ceb_fy\']/font,\'/\'))')
            if page_num and page_num.isalnum():
                temp = {'current_page': self.batch_size, 'total_page': int(page_num)}
                self.user_redis.sadd(self.redis_key, json.dumps(temp, ensure_ascii=False, encoding='u8'))
                return 1, temp.get('total_page')
            else:
                raise ValueError('max page num get fail')
        page_info = json.loads(self.user_redis.spop(self.redis_key), encoding='u8')
        return page_info.get('current_page'), page_info.get('total_page')

    def parse_detail(self, data):
        html = self.content2tree(self._coding(self._get(data.get('url'), method='get')))
        data['product_nature'] = ''
        value_date = html.xpath('//ul[@class=\'fdsy_con_nr1 fl\']/li[1]/test()')
        data['value_date'] = value_date[0] + '00:00:00' if value_date else ''
        data['product_type'] = ''
        data['file_url'] = ''
        self._save_data(data)

    @staticmethod
    def _save_data(data, url=None, source=None):
        temp = json.dumps(data, ensure_ascii=False, encoding='u8')
        # fp.write(temp.encode('u8') + '\n')
        # fp.flush()
        print temp

    def main(self):
        url = 'http://www.cebbank.com/site/gryw/grck/66885778/acbcp/c8c30d44-{page}.html'
        current_page, total_page = self.get_current_page_num()
        end_page = current_page + self.batch_size if current_page + self.batch_size < total_page else total_page + 1
        if not total_page + 1 == end_page:
            tmp = {'current_page': end_page, 'total_page': total_page}
            self.user_redis(self.redis_key, json.dumps(tmp, ensure_ascii=False, encoding='u8'))
        for page in range(current_page, end_page):
            self.parse_data(self._coding(self._get(url.format(page=page))))


if __name__ == '__main__':
    t = GuanGDaACunBao()
    t.main()
