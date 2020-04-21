#!/usr/bin/python
# coding: utf-8
import mimetypes
import sys
import urllib
import urllib2

import os
import stat

'''
/**
 * 敬告使用者
 *
 * 接口、实例文件，均为第三方开发，因技术原因，联众识图平台未进行代码审查，亦不能确定代码的功能作用，请接入的开发者审查代码后调用。如实例中包含恶意代码或针对某网站、软件的攻击行为，请联系联众识图平台删除。
 *
 * 联众识别平台仅为残障人士以及有需要的个人和企业提供图像识别和图像识别分类服务，联众平台仅仅被动接受开发者传入的图像返回图像中的文字或结果信息，不参与破解，不为恶意软件提供帮助，不针对任何网站或个人。
 * 请勿利用联众识别做违反国家法律法规的行为，否则强制停止使用，不予退费，联众将依法向有关部门递交您的个人资料！
 * 违法软件是指的是包括但不限于以下用途的软件：
 * 1、破解、入侵系统，或正常登录但超越授权范围获取信息。
 * 2、赌博
 * 3、薅羊毛
 * 4、批量登录、批量注册、批量支付
 * 5、游戏外挂、游戏辅助
 * 6、超越访问频率限制
 * 7、批量盗取公民个人信息，获取手机号、身份证等隐私信息
 *
 */
'''


class Callable:
    def __init__(self, anycallable):
        self.__call__ = anycallable


doseq = 1


class MultipartPostHandler(urllib2.BaseHandler):
    handler_order = urllib2.HTTPHandler.handler_order - 10  # needs to run first

    def http_request(self, request):
        data = request.get_data()
        if data is not None and type(data) != str:
            v_files = []
            v_vars = []
            try:
                for (key, value) in data.items():
                    if type(value) == file:
                        v_files.append((key, value))
                    else:
                        v_vars.append((key, value))
            except TypeError:
                systype, value, traceback = sys.exc_info()
                raise TypeError, "not a valid non-string sequence or mapping object", traceback

            if len(v_files) == 0:
                data = urllib.urlencode(v_vars, doseq)
            else:
                boundary, data = self.multipart_encode(v_vars, v_files)
                contenttype = 'multipart/form-data; boundary=%s' % boundary
                if (request.has_header('Content-Type')
                        and request.get_header('Content-Type').find('multipart/form-data') != 0):
                    print "Replacing %s with %s" % (request.get_header('content-type'), 'multipart/form-data')
                request.add_unredirected_header('Content-Type', contenttype)

            request.add_data(data)
        return request

    def multipart_encode(vars, files, boundary=None, buffer=None):
        if boundary is None:
            boundary = "--1234567890"
        if buffer is None:
            buffer = ''
        for (key, value) in vars:
            buffer += '--%s\r\n' % boundary
            buffer += 'Content-Disposition: form-data; name="%s"' % key
            buffer += '\r\n\r\n' + value + '\r\n'
        for (key, fd) in files:
            file_size = os.fstat(fd.fileno())[stat.ST_SIZE]
            filename = fd.name.split('/')[-1]
            contenttype = mimetypes.guess_type(filename)[0] or 'application/octet-stream'
            buffer += '--%s\r\n' % boundary
            buffer += 'Content-Disposition: form-data; name="%s"; filename="%s"\r\n' % (key, filename)
            buffer += 'Content-Type: %s\r\n' % contenttype
            fd.seek(0)
            buffer += '\r\n' + fd.read() + '\r\n'
        buffer += '--%s--\r\n\r\n' % boundary
        return boundary, buffer

    multipart_encode = Callable(multipart_encode)
    https_request = http_request


def main(api_username, api_password, img_url, api_post_url, yzm_min='', yzm_max='', yzm_type='', tools_token=''):
    import tempfile

    validatorURL = api_post_url
    opener = urllib2.build_opener(MultipartPostHandler)

    if yzm_min == '':
        yzm_min = '4'
    if yzm_max == '':
        yzm_max = '4'

    def validateFile(url):
        temp = tempfile.mkstemp(suffix=".png")
        os.write(temp[0], opener.open(url).read())
        params = {"user_name": '%s' % api_username,
                  "user_pw": "%s" % api_password,
                  "yzm_minlen": "%s" % yzm_min,
                  "yzm_maxlen": "%s" % yzm_max,
                  "yzmtype_mark": "%s" % yzm_type,
                  "zztool_token": "%s" % tools_token,
                  "upload": open(temp[1], "rb")
                  }

        print opener.open(validatorURL, params).read()

    validateFile(img_url)


if __name__ == "__main__":
    main('cheanchun',
         'p8dVu2XLverRVYU',
         'https://www.jsdati.com/captcha/login?_=khPsmgzOeFNxjGkA',
         "http://v1-http-api.jsdama.com/api.php?mod=php&act=upload",
         '',
         '',
         '',
         '')

    '''
    main() 参数介绍
    api_username    （API账号）             --必须提供
    api_password    （API账号密码）         --必须提供
    img_url         （需要识别的图片URL）  --必须提供
    api_post_url    （API接口地址）         --必须提供
    yzm_min         （识别最小值）        --可空提供
    yzm_max         （识别最大值）        --可空提供
    yzm_type        （识别类型）          --可空提供
    tools_token     （工具或软件token）     --可空提供
   '''
