#coding:utf-8
import requests

HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"
    }

CHARSETS = {
    'big5': 'big5hkscs',
    'gb2312': 'gb18030',
    'ascii': 'utf-8',
    'maccyrillic': 'cp1251',
    'win1251': 'cp1251',
    'win-1251': 'cp1251',
    'windows-1251': 'cp1251',
}

class Response:

    def response(self,url, method, params=None, data=None,custom_char=None):
        RETRY_NUM = 1
        while True:
            try:
                if method.lower() == "get":
                    response = requests.get(url=url, headers=HEADERS, params=params)
                if method.lower() == "post":
                    response = requests.post(url=url, headers=HEADERS, data=data)
                if response.apparent_encoding == "Windows-1254":
                    page = response.content.decode("iso-8859-9").encode("iso-8859-9")
                    return page
                else:
                    encoding = response.apparent_encoding
                    encoding = encoding.lower()
                    if custom_char:
                        CHARSETS.update(custom_char)
                    return response.content.decode(CHARSETS.get(encoding, encoding), "replace")
            except Exception as e:
                if RETRY_NUM < 4:
                    RETRY_NUM += 1
                    continue
                else:
                    return None
