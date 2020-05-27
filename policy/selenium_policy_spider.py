# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import cookielib
import random
import re
import time
from urlparse import urljoin

import chardet
import requests
from lxml import etree
from requests.cookies import RequestsCookieJar
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By  # 选择方法
from selenium.webdriver.support import expected_conditions as EC  # 等待条件
from selenium.webdriver.support.ui import WebDriverWait  # 等待

from bank.utils.Comm import CommSession, DEFAULT_HEADERS
from policy.common_tools import tools
from policy.common_tools.tools import get_abuyun_proxy, get_zhima_proxy

ITEM = {
    'website': '',
    'refer': '',
    'category': '',
    'HTML': '',
    'HTML_length': '',
    'attachments': [],  # 附件路径列表
    'attachments_detail': [],  # 附件详细列表  ATTACHMENT
    'anchorText': '',
    'handler': '',
    'invTime': '',
    'dataId': '',  # sha256(url)
    # 'publish_time': '',  # 已废弃
}
ATTACHMENT = {
    'anchorText': '',
    'file': '',
    'url': ''
}
FILTER_URL = ['javascript:void(0);', 'javascript:;']
CHARSET_RE = re.compile(r'<meta.*?charset=["\']*(.+?)["\'>]', flags=re.I)
PRAGMA_RE = re.compile(r'<meta.*?content=["\']*;?charset=(.+?)["\'>]', flags=re.I)
ATTACH_RE = re.compile(r'(https?://.*.(doc|docx|xls|xlsx|pdf|zip|rar|7z|gif|jpg|jpeg|png|bmp).*?)')
NOT_NEED_PATTERN = re.compile(ur'\n| |Â|\\')


class ChromeHandle(object):
    def __init__(self, url=None, chrome_config=None, proxy_type=None):
        self.url = index
        self.chrome_config = chrome_config
        self.proxy_type = proxy_type
        self.driver = self._open_chrome()

    def _wait_page(self, timeout=5, try_times=3, **kwargs):
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
        return flag

    def _open_chrome(self):
        """
        open chrome
        :return: driver
        """
        options = webdriver.ChromeOptions()
        if self.proxy_type:
            self.proxy = self._get_proxy(self.proxy_type)
            print(self.proxy)
            options.add_argument("--proxy-server={}".format(self.proxy.get("http") or self.proxy.get("https")))
        options.add_argument('--disable-gpu')
        options.add_argument('window-size=1080x720')
        options.add_argument('--no-sandbox')
        # options.add_argument("--headless")  # todo headless
        options.add_argument("--user-agent={}".format(DEFAULT_HEADERS))
        if self.chrome_config and isinstance(self.chrome_config, list):
            c = DesiredCapabilities.CHROME.copy()
            for item in self.chrome_config:
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
        self.driver.get(url)
        return self._wait_page(timeout=timeout, try_times=try_times, **kwargs)

    def restart_chrome(self, url=None):
        print 'chrome restarting ...'
        self.driver.quit()
        self.driver = self._open_chrome()
        if url:
            self.driver.get(url)
        print 'chrome start finish ...'

    @property
    def get_cookies(self):
        return {item.get('name'): item.get('value') for item in self.driver.get_cookies()}

    @property
    def page_source(self):
        return self.driver.page_source

    def _close_chrome(self):
        self.driver.close()  # todo quit 会有错误
        print 'chrome close'

    @property
    def user_agent(self):
        return self.driver.execute_script('return navigator.userAgent')

    def __del__(self):
        self._close_chrome()


class SeleniumCrawler(object):
    def __init__(self):
        self.chrome = ''
        self.chrome_config = ''
        self.proxy_type = ''
        self.topic_id = 'b31d8e04-eba3-4670-969a-ead93d27464e'
        self.website = None
        self.category = None
        self.handler = None
        self.session = None
        self.list_xpath = list_config.get('rule')  # 列表解析内容URL的xpath
        self.title_xpath = None  # 标题xpath
        self.attach_xpath = None  # 附件xpath
        self.second_num = None  # 列表页第二页的页码数字
        self.max_pages = list_config.get('pages', 1)  # 列表最大页数
        self.index = index  # 首页url
        self.list_format = list_config.get('format')  # 翻页format

        self.is_finished = None  # 是否爬完全量
        self.list_redis = 'policy:all_list'
        self.crawled_urls = 'policy:crawled_urls'

        self.error_list = 'policy:error_list'

    def _get(self, url, method='get', retry=3, timeout=30, **kwargs):
        """
        网页下载
        :param url:
        :param method:
        :param retry:
        :param timeout:
        :param kwargs:
        :return:
        """
        for _ in range(retry):
            try:
                time.sleep(random.randint(3, 5))
                if method == 'get':
                    resp = self.session.get(url=url, timeout=timeout, params=kwargs.get('params', {}), **kwargs)
                elif method == 'post':
                    resp = self.session.post(url=url, timeout=timeout, **kwargs)
                else:
                    raise ValueError('request method not support')
            except requests.exceptions:
                continue
            if resp.status_code // 100 == 2:
                return resp
        raise requests.exceptions.RequestException('requests fail:{}'.format(url))

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

    def instance_session(self, index_url=None, cookie_dict=None, overwrite=True, **kwargs):
        session = CommSession(verify=True).session(index_url) if index_url else CommSession(verify=True).session()
        cookiejar = RequestsCookieJar()
        if cookie_dict is not None:
            names_from_jar = [cookie.name for cookie in cookiejar]
            for name in cookie_dict:
                if overwrite or (name not in names_from_jar):
                    cookiejar.set_cookie(self.create_cookie(name, cookie_dict[name]))
            session.cookies = cookiejar
            session.headers = {'User-Agent': self.chrome.user_agent}
        else:
            session.headers = {'cookie': kwargs.get('cookie')}
        return session

    def get_page(self, url, chrome=True, **kwargs):
        """

        :param url:
        :param chrome:
        :param kwargs:
        :return:
        """
        if chrome:
            if not self.chrome:
                self.chrome = ChromeHandle()
            try:
                res = self.chrome.get_page(url, **kwargs)
                return res
            except Exception as e:
                print 'chrome run error {}'.format(e)
                return self.chrome.restart_chrome(url)

        else:
            if self.chrome and self.session and self.session.cookies:
                self.session = self.instance_session(cookie_dict=self.chrome.get_cookies)
            else:
                self.session = self.instance_session(cookies=kwargs.get('cookies', ''))
            return self._get(url, **kwargs)

    @staticmethod
    def _coding(response):
        """
        设置编码
        :param response:
        :return:
        """
        if CHARSET_RE.findall(response.text):
            response.encoding = CHARSET_RE.findall(response.text)[0]
        elif PRAGMA_RE.findall(response.text):
            response.encoding = PRAGMA_RE.findall(response.text)[0]
        else:
            temp = chardet.detect(response.content)
            response.encoding = temp['encoding']
        return response

    def parse_list(self, content, res_url):
        """
        列表页解析
        :param content:string
        :param res_url: string
        :return: urls ->list
        """
        urls = []
        file_urls = []
        html = etree.HTML(content)
        temps = html.xpath(self.list_xpath)
        for temp in temps:
            url = ''.join(temp.xpath('./@href'))
            title_temp = temp.xpath('./@title|.//text()')
            title = title_temp.pop(0) if title_temp else ''
            if not title:
                title = re.sub(NOT_NEED_PATTERN, '', ''.join(title_temp))
            if not url.startswith('http'):
                url = urljoin(res_url, url)
            if ATTACH_RE.findall(url):
                file_urls.append((url, title))
            else:
                urls.append(url)
        return urls, file_urls

    def parse_content(self, content, url, **kwargs):
        """

        :param content:
        :param url:
        :param kwargs:
        :return:
        """
        # todo 文件下载 content不需要 但是需要 response
        item = dict(ITEM)
        item['website'] = self.website
        item['category'] = self.category
        item['handler'] = self.handler
        item['HTML'] = content if not kwargs.get('title') == 'content' else ''
        item['HTML_length'] = len(item['HTML'])
        item['refer'] = url
        item['invTime'] = int(time.time() * 1000)
        item['dataId'] = tools.make_sha256(text=item['refer'])
        if not kwargs.get('title'):
            html = etree.HTML(content)
            item['anchorText'] = re.sub(NOT_NEED_PATTERN, '',
                                        ''.join(html.xpath(self.title_xpath or '//title/text()')).strip())
            attach_temps = html.xpath(self.attach_xpath or '//a')
            item['attachments'], item['attachments_detail'] = self._parse_attach(attaches=attach_temps,
                                                                                 base_url=url)
        else:
            item['anchorText'] = kwargs.get('title')
            item['attachments'] = []
            item['attachments_detail'] = []
            md5_url = tools.make_md5(text=url)
            suffix = url.split('.')[-1].split('?')[0]
            filename = '{}.{}'.format(md5_url, suffix)
            item['attachments'].append(filename)
            attachment = dict(ATTACHMENT)
            attachment['anchorText'] = kwargs.get('title').strip() or md5_url
            attachment['file'] = filename
            attachment['url'] = url
            item['attachments_detail'].append(attachment)
            self._save_file(kwargs.get('response'), filename, attach_url=url)
        self.save_data(url, item, self.topic_id)

    def _save_file(self, resp, filename, attach_url):
        print attach_url, resp, filename
        # self.save_file(source_stream=resp, filename=filename, source_url=attach_url)

    def save_data(self, url, item, topic_id):
        print url, item, topic_id
        # self.save_topic_data(url=url, data=item, topic_id=self.topic_id)

    def _parse_attach(self, attaches=None, base_url=''):
        """
        解析附件
        :param attaches:
        :param base_url:
        :return:
        """
        attachments = []
        attachments_detail = []
        if attaches is not None:
            for temp in attaches:
                attach_url = ''.join(temp.xpath('./@href')).strip()
                # 过滤，排除非法的
                if attach_url in FILTER_URL:
                    continue
                # 格式化URL
                if not attach_url.startswith('http'):
                    attach_url = urljoin(base_url, attach_url)
                # 验证URL
                if not ATTACH_RE.findall(attach_url):
                    continue

                md5_url = tools.make_md5(text=attach_url)
                suffix = attach_url.split('.')[-1].split('?')[0]
                filename = '{}.{}'.format(md5_url, suffix)
                # 判断是否已经添加过
                if filename in attachments:
                    continue
                attachments.append(filename)
                # attachments_detail
                attachment = dict(ATTACHMENT)
                # 当anchorText没有文件名时，用附件url的md5
                attachment['anchorText'] = ''.join(temp.xpath('.//text()')).strip() or md5_url
                attachment['file'] = filename
                attachment['url'] = attach_url
                attachments_detail.append(attachment)
        return attachments, attachments_detail

    def main(self):
        page = 1
        while page <= self.max_pages:
            page += 1
            list_url = self.index
            if page > 1:
                if self.second_num == 1:
                    list_url = self.list_format.format(page - 1)
                else:
                    list_url = self.list_format.format(page)
            res = self.get_page(self.index, sel_config.get('index_use', True))
            if isinstance(res, bool):
                content = self.chrome.page_source
            else:
                content = self._coding(res).text
            urls, file_urls = self.parse_list(content, list_url)
            for url in urls:
                resp = self.get_page(url, chrome=sel_config.get('detail_use', True))
                if not isinstance(resp, bool):
                    content = self._coding(resp).text
                else:
                    content = self.chrome.page_source
                print 'url:{} resp:{}'.format(url, res)
                self.parse_content(content, url)
            for url, title in file_urls:
                print 'url:{} resp:{}'.format(url, res)
                resp = self.get_page(url, chrome=False, stream=True)
                self.parse_content(content='', url=url, title=title, response=resp)


if __name__ == '__main__':
    UrlConfig = {
        'index': 'http://www.cffex.com.cn/xgfg/',
        'list_config': {
            'format': 'http://www.cffex.com.cn/xgfg/',
            'pages': 2,
            'rule': "//li/a[@class='list_a_text ']",
            'method': '',
            'second_num': '2',
            'step': '1'
        },
        'content_config': {
            'method': '',
            'title_xpath': '',
            'attach_xpath': ''
        },
        'handler': '',
        'category': '',
        'website': '',
        'proxy_type': '',
        'redis_key': '',
        'cookie': '',
        'headers': '',
        'selenium_config': {
            'chrome_config': [],
            'index_use': False,
            'detail_use': False,
            'waiting_xpath': ''
        }
    }
    sel_config = UrlConfig.get('selenium_config')
    index = UrlConfig.get('index')
    list_config = UrlConfig.get('list_config')
    content_config = UrlConfig.get('content_config')
    t = SeleniumCrawler()
    t.main()
