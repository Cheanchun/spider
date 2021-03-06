#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Alex
@date: 2020/08/18 15:54:00
@file: ws_api.py
@usage: 搜狗微信API
"""
import os
import re
import time
import urllib

import ws_exceptions
from common_tools import config, exception, tools
from common_tools.chaojiying import ChaojiyingClient
from common_tools.common_requests import CommonRequests
from common_tools.identify_captcha import IdentifyCaptcha
from ws_parse import WechatSogouParse


class WechatSogouApi(object):
    """
    搜狗微信API
    """

    def __init__(self, captcha_break_times=3, headers=None):
        """
        初始化
        :param captcha_break_times: 破解验证码尝试次数 int
        :param headers: 请求头 dict
        """
        assert isinstance(captcha_break_times, int) and 0 < captcha_break_times < 10
        self.captcha_break_times = captcha_break_times

        self.common_requests = CommonRequests(is_need_session=True)
        self.headers = headers
        if self.headers:
            self.headers['User-Agent'] = config.USER_AGENT
        else:
            self.headers = {'User-Agent': config.USER_AGENT}

        # self.article_list_format = 'http://weixin.sogou.com/weixin?type=2&page={page}&ie=utf8&query={keyword}&interation='
        self.article_list_format = 'https://weixin.sogou.com/weixin?query={keyword}&_sug_type_=&s_from=input&_sug_=n&type=2&page={page}&ie=utf8'
        self.gzh_list_format = 'https://weixin.sogou.com/weixin?query={keyword}&s_from=input&type=1&page={page}&ie=utf8'

        # 搜狗验证码相关
        self.sogou_captcha_format = 'http://weixin.sogou.com/antispider/util/seccode.php?tc={tc}'  # get
        self.sogou_identify_captcha = 'http://weixin.sogou.com/antispider/thank.php'  # post
        # 微信验证码相关
        self.wechat_captcha_format = 'https://mp.weixin.qq.com/mp/verifycode?cert={cert}'  # get
        self.wechat_identify_captcha = 'https://mp.weixin.qq.com/mp/verifycode'  # post

    def _crawl_page(self, url, method='get', data=None, headers=None):
        """
        请求页面
        :param url:
        :return:
        """
        try:
            response = self.common_requests.retry_download_page(url=url, method=method, data=data, headers=headers)
            return response
        except exception.DownloadError as ex:
            raise ws_exceptions.WechatSogouRequestsError(ex)
        except Exception as ex:
            raise ws_exceptions.WechatSogouRequestsError(ex)

    def _identify_image_by_chaojiying(self, img):
        """
        超级鹰打码
        :param img:
        :return:
        """
        chaojiying_client = ChaojiyingClient()
        res = chaojiying_client.post_pic(img, 1006)
        return res.get("pic_str")

    def _identify_image_by_hand(self, img):
        """
        手动打码
        :param img:
        :return:
        """
        text = raw_input(u'验证码:')
        return text

    def _identify_image_by_bearcat(self, img):
        """
        使用自己搭建的打码平台识别
        :param img:
        :return:
        """
        identify_captcha = IdentifyCaptcha()
        res = identify_captcha.post_pic(img=img)
        return res.get('result')

    def _crack_sogou_callback(self, url, img, identify_image_callback=None):
        """
        识别搜狗验证码并破解
        :param url: 原URL
        :param img: 验证码content,流数据
        :param identify_image_callback: 验证码识别方法
        :return:
        """
        url_quote = url.split('weixin.sogou.com/')[-1]
        data = {
            'c': identify_image_callback(img),
            'r': '%2F' + url_quote,
            'v': 5
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://weixin.sogou.com/antispider/?from=%2f' + url_quote
        }
        # 调用验证URL
        res = self._crawl_page(self.sogou_identify_captcha, method='post', data=data, headers=headers)
        if res.status_code != 200:
            raise ws_exceptions.WechatSogouIdentifyImgError(u'identify code error, '
                                                            u'status code: {}, msg: {}'.format(res.get('code'),
                                                                                               res.get('msg')))
        return res.json()

    def _crack_wechat_callback(self, url, img, identify_image_callback=None):
        """
        识别微信验证码并破解
        :param url: 原URL
        :param img: 验证码content,流数据
        :param identify_image_callback: 验证码识别方法
        :return:
        """
        data = {
            'cert': time.time() * 1000,
            'input': identify_image_callback(img)
        }
        headers = {
            'Host': 'mp.weixin.qq.com',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': url
        }
        # 调用验证URL
        res = self._crawl_page(self.wechat_identify_captcha, method='post', data=data, headers=headers)
        if res.status_code != 200:
            raise ws_exceptions.WechatSogouIdentifyImgError(u'identify code error, '
                                                            u'status code: {}, msg: {}'.format(res.get('code'),
                                                                                               res.get('msg')))
        return res.json()

    def _crack_captcha(self, url, identify_image_callback, platform=None):
        """
        开始破解
        :param url: 原URL
        :param identify_image_callback: 验证码识别方法
        :param platform: 平台, sogou or wechat
        :return:
        """
        millis = int(round(time.time() * 1000))
        if platform == 'sogou':
            captcha_url = self.sogou_captcha_format.format(tc=millis)
            crack_captcha_callback = self._crack_sogou_callback
        elif platform == 'wechat':
            captcha_url = self.wechat_captcha_format.format(cert=millis)
            crack_captcha_callback = self._crack_wechat_callback
        else:
            raise ValueError('platform value error')
        captcha_res = self._crawl_page(captcha_url, headers={'Referer': url})
        # with open('./img/{}.jpg'.format(millis), 'w') as fw:
        #     fw.write(captcha_res.content)
        if captcha_res.status_code != 200:
            raise ws_exceptions.WechatSogouRequestsError('get captcha img error')

        # 调用识别破解方法
        res = crack_captcha_callback(url, captcha_res.content, identify_image_callback)
        if res['code'] != 0:
            raise ws_exceptions.WechatSogouIdentifyImgError(u'identify img error, '
                                                            u'code: {}, msg: {}'.format(res.get('code'),
                                                                                        res.get('msg')))
        if platform == 'sogou':
            cookies = 'SUV={}; SNUID={};'.format(self.common_requests.session.cookies.get('SUID'),
                                                 res.get('id'))
            self.headers['Cookie'] = cookies

    def _get_page(self, url, referer=None, identify_image_callback=None, platform=None):
        """
        获取页面
        :param url: 页面URL
        :param referer: referer
        :param identify_image_callback: 验证码识别方法
        :param platform: 平台, sogou or wechat
        :return:
        """
        if platform not in ['sogou', 'wechat']:
            raise ValueError('platform value error')

        self.headers['Referer'] = referer
        resp = self._crawl_page(url, headers=self.headers)
        resp = tools.coding(response=resp)
        if u'antispider' in resp.url or u'请输入验证码' in resp.text:
            for times in range(self.captcha_break_times):
                try:
                    self._crack_captcha(url=url, identify_image_callback=identify_image_callback, platform=platform)
                    break
                except ws_exceptions.WechatSogouIdentifyImgError as ex:
                    if times == self.captcha_break_times - 1:
                        raise ws_exceptions.WechatSogouIdentifyImgError(ex)
            # 再次访问
            self.headers['Referer'] = referer
            self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
            resp = self._crawl_page(url, headers=self.headers)
            resp = tools.coding(response=resp)
        return resp

    def _gen_search_list_url(self, keyword, page=1, url_type='article'):
        """
        构造URL
        :param keyword:
        :param page:
        :param url_type:
        :return:
        """
        if url_type not in ['article', 'gzh']:
            raise ValueError('url type value error')
        if url_type == 'article':
            return self.article_list_format.format(keyword=urllib.quote(keyword.encode('utf-8')), page=page)
        else:
            return self.gzh_list_format.format(keyword=urllib.quote(keyword.encode('utf-8')), page=page)

    def gen_img(self, url, path):
        """
        生产验证码用于测试打码平台
        :param url:
        :param path:
        :return:
        """
        if not os.path.exists(path):
            os.makedirs(path)
        millis = int(round(time.time() * 1000))
        captcha_res = self._crawl_page(self.sogou_captcha_format.format(tc=millis), headers={'Referer': url})
        with open('{}/{}.jpg'.format(path, millis), 'w') as fw:
            fw.write(captcha_res.content)

    def _decode_url(self, origin_url, referer=None, identify_image_callback=None):
        """
        解析成真正的URL,将搜狗端的URL解析成微信端的URL
        :param origin_url: 原URL
        :param referer: referer
        :param identify_image_callback: 自定义验证码识别方法,(默认使用超级鹰,需要提供账号密码)
        :return:
        """
        if identify_image_callback is None:
            # identify_image_callback = self._identify_image_by_chaojiying
            # identify_image_callback = self._identify_image_by_hand
            identify_image_callback = self._identify_image_by_bearcat
        assert callable(identify_image_callback)

        resp = self._get_page(url=origin_url,
                              referer=referer,
                              identify_image_callback=identify_image_callback,
                              platform='sogou')
        true_url = ''.join(re.findall(r"url.*?= '(.*?)';", resp.text)).replace('@', '')
        return true_url

    def search_article_list(self, keyword, page=1, identify_image_callback=None, decode_url=True):
        """
        搜索接口获取文章列表
        :param keyword: 关键字
        :param page: 页码
        :param identify_image_callback: 自定义验证码识别方法,(默认使用超级鹰,需要提供账号密码)
        :param decode_url: 是否将origin_url解析为真正的详情页url, 默认True,解析
        :return:
        """
        if identify_image_callback is None:
            # identify_image_callback = self._identify_image_by_chaojiying
            # identify_image_callback = self._identify_image_by_hand
            identify_image_callback = self._identify_image_by_bearcat
        assert callable(identify_image_callback)

        list_url = self._gen_search_list_url(keyword=keyword, page=page, url_type='article')
        response = self._get_page(url=list_url,
                                  referer=self._gen_search_list_url(keyword=keyword, page=1, url_type='article'),
                                  identify_image_callback=identify_image_callback,
                                  platform='sogou')
        # 解析列表页
        articles = WechatSogouParse.parse_sogou_article_list(resp_text=response.text)
        for article in articles:
            if decode_url:
                true_url = self._decode_url(origin_url=article.get('origin_url'),
                                            referer=list_url,
                                            identify_image_callback=identify_image_callback)
                article['true_url'] = true_url
            yield article

    def search_gzh_list(self, keyword, page=1, identify_image_callback=None, decode_url=True):
        """
        搜索接口获取公众号列表, 并返回公众号最新1条文章
        :param keyword: 关键字
        :param page: 页码
        :param identify_image_callback: 自定义验证码识别方法,(默认使用超级鹰,需要提供账号密码)
        :param decode_url: 是否将origin_url解析为真正的详情url, 默认True,解析
        :return:
        """
        if identify_image_callback is None:
            # identify_image_callback = self._identify_image_by_chaojiying
            # identify_image_callback = self._identify_image_by_hand
            identify_image_callback = self._identify_image_by_bearcat
        assert callable(identify_image_callback)

        list_url = self._gen_search_list_url(keyword=keyword, page=page, url_type='gzh')
        response = self._get_page(url=list_url,
                                  referer=self._gen_search_list_url(keyword=keyword, page=1, url_type='gzh'),
                                  identify_image_callback=identify_image_callback,
                                  platform='sogou')
        # 解析列表页
        gzh_list = WechatSogouParse.parse_sogou_gzh_list(resp_text=response.text)
        for gzh in gzh_list:
            if decode_url:
                true_url = self._decode_url(origin_url=gzh.get('origin_url'),
                                            referer=list_url,
                                            identify_image_callback=identify_image_callback)
                gzh['true_url'] = true_url
            yield gzh

    def get_gzh_history_articles(self, keyword, url, identify_image_callback=None):
        """
        搜狗已关闭此功能
        获取公众号最近10条文章
        :param keyword: 关键字
        :param url: 公众号详情URL
        :param identify_image_callback: 自定义验证码识别方法,(默认使用超级鹰,需要提供账号密码)
        :return:
        """
        if identify_image_callback is None:
            # identify_image_callback = self._identify_image_by_chaojiying
            # identify_image_callback = self._identify_image_by_hand
            identify_image_callback = self._identify_image_by_bearcat
        assert callable(identify_image_callback)

        origin_url = url
        if url.startswith(('https://weixin.sogou.com', 'http://weixin.sogou.com')):
            url = self._decode_url(origin_url=url,
                                   referer=self._gen_search_list_url(keyword=keyword, page=1, url_type='article'),
                                   identify_image_callback=identify_image_callback)
        response = self._get_page(url=url,
                                  referer=self._gen_search_list_url(keyword=keyword, page=1, url_type='article'),
                                  identify_image_callback=identify_image_callback,
                                  platform='wechat')
        if u'链接已过期' in response.text:
            raise ws_exceptions.WechatSogouUrlExpireError('url is expire, {}'.format(origin_url))
        elif u'该内容已被发布者删除' in response.text:
            raise ws_exceptions.WechatSogouArticleDeletedError('article is deleted, {}'.format(origin_url))
        elif u'此帐号已自主注销，内容无法查看' in response.text:
            raise ws_exceptions.WechatSogouAccountCancelError('account has been canceled, {}'.format(origin_url))
        articles = WechatSogouParse.parse_gzh_article_list(resp_text=response.text)
        return articles

    def get_article_content(self, keyword, article_url, identify_image_callback=None, is_raw=False):
        """
        获取文章详情
        :param keyword: 关键字
        :param article_url: 文章URL
        :param identify_image_callback: 自定义验证码识别方法,(默认使用超级鹰,需要提供账号密码)
        :param is_raw: 是否只返回HTML, True返回, False不返回, 默认False
        :return:
        """
        if identify_image_callback is None:
            # identify_image_callback = self._identify_image_by_chaojiying
            # identify_image_callback = self._identify_image_by_hand
            identify_image_callback = self._identify_image_by_bearcat
        assert callable(identify_image_callback)

        origin_url = article_url
        if article_url.startswith(('https://weixin.sogou.com', 'http://weixin.sogou.com')):
            article_url = self._decode_url(origin_url=article_url,
                                           referer=self._gen_search_list_url(keyword=keyword, page=1,
                                                                             url_type='article'),
                                           identify_image_callback=identify_image_callback)
        response = self._get_page(url=article_url,
                                  identify_image_callback=identify_image_callback,
                                  platform='wechat')
        if u'链接已过期' in response.text:
            raise ws_exceptions.WechatSogouUrlExpireError('url is expire, {}'.format(origin_url))
        elif u'该内容已被发布者删除' in response.text:
            raise ws_exceptions.WechatSogouArticleDeletedError('article is deleted, {}'.format(origin_url))
        elif u'此帐号已自主注销，内容无法查看' in response.text:
            raise ws_exceptions.WechatSogouAccountCancelError('account has been canceled, {}'.format(origin_url))
        if is_raw:
            return response.text
        content = WechatSogouParse.parse_article_detail(resp_text=response.text)
        return content


if __name__ == '__main__':
    pass

