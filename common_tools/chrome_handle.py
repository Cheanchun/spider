# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo 1.页面滚动 2.页面截图，
"""
import functools
import io
import time
import traceback
import warnings

from PIL import Image
from requests.cookies import RequestsCookieJar
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# from common_tools.tools import get_abuyun_proxy, get_zhima_proxy

DEFAULT_HEADERS = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
WEB_DRIVER_PATH = 'chromedriver'
# WEB_DRIVER_PATH = "/home/work/data/tools/chromedriver"

CHROME_DEFAULT_INIT = [
    "window-size=1080x720",
    "--disable-gpu",
    "--no-sandbox",
    "--user-agent={}".format(DEFAULT_HEADERS),
    # "--proxy-server={}".format("127.0.0.1:80"),
    # "--headless",
    "acceptSslCerts"
]
HANDEL_MAP = {}  # 句柄管理


def handel_manage(func):
    @functools.wraps(func)
    def wrapper(self, url, *args, **kwargs):
        HANDEL_MAP[url] = self.driver.current_window_handle
        return func(self, url, *args, **kwargs)

    return wrapper


class ChromeHandle(object):
    def __init__(self, config={}, file_download_path=None, debug=False):
        assert isinstance(config, dict)
        self.file_download_path = file_download_path
        self.selenium_config = config
        self.proxy = config.get('proxy_type')
        self.chrome_init = config.get('chrome_init', [])
        self.driver = self._open_chrome(self.chrome_init)
        self.driver.implicitly_wait(config.get('implicitly_wait', 30))  # 隐式等待
        self.driver.set_page_load_timeout(config.get('load_timeout', 30))  # 页面加载等待

    def _wait_page(self, timeout=2, try_times=3, **kwargs):
        """
        waiting page until some element is available
        :param timeout:超时
        :param try_times:尝试次数
        :param kwargs:
        :return:bool
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
                    return True  # 未配置等待，默认睡眠，返回True
                return True
            except TimeoutException:
                self.driver.refresh()
                warnings.warn('Element Not Find,please check the element is available')
        return flag

    def add_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def _open_chrome(self, init):
        """
        open chrome
        :param init: chrome init info
        :return: driver
        """
        # print 'chrome init info:', init
        options = webdriver.ChromeOptions()
        if self.proxy:
            # print('use proxy', self.proxy)
            self.proxy = self._get_proxy(self.proxy)
            options.add_argument("--proxy-server={}".format(self.proxy.get("http") or self.proxy.get("https")))
        if self.file_download_path:
            pfs = {'profile.default_content_settings.popups': 0, 'download.default_directory': self.file_download_path}
            options.add_experimental_option('prefs', pfs)  # 自定义文件存储路径
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        init = init or CHROME_DEFAULT_INIT
        c = DesiredCapabilities.CHROME.copy()
        if init and isinstance(init, list):
            for item in init:
                if item == 'acceptSslCerts':
                    c['acceptSslCerts'] = True
                    c['acceptInsecureCerts'] = True
                options.add_argument(item)
            return webdriver.Chrome(chrome_options=options, desired_capabilities=c, executable_path=WEB_DRIVER_PATH)
        return webdriver.Chrome(chrome_options=options, executable_path=WEB_DRIVER_PATH)

    @staticmethod
    def _get_proxy(proxy_type='abuyun'):
        """
        get a proxy
        :param proxy_type:
        :return: proxy ->  {'https':'ip:port','http':'ip:port'}
        """
        if proxy_type == 'abuyun':
            return get_abuyun_proxy()
        elif proxy_type == 'duobeiyun':
            pass  # todo add
        elif proxy_type == 'zhima':
            return get_zhima_proxy()
        elif isinstance(proxy_type, dict) and (proxy_type.get('https') or proxy_type.get('http')):
            return proxy_type
        else:
            raise TypeError('no such proxy type,please check the proxy type')

    @handel_manage
    def get_page(self, url, timeout=5, page_source=None, try_times=3, waiting={}):
        """
        open web page through chrome
        :param url: page of url
        :param timeout:
        :param page_source: is return page_source
        :param try_times:
        :param waiting: return until some element is available
        :return:bool or str
        """
        try:
            self.driver.get(url)
        except TimeoutException as ex:
            warnings.warn(ex.msg)
            self.restart_chrome(init=self.chrome_init)
            self.driver.get(url)
        flag = self._wait_page(timeout=timeout, try_times=try_times, **waiting)
        if flag:
            if page_source:
                return self.page_source
        else:
            warnings.warn('page get fail the element not find in this page')
        return flag

    def restart_chrome(self, init=None):
        """
        close chrome and start a new chrome
        :param init: chrome init -> list
        :return:driver with current url page
        """
        # print 'chrome restarting ...'
        self.driver.quit()
        self.driver = self._open_chrome(init) if init else self._open_chrome(self.chrome_init)
        # print 'chrome start finish ...'

    def delete_cookies(self):
        """
        delete all cookie
        :return: None
        """
        self.driver.delete_all_cookies()

    def delete_cookie(self, name):
        """
        delete one of cookies
        :param name: cookie name
        :return: None
        """
        self.driver.delete_cookie(name)

    def open_new_handel(self, check_out=False):
        """
        open a new label
        :param check_out:
        :return:
        """
        self.driver.execute_script("window.open()")
        if check_out:
            self.driver.switch_to.window(self.driver.window_handles[-1])

    def check_out_handel(self, url=None, index=None, handel_name=None):
        assert url or index or handel_name
        if index and abs(index) < len(self.driver.window_handles):
            self.driver.switch_to.window(self.driver.window_handles[-1])
            return True
        elif handel_name:
            self.driver.switch_to.window(handel_name)
            return True
        handel_name = HANDEL_MAP.get(url)
        self.driver.switch_to.window(handel_name)

    def close_handel(self, url, index):
        current_handel = self.driver.current_window_handle
        self.check_out_handel(url, index)
        self.driver.close()
        self.check_out_handel(handel_name=current_handel)

    @property
    def current_url(self):
        """
        get current url on current handel
        :return:url -> str
        """
        return self.driver.current_url

    @property
    def cookies_dict(self):
        """
        website cookie
        :return: cookies  -> dict
        """
        return {item.get('name'): item.get('value') for item in self.driver.get_cookies()}

    @property
    def cookie_jar(self, overwrite=True):
        """make a cookie jar obj"""
        cookiejar = RequestsCookieJar()
        names_from_jar = [cookie.name for cookie in cookiejar]
        cookie_dict = self.cookies_dict
        for name in cookie_dict:
            if overwrite or (name not in names_from_jar):
                cookiejar.set_cookie(self.create_cookie_item(name, cookie_dict[name]))
        return cookiejar

    # @staticmethod
    # def create_cookie_item(name, value, **kwargs):
    #     """Make a cookie from underspecified parameters.
    #
    #     By default, the pair of `name` and `value` will be set for the domain ''
    #     and sent on every request (this is sometimes called a "supercookie").
    #     """
    #     result = {
    #         'version': 0,
    #         'name': name,
    #         'value': value,
    #         'port': None,
    #         'domain': '',
    #         'path': '/',
    #         'secure': False,
    #         'expires': None,
    #         'discard': True,
    #         'comment': None,
    #         'comment_url': None,
    #         'rest': {'HttpOnly': None},
    #         'rfc2109': False,
    #     }
    #
    #     badargs = set(kwargs) - set(result)
    #     if badargs:
    #         err = 'create_cookie() got unexpected keyword arguments: %s'
    #         raise TypeError(err % list(badargs))
    #
    #     result.update(kwargs)
    #     result['port_specified'] = bool(result['port'])
    #     result['domain_specified'] = bool(result['domain'])
    #     result['domain_initial_dot'] = result['domain'].startswith('.')
    #     result['path_specified'] = bool(result['path'])
    #
    #     return cookielib.Cookie(**result)

    @property
    def get_driver(self):
        return self.driver

    @property
    def page_source(self):
        return self.driver.page_source

    @property
    def user_agent(self):
        self.driver.add_cookie()
        return self.driver.execute_script('return navigator.userAgent')

    def close_chrome(self):
        self.driver.quit()  # todo quit 会有错误
        # print 'chrome close'

    def click_element(self, by_class='', by_xpath='', by_id='', waiting={}):
        try:
            element = self.find_elements(by_class, by_xpath, by_id)
            if element:
                element.click()
                return self._wait_page(**waiting)
            return False
        except Exception as ex:
            traceback.format_exc()
            return False

    def roll_page(self, shot=False, img_path=None):
        pass  # todo

    def find_elements(self, by_class='', by_xpath='', by_id=''):
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
            print('element not find in this page')

    def headless_break(self):
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
			 Object.defineProperty(navigator, 'webdriver', {
			   get: () => undefined
			 })
		   """
        })

    def box_input(self, text, btn_class='', btn_xpath='', btn_id=''):
        assert text and (btn_id or btn_xpath or btn_class)
        element = self.find_elements(btn_class, btn_xpath, btn_id)
        try:
            element.send_keys(text)
            return True
        except Exception as e:
            traceback.format_exc()
            return False

    def get_screen(self):
        js = 'var winW = window.screen.width;var winH = window.screen.height;return(winW+","+winH)'
        w, h = self.driver.execute_script(js).encode('u8').split(',')
        return int(w), int(h)

    def _long_screen_shot(self):
        """
        长截图功能
        :return:Image Obj
        """
        self.driver.fullscreen_window()
        self.driver.find_element_by_xpath('//html').send_keys(Keys.HOME)  # 回到页面顶端
        body_height = self.driver.execute_script('var temp = document.body.clientHeight;return temp;')
        width, height = self.get_screen()
        ims = []
        current_height = 0
        while current_height < body_height:
            js = "var q=document.documentElement.scrollTop={}".format(current_height)
            self.driver.execute_script(js)
            ims.append(Image.open(io.BytesIO(self.driver.get_screenshot_as_png())))
            current_height += height
        result = Image.new(ims[0].mode, (width, body_height))
        for index, item in enumerate(ims):
            if index + 1 == len(ims):
                last_height = body_height - (height * index)
                cropped = item.crop((0, height - last_height, width, height))
                result.paste(cropped, box=(0, index * height))
                result.crop((0, 0, width, height))
            else:
                result.paste(item, box=(0, index * height))
        self.driver.maximize_window()
        return result

    # def screen_shot_as_base64(self, element=None, is_long_shot=False):
    #     """
    #     截图返回base64
    #     :param is_long_shot: 是否长截图
    #     :param element: 定位截图标签  {'by_class':'','by_xpath':'','by_id':''}
    #     :return:
    #     """
    #     if is_long_shot:
    #         long_shot_obj = self._long_screen_shot()
    #         outer_string = StringIO()
    #         long_shot_obj.save(outer_string, format='PNG')
    #         return base64.b64encode(outer_string.getvalue())
    #     else:
    #         if element:
    #             ele = self.find_elements(**element)
    #             self.driver.execute_script(u'arguments[0].scrollIntoView(true);', ele)
    #         return self.driver.get_screenshot_as_base64()

    def save_screen_shot(self, filename, is_long_shot=None, element=None):
        """
        截图保存
        :param filename:图片文件名称
        :param is_long_shot: 是否长截图
        :param element: 定位截图标签  {'by_class':'','by_xpath':'','by_id':''}
        :return:
        """
        if is_long_shot:
            long_shot_obj = self._long_screen_shot()
            long_shot_obj.save(filename, format='PNG')
            return long_shot_obj.save(filename)
        else:
            if element:
                ele = self.find_elements(**element)
                self.driver.execute_script(u'arguments[0].scrollIntoView(true);', ele)
            return self.driver.save_screenshot(filename)

    def __del__(self):
        self.close_chrome()


if __name__ == '__main__':
    sel_config = {
        'chrome_init': ['acceptSslCerts'],
        # 'proxy_type': {'https': '221.210.54.128:4257'},

    }
    client_btn = {
        'by_xpath': "//input[@id='su']",
        'by_id': '',
        'by_class': '',
    }
    waiting_page = {
        'by_xpath': '',
        'by_id': 'main-content',
        'by_class': '',
    }
    c = ChromeHandle(sel_config)
    c.get_page('http://dwiki.cmbchina.cn/pages/viewpage.action?pageId=84773141',
               page_source=True)
    print(c.screen_shot(element={"by_xpath": "//div[@class='ifx-xf-loupan-title']/div"}, full_page=True,
                        filename='123.png'))
    time.sleep(2)
    c.open_new_handel(check_out=True)
    c.get_page('https://www.taobao.com')
    c.check_out_handel('https://www.baidu.com')
    print(HANDEL_MAP)
    time.sleep(2)
    del c
