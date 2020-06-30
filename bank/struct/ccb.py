# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:20200629
@Desc:
@Todo
"""
import json

import requests

from policy.chrome_handle import ChromeHandle

sel_config = {
	'chrome_init': ['acceptSslCerts'],
	'proxy_type': '',

}
KEYS = [
	'issue_bank', 'sales_target', 'sales_area', 'product_name', 'product_name', 'product_term', 'product_type',
	'min_purchase_amount', 'currency', 'url', 'product_nature', 'value_date', 'expire_date', 'increase_amount',
	'highest_yield', 'lowest_yield', 'file_url', 'sales_start_date', 'sales_end_date'
]
HEADERS = {
	"Accept": "application/json, text/javascript, */*; q=0.01",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
	"Cache-Control": "no-cache",
	"Connection": "keep-alive",
	"Host": "www.ccb.com",
	"Pragma": "no-cache",
	"Referer": "http://www.ccb.com/cn/finance/deposit_products.html",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest",
}


class CCBStructure(object):
	def __init__(self):
		self.session = requests.Session()
		self.session.headers = HEADERS
		self.max_page = 1
		self.index_page = 'http://www.ccb.com/cn/finance/deposit_products.html'

	def get_cookies(self):
		driver = ChromeHandle(config=sel_config)
		driver.get_page(self.index_page, waiting={'by_id': 'deposit_list'})
		return driver.cookie_jar

	@staticmethod
	def date_format(source_date):
		"""
		日期格式化
		eg ： 20200629 -> 2020-06-29 00:00:00
		:param source_date:
		:return:
		"""
		return source_date[:4] + '-' + source_date[4:6] + '-' + source_date[6:] + ' 00:00:00'

	def page_download(self, list_url, list_params):
		self.session.cookies = self.get_cookies()
		resp = self.session.get(list_url, params=list_params)
		self.max_page = int(resp.json().get('TOTAL_PAGE'))
		return resp

	def main(self):
		list_url = 'http://www.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5'
		list_params = {
			"isAjaxRequest": "true",
			"SERVLET_NAME": "WCCMainPlatV5",
			"TXCODE": "JGH001",
			"BsPD_Cd": "001",
			"Sel_StCd": "2",
			"Sale_Inst_ECD": "111111111",
			"CorpPrvt_Cd": "1",
			"PAGE_JUMP": "1",
			"REC_IN_PAGE": "10",
		}
		try:
			res = self.page_download(list_url, list_params)
			self.page_list_data(res.json(), res.url)
		except requests.exceptions as ex:
			print ex
			exit()
		for page in range(2, self.max_page + 1):
			try:
				list_params["PAGE_JUMP"] = str(page)
				res = self.page_download(list_url, list_params)
				self.page_list_data(res.json(), res.url)
			except requests.exceptions as ex:
				print ex

	def page_list_data(self, content, url):
		# print 'total_page', self.max_page
		data_list = content.get('PROD_INFO_GRP')
		for item in data_list:
			source_dict = Dict(item)
			data = Dict(KEYS)
			data.product_name = source_dict.ChmtPd_Nm
			data.product_term = source_dict.Ivs_Trm
			data.sale_start_date = self.date_format(source_dict.Rs_StDt)
			data.sale_end_date = self.date_format(source_dict.Rs_EdDt)
			data.min_purchase_amount = source_dict.PerTxn_Num_LwrLmt_Val
			data.url = url + source_dict.IvsmPd_Cd
			data.setup_date = self.date_format(source_dict.Ivs_StDt)
			data.expire_date = self.date_format(source_dict.Ivs_CODt)
			data.file_url = source_dict.Web_Acs_Rsc_URL
			data.currency = u'人民币' if source_dict.CcyCd == '156' else u'其他'
			data.highest_yield = source_dict.PfCmpBss.split('-')[-1]
			data.lowest_yield = source_dict.PfCmpBss.split('-')[0]
			self.save_data(data)
			print json.dumps(data, encoding='u8', ensure_ascii=False)

	def save_data(self, data):
		# self.save_topic_data(data.pop('url'), data, self.topic_id)
		pass


class Dict(dict):

	def __init__(self, _map=None, **kw):
		super(dict, self).__init__(**kw)
		if isinstance(_map, list):
			for key in _map:
				self[key] = ''
			self.issue_bank = '建设银行'
		if isinstance(_map, dict):
			self.__recursion_setval__(_map)

	def __recursion_setval__(self, _map):
		for k, v in _map.iteritems():
			if isinstance(v, dict):
				self.__recursion_setval__(v)
			elif isinstance(v, list):
				for item in v:
					self.__recursion_setval__(item)
			else:
				self[k] = v

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			return None

	def __setattr__(self, key, value):
		self[key] = value


if __name__ == '__main__':
	a = CCBStructure()
	a.main()
# d = Dict({'a': {'5': 1}, 'b': 45, 'l': [{'2': 4, '7': 0}]})
# print d
