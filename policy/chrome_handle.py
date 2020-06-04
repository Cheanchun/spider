# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo   1.下一页操作 2.滑动到指定的标签
"""
import cookielib
import random
import time
import warnings

from requests.cookies import RequestsCookieJar
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By  # 选择方法
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待

from policy.common_tools.tools import get_abuyun_proxy, get_zhima_proxy

DEFAULT_HEADERS = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"


class ChromeHandle(object):
    def __init__(self, selenium_config={}):
        assert isinstance(selenium_config, dict)
        self.proxy = selenium_config.get('proxy_type', '')
        self.chrome_init = selenium_config.get('chrome_init', [])
        self.driver = self._open_chrome(self.chrome_init)
        self.driver.implicitly_wait(selenium_config.get('implicitly_wait', 10))  # 隐式等待
        self.driver.set_page_load_timeout(selenium_config.get('load_timeout', 10))  # 页面加载等待

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
        options = webdriver.ChromeOptions()
        if self.proxy:
            self.proxy = self._get_proxy(self.proxy)
            print(self.proxy)
            options.add_argument("--proxy-server={}".format(self.proxy.get("http") or self.proxy.get("https")))
        options.add_argument('--disable-gpu')
        options.add_argument('window-size=1080x720')
        options.add_argument('--no-sandbox')
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
        self.driver.close()  # todo quit 会有错误
        print 'chrome close'

    @property
    def user_agent(self):
        return self.driver.execute_script('return navigator.userAgent')

    def click_element(self, by_class='', by_xpath='', by_id='', **kwargs):
        selement = self.find_elements(by_class='', by_xpath='', by_id='', **kwargs)



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

    def __del__(self):
        self.close_chrome()


if __name__ == '__main__':
    sel_config = {
        'proxy_type': '',
        'chrome_init': [],
    }
    t = ChromeHandle(sel_config)
    res = t.get_page('http://www.baidu.com', by_id='su')
    if res:
        # print t.page_source.encode('GBK', 'ignore').decode('GBK')
        # print t.cookies_dict
        t.click_element(by_id='su1')
    # print t.page_source
