# coding=utf-8
import datetime
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


class GuangDaRate():
    def __init__(self):
        self.index_page = 'http://www.cebbank.com/'
        self.post_url = 'http://www.cebbank.com/eportal/ui?moduleId=12073&struts.portlet.action=/app/yglcAction!listProduct.action'
        self.TOPIC_ID = ''
        self.session = self.instance_session()
        self.charset_re = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
        self.pragma_re = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
        self.channel = self._get_channel_id()
        self.product_xpath = u'//*[contains(text(),"{}")]/@href'
        self.detail_xpath = u'//*[contains(text(),\'历史业绩\')]/following-sibling::div//@href'
        self.table_xpath = u'//table'
        self.max_page = 1

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

    def queryApi(self, p_code):
        url = 'http://www.cebbank.com/eportal/ui?moduleId=12073&struts.portlet.action=/app/yglcAction!getLsjz.action'
        post_data = {'cpcode': p_code
                     }
        return self._get(url, method='post', post_data=post_data)

    def _coding(self, response):
        if self.charset_re.findall(response.text):
            response.encoding = self.charset_re.findall(response.text)[0]
        elif self.pragma_re.findall(response.text):
            response.encoding = self.charset_re.findall(response.text)[0]
        else:
            temp = chardet.detect(response.content)
            response.encoding = temp['encoding']
        return response

    def _get_channel_id(self):
        index_url = 'http://www.cebbank.com/site/gryw/yglc/lccp49/index.html'
        resp = self._get(url=index_url)
        res = re.search(pattern='Array(.+);varqgjeStr=', string=''.join(resp.text.split()))
        if res:
            return eval(res.group(1))
        raise Exception('page changed request arg get fail')

    def _save_data(self, data, url=''):
        # self.save_topic_data(url, data, self.TOPIC_ID)
        temp = json.dumps(data, ensure_ascii=False, encoding='u8')
        fp.write(temp.encode('u8') + '\n')
        fp.flush()
        print temp

    def _get_product_name(self, page_num=1):
        post_data = {'sylxArr[]': '02', 'SFZS': '', 'qxrUp': 'Y', 'page': page_num, 'pageSize': '12',
                     'channelIds[]': self.channel}
        html = self.content2tree(self._coding(self._get(self.post_url, method='post', post_data=post_data)))
        max_page = html.xpath('string(//span[contains(@id,\'totalpage\')])')
        self.max_page = int(max_page) if max_page and str(max_page).isalnum() else 1
        names = html.xpath('//div[@class=\'lccp_main_content_tx\']//li/a/@title')
        product_name = []
        for name in names:
            try:
                temp = name.split(u'(')
                p_name = temp[0], temp[1][:-1] if len(temp) == 2 else ''
                product_name.append(p_name)
            except Exception as e:
                print e
        return product_name

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

    def main(self):
        flag = 1
        while flag:
            print 'current page:%s' % flag
            for p_name, p_code in self._get_product_name(flag):
                print p_name,p_code
                datas = self._coding(self.queryApi(p_code)).json()
                product_name = datas.get('cpname')
                for data in datas.get('lsjzMap'):
                    data['product_name'] = product_name
                    self._save_data(data)
            flag += 1
            if flag > self.max_page:
                flag = 0


if __name__ == '__main__':
    fp = open('guangda_rate{}'.format(str(datetime.date.today())), mode='w')
    t = GuangDaRate()
    t.main()
    fp.close()
