#!/usr/bin/env python
# coding:utf-8
import base64

import requests


class IdentifyCaptcha(object):
    def __init__(self):
        self.identify_url = 'http://55.24.8.101:5006'  # post

    def post_pic(self, img):
        """
        发送图片，获取识别后的结果
        :param img:  图片字节
        :return:
        """
        res = requests.post(url=self.identify_url, data={'img': base64.b64encode(img)})
        return res.json()

