# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo   3.chrome报错之后恢复现场 4.文件 点击事件下载，保存之后写入mongo
"""
import cookielib
import json
import os
import random
import re
import time
import traceback
import urlparse
import warnings
from urlparse import urljoin

import redis
import requests
from requests.cookies import RequestsCookieJar
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By  # 选择方法
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待

from policy.common_tools.tools import get_abuyun_proxy, get_zhima_proxy
# from policy.config_v2 import sel_config
from policy.config_v2 import config
from policy.formatter import Formatter
from policy.parser import Parser
from policy.policy_module.configuration import ATTACH_RE

DEFAULT_HEADERS = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
FILE_PATH = u'./files/'
REDIS_CONFIG = {'host': '47.105.54.129', 'port': 6388, 'password': 'admin'}
CHARSET_RE = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
PRAGMA_RE = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
WEB_DRIVER_PATH = ''
FILE_PATH = ''


class ChromeHandle(object):
    def __init__(self, selenium_config):
        assert isinstance(selenium_config, dict)
        self.selenium_config = selenium_config
        self.proxy = selenium_config.get('proxy_type', '')
        self.chrome_init = selenium_config.get('chrome_init', [])
        self.driver = self._open_chrome(self.chrome_init)
        self.driver.implicitly_wait(selenium_config.get('implicitly_wait', 30))  # 隐式等待
        self.driver.set_page_load_timeout(selenium_config.get('load_timeout', 30))  # 页面加载等待
        self.user_redis = redis.Redis(**REDIS_CONFIG)
        self.parse = Parser(list_parse_type='xpath', list_parse_rule=selenium_config.get('list_parse_rule'),
                            content_format='')
        self.redis_key = selenium_config.get('redis_key')

    def _wait_page(self, timeout=5, try_times=3, **kwargs):
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
                time.sleep(random.randint(2, 5))
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
        # prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': FILE_PATH}
        # options.add_experimental_option('prefs', prefs)  # todo 三期 本地文件存储路径
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # options.add_argument("--headless")  # todo headless
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
        self.user_redis = redis.Redis(**REDIS_CONFIG)

    def get_config(self):
        return config[0]

    def page_handle(self, cur_url):
        urls = [{'title': item.get('title'), 'url': urljoin(cur_url, item.get('url'))} for item in
                self.parse.parse_list(self.driver.page_source)]
        content_urls, file_urls = self.check_list_url_type(urls)
        js = 'window.open();'
        self.driver.execute_script(js)
        self.driver.switch_to.window(self.driver.window_handles[1])
        for item in content_urls:
            self.driver.get(item.get('url'))
            self.check_page(self.chrome_handel.page_source, item.get('url'))
            file_urls.extend(self.parse.parse_content(self.chrome_handel.page_source, item.get('url')))
            self.data_format(item.get('url'), item.get('title'), self.driver.page_source, self.parse)
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        if file_urls:
            session, session.headers = requests.Session(), {'User-Agent': self.chrome_handel.user_agent}
            session.cookies = self.chrome_handel.cookie_jar
            for item in file_urls:
                self.file_download(session.get(item.get('url')), item.get('url'), item.get('title'))
                print item.get('title'), item.get('url').decode('u8')
                # pass  # todo 附件下载

    def file_download(self, resp, url, file_name):
        file_path = os.path.join(FILE_PATH, urlparse.urlparse(url).netloc)
        os.makedirs(file_path)
        with open(os.path.join(file_path, file_name), mode='wb') as fp:
            fp.write(resp.content)

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
        config = self.get_config()
        sel_config = config.get('sel_config')
        site_config = config.get('site_config')
        self.parse = Parser(list_parse_type='xpath', list_parse_rule=site_config.get('list_parse_rule'),
                            content_format='')
        self.chrome_handel = ChromeHandle(sel_config)
        self.driver = self.chrome_handel.driver
        index_url = site_config.get('index_url')
        if self.chrome_handel.get_page(index_url):
            self.page_handle(self.chrome_handel.current_url)
            for _ in range(1, site_config.get('total_page', 0)):
                if self.chrome_handel.click_element(**sel_config.get('next_page_btn')):
                    self.page_handle(self.chrome_handel.current_url)

    def data_format(self, current_url, title, response, parse):
        data_format = Formatter(self.website, self.category, self.handler, parse)
        data = data_format.format_data(current_url, title, response)
        print json.dumps(data, ensure_ascii=False, encoding='u8')


def save_location_file(path):
    files = os.listdir(path)
    for _file in files:
        file_path = os.path.join(path, _file)
        print file_path
        with open(file_path, mode='rb') as fp:
            print fp
            pass  # todo mongo 写文件入口


if __name__ == '__main__':
    save_location_file('./')
