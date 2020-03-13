"""
使用正则表达式将headers转换成python字典格式的工具函数
"""

# import utils:
import re


def headers_formatter(headers_str):
    for string in headers_str.strip().splitlines():
        print(re.sub(r'^(.*?):\s*(.*)$', r"'\1': '\2',", string))


headers_str = """

Accept-Encoding: identity;q=1, *;q=0
Range: bytes=0-
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36
"""

if __name__ == '__main__':
    headers_formatter(headers_str)
    # print(headers_formatter(headers_str))
