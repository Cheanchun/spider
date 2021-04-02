#!/usr/bin/env python
# coding:utf-8

from hashlib import md5

import requests

from common_tools import config


class ChaojiyingClient(object):

    def __init__(self, username=None, password=None, soft_id=None):
        if username is None:
            username = config.CHAOJIYING_USERNAME
            password = config.CHAOJIYING_PASSWORD
            soft_id = config.CHAOJIYING_SOFT_ID
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def post_pic(self, img, code_type):
        """
        im: 图片字节
        code_type: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': code_type,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', img)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def report_error(self, img_id):
        """
        img_id:报错题目的图片ID
        """
        params = {
            'id': img_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    chaojiying = ChaojiyingClient('cheanchun', 'PdrU3m6yBbB4J95', '899598')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('./pic/test.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    res = chaojiying.post_pic(im, 1006)  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    print res.get("err_str")

