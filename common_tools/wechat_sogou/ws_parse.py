#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Alex
@date: 2020/08/19 10:47:47
@file: ws_parse.py
@usage: 搜狗微信解析
"""
import re

from lxml import etree


class WechatSogouParse(object):
    @staticmethod
    def parse_sogou_article_list(resp_text=None):
        """
        解析文章列表页
        :param resp_text:
        :return:
        """
        if not resp_text:
            return None
        html = etree.HTML(resp_text)
        lis = html.xpath('//ul[@class="news-list"]/li')
        articles = []
        for li in lis:
            origin_url = ''.join(li.xpath('./div[@class="txt-box"]/h3/a/@href')).strip()
            if origin_url.startswith('/link'):
                origin_url = 'https://weixin.sogou.com{}'.format(origin_url)
            title = ''.join(li.xpath('./div[@class="txt-box"]/h3/a//text()')).strip()
            summary = ''.join(li.xpath('./div[@class="txt-box"]/p[@class="txt-info"]//text()')).strip()
            gzh_name = ''.join(li.xpath('./div[@class="txt-box"]/div[@class="s-p"]/a//text()')).strip()
            gzh_url = ''.join(li.xpath('./div[@class="txt-box"]/div[@class="s-p"]/a/@href')).strip()
            if gzh_url.startswith('/link'):
                gzh_url = 'https://weixin.sogou.com{}'.format(gzh_url)
            time_text = ''.join(li.xpath('./div[@class="txt-box"]/div[@class="s-p"]/span/script/text()')).strip()
            publish_time = ''.join(re.findall(r'timeConvert\(\'(.*?)\'\)', time_text))
            articles.append({
                'origin_url': origin_url,
                'title': title,
                'summary': summary,
                'gzh_name': gzh_name,
                'gzh_url': gzh_url,
                'publish_time': publish_time,
            })
        return articles

    @staticmethod
    def parse_sogou_gzh_list(resp_text=None):
        """
        解析公众号列表页
        :param resp_text:
        :return:
        """
        if not resp_text:
            return None
        html = etree.HTML(resp_text)
        lis = html.xpath('//ul[@class="news-list2"]/li')
        gzh_list = []
        for li in lis:
            origin_url = ''.join(li.xpath('./div[@class="gzh-box2"]/div[@class="img-box"]/a/@href')).strip()
            if origin_url.startswith('/link'):
                origin_url = 'https://weixin.sogou.com{}'.format(origin_url)
            avatar = ''.join(li.xpath('./div[@class="gzh-box2"]/div[@class="img-box"]/a/img/@src')).strip()
            wechat_name = ''.join(
                li.xpath('./div[@class="gzh-box2"]/div[@class="txt-box"]/p[@class="tit"]/a//text()')).strip()
            wechat_id = ''.join(
                li.xpath('./div[@class="gzh-box2"]/div[@class="txt-box"]/p[@class="info"]/label/text()')).strip()
            wechat_desc = ''.join(li.xpath(u'./dl/dt[contains(string(), "功能介绍：")]/../dd//text()')).strip()
            wechat_authentication = ''.join(li.xpath(u'./dl/dt[contains(string(), "认证：")]/../dd//text()')).strip()
            article_url = ''.join(li.xpath(u'./dl/dt[contains(string(), "最近文章：")]/../dd/a//@href')).strip()
            if article_url and article_url.startswith('/link'):
                article_url = 'https://weixin.sogou.com{}'.format(article_url)
                article_title = ''.join(li.xpath(u'./dl/dt[contains(string(), "最近文章：")]/../dd/a//text()')).strip()
                time_text = ''.join(li.xpath(u'./dl/dt[contains(string(), "最近文章：")]/../dd/span/script/text()')).strip()
                article_time = ''.join(re.findall(r'timeConvert\(\'(.*?)\'\)', time_text))
            qrcode_url = ''.join(li.xpath('./div[@class="gzh-box2"]/div[@class="ew-pop"]/span/img[1]/@src')).strip()
            open_id = ''.join(li.xpath('./div[@class="gzh-box2"]/div[@class="ew-pop"]/span/img[1]/@data-id')).strip()

            articles = []
            if article_url:
                articles.append({
                    'article_title': article_title,
                    'article_time': article_time,
                    'article_url': article_url
                })
            gzh_list.append({
                'origin_url': origin_url,
                'avatar': avatar,
                'wechat_name': wechat_name,
                'wechat_id': wechat_id,
                'wechat_desc': wechat_desc,
                'wechat_authentication': wechat_authentication,
                'qrcode_url': qrcode_url,
                'open_id': open_id,
                'articles': articles
            })
        return gzh_list

    @staticmethod
    def parse_article_detail(resp_text=None):
        """
        解析文章内容
        :param resp_text:
        :return:
        """
        if not resp_text:
            return None
        html = etree.HTML(resp_text)
        article = {}
        article['title'] = ''.join(html.xpath('//h2[@class="rich_media_title"]/text()')).strip()
        time_temp = ''.join(re.findall(r'var t=.*?,n=.*?,s="(.*?)";', resp_text)).strip()
        if not time_temp:
            time_temp = ''.join(html.xpath('//span[@id="publish_time"]/text()')).strip()
        article['publish_time'] = time_temp
        article['author'] = ''.join(html.xpath('//meta[@property="og:article:author"]/@content')).strip()
        article['content'] = ''.join(html.xpath(
            '//div[@class="rich_media_content "]//*[name(.)!="script" and name(.)!="style"]/text()|//div[@class="rich_media_content "]/text()')).strip()
        article['site_name'] = ''.join(html.xpath('//meta[@property="og:site_name"]/@content')).strip()
        article['gzh_name'] = ''.join(html.xpath('//strong[@class="profile_nickname"]/text()')).strip()
        article['gzh_id'] = ''.join(html.xpath(u'//label[text()="微信号"]/../span/text()')).strip()
        article['gzh_desc'] = ''.join(html.xpath(u'//label[text()="功能介绍"]/../span/text()')).strip()
        return article

    @staticmethod
    def parse_gzh_article_list(resp_text=None):
        """
        搜狗已关闭此功能
        解析公众号详情页中的文章
        :param resp_text:
        :return:
        """
        if not resp_text:
            return None
        re.findall(r'var msgList = (.*?);', resp_text)
        return []

