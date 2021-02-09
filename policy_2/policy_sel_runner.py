# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:20200601
@Desc:
@Todo
"""
import random
import sys

import redis

from formatter import Formatter
from parser_ import Parser
from policy_module.configuration import ATTACH_RE

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('/home/work/data/crawler3/crawler3_py/develop_jobs')
import json
import os
import re
from urlparse import urljoin

import requests

from common_tools.chrome_handle import ChromeHandle

from sel_config import config

# from api_develop.develop_job_base import DevelopJobBase

DEFAULT_HEADERS = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
BASE_PATH = u'/home/work/data/crawler3/crawler3_py/develop_jobs/policy/files'
CHARSET_RE = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
PRAGMA_RE = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
redis_info = {'host': '47.105.54.129', 'port': 6388, 'password': 'admin'}
FILE_URL = 'http://www.policy_all.com'


class SeleniumPolicySpider():
	def __init__(self):
		# super(SeleniumPolicySpider, self).__init__()
		self.website = ''
		self.category = ''
		self.handler = ''
		self.chrome_handel = ''
		self.parser = ''
		self.driver = ''
		self.file_download_path = ''
		self.user_redis = redis.Redis(**redis_info)
		self.config_redis_key = 'macropolicy'
		self.topic_id = 'b31d8e04-eba3-4670-969a-ead93d27464e'

	def get_config(self):
		if not self.user_redis.exists(self.config_redis_key):
			random.shuffle(config)
			for item in config:
				self.user_redis.sadd(self.config_redis_key, json.dumps(item, encoding='u8', ensure_ascii=False))
		return json.loads(self.user_redis.spop(self.config_redis_key), encoding='u8')

	def page_handle(self, cur_url):
		urls = [{'title': item.get('title'), 'url': urljoin(cur_url, item.get('url'))} for item in
				self.parser.parse_list(self.driver.page_source)]
		content_urls, file_urls = self.check_list_url_type(urls)
		js = 'window.open();'
		self.driver.execute_script(js)
		self.driver.switch_to.window(self.driver.window_handles[1])
		if not content_urls and not file_urls:
			self.user_redis.lpush('policy_selenium_test', cur_url + '\n' + self.chrome_handel.page_source)
		for item in content_urls:
			try:
				self.chrome_handel.get_page(item.get('url'), timeout=1)
				self.chrome_handel.headless_break()
				self.check_page(self.chrome_handel.page_source, item.get('url'))
				file_urls.extend(self.parser.parse_content(self.chrome_handel.page_source, item.get('url')))
				l_url, l_title = item.get('url') or item.get('attach_url'), item.get('title') or item.get(
					'attach_title')
				self.data_format(l_url, l_title, self.driver.page_source, self.parser)
			except Exception as ex:
				# self.logger.error(ex)
				print ex

		if len(self.driver.window_handles) > 1:
			self.driver.switch_to.window(self.driver.window_handles[-1])
			self.driver.close()
		self.driver.switch_to.window(self.driver.window_handles[0])
		if file_urls:
			session, session.headers = requests.Session(), {'User-Agent': self.chrome_handel.user_agent}
			session.cookies = self.chrome_handel.cookie_jar
			for item in file_urls:
				f_url = item.get('url') or item.get('attach_url')
				f_title = item.get('url') or item.get('attach_title')

				self.file_download(session.get(f_url, stream=True), f_url, f_title)


	def file_download(self, resp, url, file_name):
		# self.save_file(resp, file_name, url)
		print resp.status_code, url, file_name.decode('u8')

	def check_page(self, content, url):
		if len(content) < 100:
			self.chrome_handel.delete_cookies()
			# self.chrome_handel.restart_chrome()
			self.chrome_handel.get_page(url)

	@staticmethod
	def check_list_url_type(urls):
		file_urls = []
		content_urls = []
		for item in urls:
			if ATTACH_RE.search(item.get('url')):
				file_urls.append({'title': item.get('title'), 'url': item.get('url')})
			else:
				content_urls.append({'title': item.get('title'), 'url': item.get('url')})
		return content_urls, file_urls

	def main(self):
		conf = self.get_config()
		sel_config = conf.get('sel_config')
		site_config = conf.get('site_config')
		index_url = site_config.get('index_url')
		print 'crawler url:', index_url
		self.file_download_path = urljoin(BASE_PATH, 'policy_all_file/')
		if not os.path.exists(self.file_download_path):
			os.makedirs(self.file_download_path)
		self.website, self.category = site_config.get('website'), site_config.get('category')
		self.handler = site_config.get('handler')
		self.parser = Parser('xpath', site_config.get('list_parse_rule'), content_format='')
		self.chrome_handel = ChromeHandle(sel_config, self.file_download_path)
		self.driver = self.chrome_handel.driver
		self.chrome_handel.headless_break()
		try:
			page = site_config.get('total_page', 0) if not self.user_redis.exists(site_config.get('redis_key')) else 2
			if self.chrome_handel.get_page(index_url):
				self.page_handle(self.chrome_handel.current_url)
				for _ in range(1, page):
					if self.chrome_handel.click_element(**sel_config.get('next_page_btn')):
						self.page_handle(self.chrome_handel.current_url)
				self.user_redis.set(site_config.get('redis_key'), 'true')
		# self.save_location_file()  #todo linux 默认下载路径
		except Exception as e:
			# self.save_location_file()  #todo linux 默认下载路径
			self.user_redis.set(site_config.get('redis_key'), 'error')
			print e
		del self.chrome_handel
	# self.logger.error(e)

	def data_format(self, current_url, title, response, parse):
		formatter = Formatter(self.website, self.category, self.handler, parse)
		data = formatter.format_data(current_url, title, response)
		print 'data len:', len(json.dumps(data, ensure_ascii=False, encoding='u8'))

	# self.save_topic_data(current_url, data, self.topic_id)

	def save_location_file(self):
		files = os.listdir(self.file_download_path)
		for _file in files:
			print 'location files'
			file_path = os.path.join(self.file_download_path, _file)
			source_url = urljoin(FILE_URL, _file)
			# self.save_file(open(file_path, mode='rb'), _file, source_url=source_url)
			print 'file_path:', file_path, 'file_name', _file, 'source_url', source_url
		# shutil.rmtree(self.file_download_path)


if __name__ == '__main__':
	t = SeleniumPolicySpider()
	t.main()
