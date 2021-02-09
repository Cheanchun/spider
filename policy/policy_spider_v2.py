# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:20200601
@Desc:
@Todo
"""
import cookielib
import json
import os
import random
import re
import time
import traceback
import warnings
from urlparse import urljoin, urlparse

import pymongo
import redis
import requests
from requests.cookies import RequestsCookieJar
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By  # 选择方法
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待

from common_tools.tools import get_abuyun_proxy, get_zhima_proxy
from policy.formatter import Formatter
from policy.parser import Parser
from policy.policy_module.configuration import ATTACH_RE
# from policy.config_v2 import sel_config
from policy.sel_config import config

DEFAULT_HEADERS = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
BASE_PATH = u'./files/'
REDIS_CONFIG = {'host': '47.105.54.129', 'port': 6388, 'password': 'admin'}
CHARSET_RE = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
PRAGMA_RE = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
WEB_DRIVER_PATH = ''
mongo_config = {'host': '47.105.54.129', 'port': 27017}
cnn = pymongo.MongoClient(**mongo_config)
db = cnn['shixin']
db.authenticate(name='chean', password='scc57295729')
col = db['zcjd']


class ChromeHandle(object):
    def __init__(self, selenium_config, file_download_path=None):
        assert isinstance(selenium_config, dict)
        self.selenium_config = selenium_config
        self.file_download_path = file_download_path
        self.proxy = selenium_config.get('proxy_type', '')
        self.chrome_init = selenium_config.get('chrome_init', [])
        self.driver = self._open_chrome(self.chrome_init)
        self.driver.implicitly_wait(selenium_config.get('implicitly_wait', 30))  # 隐式等待
        self.driver.set_page_load_timeout(selenium_config.get('load_timeout', 30))  # 页面加载等待
        self.user_redis = redis.Redis(**REDIS_CONFIG)
        self.redis_key = selenium_config.get('redis_key')

    def _wait_page(self, timeout=2, try_times=3, **kwargs):
        """
        waiting page until some element is available
        :param timeout:超时
        :param try_times:尝试次数
        :param kwargs:
        :return:
        """
        waiting = WebDriverWait(self.driver, timeout)
        flag = False
        for i in range(try_times):
            try:
                if kwargs.get('by_xpath'):
                    flag = waiting.until(EC.presence_of_all_elements_located((By.XPATH, kwargs.get('by_xpath'))))
                elif kwargs.get('by_id'):
                    flag = waiting.until(EC.presence_of_element_located((By.ID, kwargs.get('by_id'))))
                elif kwargs.get('by_class'):
                    flag = waiting.until(EC.presence_of_all_elements_located((By.CLASS_NAME, kwargs.get('by_class'))))
                else:
                    time.sleep(timeout)
                    return True
            except TimeoutException:
                time.sleep(random.randint(1, 2))
                self.driver.refresh()
            if flag:
                return flag
            else:
                warnings.warn('Element Not Find,please check the element is available')
        return flag

    def _open_chrome(self, init):
        """
        open chrome
        :return: driver
        """
        print init
        options = webdriver.ChromeOptions()
        if self.proxy:
            self.proxy = self._get_proxy(self.proxy)
            print(self.proxy)
            options.add_argument("--proxy-server={}".format(self.proxy.get("http") or self.proxy.get("https")))
        options.add_argument('window-size=1080x720')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        if self.file_download_path:
            pfs = {'profile.default_content_settings.popups': 0, 'download.default_directory': self.file_download_path}
            options.add_experimental_option('prefs', pfs)  # todo 三期 本地文件存储路径
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument("--headless")  # todo headless
        options.add_argument("--user-agent={}".format(DEFAULT_HEADERS))
        if init and isinstance(init, list):
            c = DesiredCapabilities.CHROME.copy()
            for item in init:
                if item == 'acceptSslCerts':
                    c['acceptSslCerts'] = True
                    c['acceptInsecureCerts'] = True
                options.add_argument(item)
            return webdriver.Chrome(chrome_options=options, desired_capabilities=c)
            # return webdriver.Chrome(chrome_options=options, desired_capabilities=c, executable_path=WEB_DRIVER_PATH)
        return webdriver.Chrome(chrome_options=options)
        # return webdriver.Chrome(chrome_options=options, executable_path=WEB_DRIVER_PATH)

    @staticmethod
    def _get_proxy(proxy_type='abuyun'):
        if proxy_type == 'abuyun':
            return get_abuyun_proxy()
        elif proxy_type == 'duobeiyun':
            pass  # todo add
        elif proxy_type == 'zhima':
            return get_zhima_proxy()
        else:
            raise TypeError('no such proxy type,please check the proxy type')

    @property
    def current_url(self):
        return self.driver.current_url

    def get_page(self, url, timeout=10, try_times=3):
        try:
            self.driver.get(url)
        except TimeoutException as ex:
            warnings.warn(ex.msg)
            self.restart_chrome(init=self.chrome_init)
            self.driver.get(url)
        return self._wait_page(timeout=timeout, try_times=try_times, **self.selenium_config)

    def restart_chrome(self, init=None):
        print 'chrome restarting ...'
        self.driver.quit()
        self.driver = self._open_chrome(init) if init else self._open_chrome(self.chrome_init)
        print 'chrome start finish ...'

    @property
    def cookies_dict(self):

        return {item.get('name'): item.get('value') for item in self.driver.get_cookies()}

    @staticmethod
    def create_cookie(name, value, **kwargs):
        """Make a cookie from underspecified parameters.

        By default, the pair of `name` and `value` will be set for the domain ''
        and sent on every request (this is sometimes called a "supercookie").
        """
        result = {
            'version': 0,
            'name': name,
            'value': value,
            'port': None,
            'domain': '',
            'path': '/',
            'secure': False,
            'expires': None,
            'discard': True,
            'comment': None,
            'comment_url': None,
            'rest': {'HttpOnly': None},
            'rfc2109': False,
        }

        badargs = set(kwargs) - set(result)
        if badargs:
            err = 'create_cookie() got unexpected keyword arguments: %s'
            raise TypeError(err % list(badargs))

        result.update(kwargs)
        result['port_specified'] = bool(result['port'])
        result['domain_specified'] = bool(result['domain'])
        result['domain_initial_dot'] = result['domain'].startswith('.')
        result['path_specified'] = bool(result['path'])

        return cookielib.Cookie(**result)

    @property
    def cookie_jar(self, overwrite=True):
        cookiejar = RequestsCookieJar()
        names_from_jar = [cookie.name for cookie in cookiejar]
        cookie_dict = self.cookies_dict
        for name in cookie_dict:
            if overwrite or (name not in names_from_jar):
                cookiejar.set_cookie(self.create_cookie(name, cookie_dict[name]))
        return cookiejar

    @property
    def get_driver(self):
        return self.driver

    def delete_cookies(self):
        self.driver.delete_all_cookies()

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)

    @property
    def page_source(self):
        return self.driver.page_source

    def close_chrome(self):
        self.driver.quit()  # todo quit 会有错误
        print 'chrome close'

    @property
    def user_agent(self):
        return self.driver.execute_script('return navigator.userAgent')

    def click_element(self, by_class='', by_xpath='', by_id='', **kwargs):
        try:
            element = self.find_elements(by_class=by_class, by_xpath=by_xpath, by_id=by_id, **kwargs)
            if element:
                element.click()
                return self._wait_page(**self.selenium_config.get('waiting_page', {}))
            return False
        except Exception as ex:
            print traceback.format_exc()
            return False

    def roll_page(self):
        pass  # todo

    def find_elements(self, by_class='', by_xpath='', by_id='', **kwargs):
        assert by_id or by_xpath or by_class
        try:
            if by_class:
                element = self.driver.find_element_by_class_name(by_class)
            elif by_xpath:
                element = self.driver.find_element_by_xpath(by_xpath)
            elif by_id:
                element = self.driver.find_element_by_id(by_id)
            else:
                raise KeyError('please check selector is available')
            return element
        except NoSuchElementException:
            print 'element not find in this page'

    def box_input(self, text, by_class='', by_xpath='', by_id='', **kwargs):
        assert text and (by_id or by_xpath or by_class)
        elements = self.find_elements()
        # todo query box input

    def __del__(self):
        self.close_chrome()


class SeleniumPolicySpider(object):
    def __init__(self):
        self.website = ''
        self.category = ''
        self.handler = ''
        self.chrome_handel = ''
        self.parse = ''
        self.driver = ''
        self.config_redis_key = 'macropolicy'
        self.user_redis = redis.Redis(**REDIS_CONFIG)

    def get_config(self):
        if not self.user_redis.exists(self.config_redis_key):
            for item in config:
                self.user_redis.sadd(self.config_redis_key, json.dumps(item, encoding='u8', ensure_ascii=False))
        return json.loads(self.user_redis.spop(self.config_redis_key), encoding='u8')

    def page_handle(self, cur_url):
        urls = [{'title': item.get('title'), 'url': urljoin(cur_url, item.get('url'))} for item in
                self.parse.parse_list(self.driver.page_source)]
        content_urls, file_urls = self.check_list_url_type(urls)
        js = 'window.open();'
        self.driver.execute_script(js)
        self.driver.switch_to.window(self.driver.window_handles[1])
        if not content_urls and not file_urls:
            te = self.file_download_path + '/' + ''.join(i if i.strip() else '' for i in self.category.split('>'))
            print te
            with open(te, mode='a+') as fp:
                fp.write(self.chrome_handel.current_url + '\n' + self.chrome_handel.page_source)
        for item in content_urls:
            try:
                self.driver.get(item.get('url'))  # todo 此处可能报错
                self.check_page(self.chrome_handel.page_source, item.get('url'))
                file_urls.extend(self.parse.parse_content(self.chrome_handel.page_source, item.get('url')))
                l_url, l_title = item.get('url') or item.get('attach_url'), item.get('title') or item.get(
                    'attach_title')
                self.data_format(l_url, l_title, self.driver.page_source, self.parse)
            except Exception as ex:  # todo 精确捕捉
                continue
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
                self.file_download(session.get(f_url), f_url, f_title)
                print item.get('attach_title'), item.get('attach_url').decode('u8')
                # pass  # todo 附件下载

    def file_download(self, resp, url, file_name):
        print resp.status_code, url, file_name.decode('u8')
        # file_path = os.path.join(BASE_PATH, urlparse.urlparse(url).netloc)
        # if not os.path.exists(file_path):
        #     os.mkdir(file_path)
        # with open(os.path.join(file_path, file_name), mode='wb') as fp:
        #     fp.write(resp.content)

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
        file_download_path = urljoin(BASE_PATH, urlparse(index_url).netloc)
        self.file_download_path = file_download_path
        # print self.file_download_path,file_download_path
        if not os.path.exists(file_download_path):
            print 'file path', file_download_path
            os.makedirs(file_download_path)
        self.website, self.category = site_config.get('website'), site_config.get('category')
        self.handler = site_config.get('handler')
        self.parse = Parser(list_parse_type='xpath', list_parse_rule=site_config.get('list_parse_rule'),
                            content_format='')
        self.chrome_handel = ChromeHandle(sel_config, file_download_path)  # todo file_download_path
        self.driver = self.chrome_handel.driver
        try:
            if self.chrome_handel.get_page(index_url):
                self.page_handle(self.chrome_handel.current_url)
                for _ in range(1, site_config.get('total_page', 0)):
                    if self.chrome_handel.click_element(**sel_config.get('next_page_btn')):
                        self.page_handle(self.chrome_handel.current_url)
            del self.chrome_handel
        except Exception as e:
            self.save_location_file(file_download_path)

    def data_format(self, current_url, title, response, parse):
        data_format = Formatter(self.website, self.category, self.handler, parse)
        data = data_format.format_data(current_url, title, response)
        # print json.dumps(data, ensure_ascii=False, encoding='u8')
        col.insert(data)



    @staticmethod
    def save_location_file(path):
        files = os.listdir(path)
        for _file in files:
            file_path = os.path.join(path, _file)
            print file_path
            with open(file_path, mode='rb') as fp:
                print fp
                pass  # todo mongo 写文件入口
        os.removedirs(path)


if __name__ == '__main__':
    for _ in range(50):
        t = SeleniumPolicySpider()
        t.main()
