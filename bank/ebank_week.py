# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import datetime
import json
from urlparse import urljoin

from lxml import etree

from common_tools.tools import coding
from policy.common_tools.common_requests import CommonRequests


class EBankZZC(object):
    def __init__(self):
        self.topic_id = ''

    def main(self):
        """
        入口
        :return:
        """
        url = 'http://www.cebbank.com/site/gryw/grck/66885726/index.html'
        resp = CommonRequests().retry_download_page(url)
        resp = coding(resp)
        for list_url in self.parse_list(resp.text, resp.url):
            resp = CommonRequests().retry_download_page(list_url)
            resp = coding(resp)
            datas = self.parse_detail(resp.text, list_url)
            self.save_data(datas=datas)

    @staticmethod
    def parse_list(content, cur_url):
        """
        解析列表页
        :param content:str 列表页内容
        :param cur_url:str  列表页url
        :return: urls:list 详情页url
        """
        html = etree.HTML(content)
        items = html.xpath('//div[@id=\'grcx_r\']//li/div[@class=\'gg_nr fl\']/a')
        urls = []
        for item in items:
            if '产品公告' in item.xpath('string(./text())'):
                urls.append(urljoin(cur_url, item.xpath('string(./@href)')))
        return urls

    @staticmethod
    def date_format(date):
        """
        日期格式化
        :return:date:str 格式化后的日期
        """
        # 20200529	-> 2020-05-29 00:00:00
        return date[:4] + '-' + date[4:6] + '-' + date[6:] + ' 00:00:00'

    def parse_detail(self, content, cur_url=None):
        """
        解析详情页
        :param content: str 详情页内容
        :param cur_url: str 详情页url
        :return: datas: list 解析后详情页数据
        """
        html = etree.HTML(content)
        items = html.xpath('//div[@class=\'gd_xilan\']//tr[position()>1]')
        datas = []
        for item in items:
            data = dict()
            data['issue_bank'] = '光大银行'
            data['product_name'] = '周周存'
            data['currency'] = item.xpath('string(./td[2])')
            data['value_date'] = self.date_format(item.xpath('string(./td[3])'))
            data['product_status'] = ''
            data['lowest_yield'] = item.xpath('string(./td[5])').split('-')[0]
            data['highest_yield'] = item.xpath('string(./td[5])').split('-')[1]

            data['product_number'] = item.xpath('string(./td[1])')
            data['value_pay_date'] = self.date_format(item.xpath('string(./td[4])'))
            data['observation_date'] = self.date_format(item.xpath('string(./td[6])'))
            data['product_mark'] = item.xpath('string(./td[7])')
            data['change_rate'] = item.xpath('string(./td[8])')
            data['desc_income_measure'] = item.xpath('string(./td[9])')
            datas.append(data)

        return datas

    def save_data(self, datas):
        for data in datas:
            fp.write(json.dumps(data, encoding='u8', ensure_ascii=False) + '\n')
            # self.save_topic_data(data.get('product_number'), data, self.topic_id)


if __name__ == '__main__':
    with open('./data{}.txt'.format(str(datetime.date.today())), mode='a+') as fp:
        t = EBankZZC()
        t.main()
