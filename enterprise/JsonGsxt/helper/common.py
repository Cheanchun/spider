# encoding: utf-8
import sys

import execjs
import re


# print u"项目路径:", sys.path[0]
def execJS(resp):
    cookies = {}
    # 获取和替换动态js，生成cookie在此访问
    js_match = re.findall(r'<script>(.*?)</script>', resp)
    if js_match:
        js = js_match[0]
        key_js = re.findall(r'eval\((.*?)\);', js)[0]
        replace = 'var cookie_js={};'.format(key_js)
        js = re.sub(r'eval\(.*?\);', replace, js)
        js = js.replace(
            'break',
            'if(cookie_js.indexOf("document.cookie=\'__jsl_clearance=")!=-1){cookie_js = cookie_js.match(/document.cookie=(.*?)\+\';Expires/i)[1];break}')
        js = 'var cookie_js, window={};' + js + 'function get_cookie(){return eval(cookie_js);}'
        js = js.replace('', '')

        ctx = execjs.compile(js)
        cookie_value = ctx.call("get_cookie")
        cookies = {
            cookie_value.split('=')[0]: cookie_value.split('=')[1]
        }
    return cookies


class BaseConfig(object):
    # JiYan user/passwd
    HOME_PATH = sys.path[0]
    HOST = "47.105.54.129"
    PORT = 6388
    DB_INDEX = 10
    REDIS_SET_NAME = "order_company"
    PASSWORD = "admin"
    MONGODB_HOST = "47.105.54.129"
    MONGODB_PORT = 27017
    MONGODB_USER = 'chean'
    MONGODB_PWD = 'scc57295729'
    SEARCH_TYPE = "ent_tab"
    CYCLE_WAITE_TIME = 60 * 60 * 1  # 1 hour
