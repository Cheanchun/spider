# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo   3.chrome报错之后恢复现场 4.文件 点击事件下载，保存之后写入mongo
"""
import cookielib
import json
import random
import re
import time
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
from policy.formatter import Formatter
from policy.parser import Parser
from policy.policy_module.configuration import ATTACH_RE

DEFAULT_HEADERS = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"

redis_config = {'host': '47.105.54.129', 'port': 6388, 'password': 'admin'}
CHARSET_RE = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
PRAGMA_RE = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)


class ChromeHandle(object):
    def __init__(self, selenium_config={}):
        assert isinstance(selenium_config, dict)

        self.proxy = selenium_config.get('proxy_type', '')
        self.chrome_init = selenium_config.get('chrome_init', [])
        self.driver = self._open_chrome(self.chrome_init)
        self.driver.implicitly_wait(selenium_config.get('implicitly_wait', 30))  # 隐式等待
        self.driver.set_page_load_timeout(selenium_config.get('load_timeout', 30))  # 页面加载等待
        self.user_redis = redis.Redis(**redis_config)
        self.parse = Parser(list_parse_type='xpath', list_parse_rule=sel_config.get('list_parse_rule'),
                            content_format='')
        self.website = sel_config.get('website')
        self.handler = sel_config.get('handler')
        self.category = sel_config.get('category')
        self.redis_key = sel_config.get('redis_key')

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
        options.add_argument('--disable-gpu')
        options.add_argument('window-size=1080x720')
        options.add_argument('--no-sandbox')
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
        return webdriver.Chrome(chrome_options=options)

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

    def get_page(self, url, timeout=10, try_times=3, **kwargs):
        try:
            self.driver.get(url)
        except TimeoutException as ex:
            warnings.warn(ex.msg)
            self.restart_chrome(init=self.chrome_init)
            self.driver.get(url)
        return self._wait_page(timeout=timeout, try_times=try_times, **kwargs)

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
                return self._wait_page(**sel_config.get('waiting_page', {}))
            return False
        except Exception:
            return False

    def roll_page(self):
        pass

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
        selemnt = self.find_elements()
        # todo query box input

    def __del__(self):
        self.close_chrome()

    def file_download(self, resp, url, file_name):
        with open('./file/{}'.format(file_name), mode='wb') as fp:
            fp.write(resp.content)

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

    def check_page(self, content, url):
        if len(content) < 100:
            self.restart_chrome()
            self.driver.get(url)

    def page_handle(self, cur_url):
        urls = [{'title': item.get('title'), 'url': urljoin(cur_url, item.get('url'))} for item in
                self.parse.parse_list(self.driver.page_source)]
        content_urls, file_urls = self.check_list_url_type(urls)
        js = 'window.open();'
        self.driver.execute_script(js)
        self.driver.switch_to.window(self.driver.window_handles[1])
        for item in content_urls:
            self.driver.get(item.get('url'))
            self.check_page(self.driver.page_source, item.get('url'))
            time.sleep(2)
            self._wait_page()
            file_urls.extend(self.parse.parse_content(self.driver.page_source, item.get('url')))
            self.data_format(item.get('url'), item.get('title'), self.driver.page_source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        if file_urls:
            session, session.headers = requests.Session(), {'User-Agent': self.user_redis}
            session.cookies = self.cookie_jar
            for item in file_urls:
                self.file_download(session.get(item.get('url')), item.get('url'), item.get('title'))
                # print item.get('title'), item.get('url').decode('u8')
                # pass  # todo 附件下载

    def data_format(self, current_url, title, response):
        data_format = Formatter(self.website, self.category, self.handler, self.parse)
        data = data_format.format_data(current_url, title, response)
        print json.dumps(data, ensure_ascii=False, encoding='u8')

    def main(self):
        index_url = sel_config.get('index_url')
        if self.get_page(index_url, **sel_config.get('waiting_page', '')):
            self.page_handle(self.driver.current_url)
            for _ in range(1, sel_config.get('total_page', 0)):
                self._wait_page(**sel_config.get('waiting_page'))
                if self.click_element(**sel_config.get('next_page_btn')):
                    self.page_handle(self.driver.current_url)


if __name__ == '__main__':
    sel_config = {
        'index_url': 'http://www.cde.org.cn/regulat.do?method=getList&fclass=all&year=all',
        'list_parse_rule': "//tbody/tr/td/a",
        'next_page_btn': {
            'by_xpath': "//td[1]/font/a[2]",
            'by_id': '',
            'by_class': '',
        },
        'total_page': 2,
        'proxy_type': '',
        'handler': '1-proxy-nao',
        'category': '首页>公开目录',
        'website': '审计署',
        'redis_key': 'policy:audit:audit_gdnps',
        'chrome_init': ['acceptSslCerts'],
        'waiting_page': {
            'by_xpath': "//tbody/tr/td/a",
            'by_id': '',
            'by_class': '',
        },

    }
    t = ChromeHandle(sel_config)
    t.main()
