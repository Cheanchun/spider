# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:20200629
@Desc:
@Todo
"""
import json

import requests
from lxml import etree


class ICBCBigDeposit(object):
	def __init__(self):
		self.url = 'https://mybank.icbc.com.cn/servlet/ICBCBaseReqServletNoSession'
		self.params = {
			'dse_operationName': 'per_accountQueryFixedProductsOutOp',
			'cmd': '0',
			'NormalOrBooking': '0',
			'IN_CURRFLAG': '',
			'IN_APPID': '02',
			'IN_SAVETYPE': '',
			'IN_BIGFLAG': '1',
			'JJGFLAG': '0',
			'Area_code': '1001',
		}
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
		}

	def page_download(self, url, params):
		resp = requests.get(url, params=params, headers=self.headers)
		if resp.status_code // 100 == 2:
			return resp
		else:
			print 'page download fail'
			return None

	@staticmethod
	def coding(response):
		return response

	def data_parse(self, content, url):
		html = etree.HTML(content)
		items = html.xpath('//div[@class="ebdp-pc4promote-circularcontainer-wrapper"]')
		for item in items:
			data = {'issue_bank': '工商银行'}
			data['product_name'] = item.xpath('string(.//span[@class="ebdp-pc4promote-circularcontainer-head-left"])')
			data['highest_yield'] = item.xpath('string(.//a[@class="trcontent"])') + '%'
			data['lowest_yield'] = item.xpath('string(.//a[@class="trcontent"])') + '%'
			data['min_purchase_amount'] = item.xpath('string(.//tr/td[@class="trcontent"]/text())')
			data['url'] = url + data.get('product_name')
			self.save_data(data)

	def save_data(self, data):
		# self.save_topic_data(data.pop(url), data, self.topic_id)
		print json.dumps(data, ensure_ascii=False, encoding='u8')

	def main(self):
		try:
			res = self.page_download(self.url, self.params)
			if res:
				self.data_parse(self.coding(res).text, res.url)
		except requests.exceptions as ex:
			print ex


if __name__ == '__main__':
	c = ICBCBigDeposit()
	c.main()
