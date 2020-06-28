# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import requests

from policy.chrome_handle import ChromeHandle

sel_config = {
	'chrome_init': ['acceptSslCerts'],
	'proxy_type': '',

}

"http://www.ccb.com/tran/WCCMainPlatV5"
"""
CCB_IBSVersion=V5
isAjaxRequest=true
SERVLET_NAME=WCCMainPlatV5
TXCODE=JGH001&BsPD_Cd=001&Sel_StCd=2
Sale_Inst_ECD=110000000&CorpPrvt_Cd=1
PAGE_JUMP=1&REC_IN_PAGE=10

"""
headers = {
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
		self.session.headers = headers

	def get_cookies(self):
		driver = ChromeHandle(config=sel_config)
		driver.get_page('http://www.ccb.com/cn/finance/deposit_products.html', waiting={'by_id': 'deposit_list'})
		return driver.cookie_jar

	def main(self):
		list_url = 'http://www.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5'
		list_params = {
			"isAjaxRequest": "true",
			"SERVLET_NAME": "WCCMainPlatV5",
			"TXCODE": "JGH001",
			"BsPD_Cd": "001",
			"Sel_StCd": "2",
			"Sale_Inst_ECD": "110000000",
			"CorpPrvt_Cd": "1",
			"PAGE_JUMP": "1",
			"REC_IN_PAGE": "10",
		}
		self.session.cookies = self.get_cookies()
		resp = self.session.get(list_url, params=list_params)
		'http://www.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&isAjaxRequest=true&SERVLET_NAME=WCCMainPlatV5&TXCODE=JGH001&BsPD_Cd=001&Sel_StCd=2&Sale_Inst_ECD=110000000&CorpPrvt_Cd=1&PAGE_JUMP=1&REC_IN_PAGE=10'
		self.page_list_data(resp.text)

	def page_list_data(self, content):
		print content
		"http://www.ccb.com/cn/finance/deposit_product_detail.html?IvsmPd_Cd=ZHJGX202006236001&Sale_Inst_ECD=111111111"


if __name__ == '__main__':
	a = CCBStructure()
	a.main()
