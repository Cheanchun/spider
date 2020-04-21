import json
import time

import execjs
import random
import re
import requests


def exec_js2(resp):
    js = "function dd(){var json=" + resp + ";return json.map( function(item){ return String." \
                                            "fromCharCode(item);}).join('');}"
    ctx = execjs.compile(js)
    return ctx.call("dd")


headers = {
    'Host': 'www.gsxt.gov.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36',
    'Refer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
    'Referer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
    'Origin': 'http://www.gsxt.gov.cn',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}


class test():
    # 获取验证码信息
    def __init__(self):
        pass
    def get_image_gif(self):
        url = f'http://www.gsxt.gov.cn/SearchItemCaptcha?t={time.time()*1000}'
        resj = self.session.get(url, headers=self.headers, cookies=self.cookies)
        for_test_error = resj.text  # 用于错误捕获打印
        for i in range(3):
            try:
                resj = resj.json()
                # print(resj)
                url = "http://www.gsxt.gov.cn/corp-query-custom-geetest-image.gif?v="
                local_time = time.localtime(time.time())
                url = url + str(local_time.tm_min + local_time.tm_sec)
                time.sleep(random.randint(1, 2))
                resp = self.session.get(url, headers=self.headers, cookies=self.cookies)
                print(resp.text)
                self.success = resj['success']
                self.gt = resj['gt']
                self.challenge = resj['challenge']
                aaa = exec_js2(resp.text)
                matchObj = re.search('location_info = (\d+);', aaa)
                if matchObj:
                    return matchObj.group(1)
                else:
                    raise RuntimeError("RuntimeError:没有找到location_info")
            except json.JSONDecodeError as e:
                print("[!]image_gif获取失败,重新获取")
                print(e)
                print(for_test_error)
                raise EOFError("image_gif获取失败,重新获取")

    def get_token(self):
        url = "http://www.gsxt.gov.cn/corp-query-geetest-validate-input.html?token=" + self.get_image_gif()
        resp = self.session.get(url, headers=self.headers, cookies=self.cookies)
        time.sleep(random.randint(1, 2))
        aaa = exec_js2(resp.text)
        matchObj = re.search('value: (\d+)}', aaa)
        if matchObj:
            location_info = matchObj.group(1)
            self.token = str(int(location_info) ^ 536870911)
            print('[*] 3. 获取token: ' + self.token)
        else:
            print("[!]token获取失败,等待重新获取!")
            time.sleep(random.randint(3, 5))
            self.get_token()
            # raise EOFError("RuntimeError:没有找到location_info")

    cookies = {
        'CNZZDATA1261033118': '1849185664-1553058063-http%253A%252F%252Fwww.gsxt.gov.cn%252F%7C1553058063',
        'UM_distinctid': '16999acf61518f-07ab71371206e2-15231708-fa000-16999acf61694f',
        'JSESSIONID': 'AB41E25398EFE3FE867121551293F839-n2:0', 'tlb_cookie': 'S172.16.12.68',
        'SECTOKEN': '7168566930043570200', '__jsl_clearance': '1553061438.015|0|yksV%2FZS%2FhwKwjs17P98u4qjkxMA%3D',
        '__jsluid': '6bb26a36369fde75e4787a68b623f937'
    }

    url = "http://www.gsxt.gov.cn/SearchItemCaptcha?t={}".format(int(time.time() * 1000))  # 获取gt & challenge
    url1 = "http://jiyanapi.c2567.com/shibie?gt={}&challenge={}&referer=http://www.gsxt.gov.cn/&user=zsyhcdjy&pass=secneo123&return=json&model=3&format=utf8"
