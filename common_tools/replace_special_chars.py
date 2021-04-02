#coding: utf-8
"""
替换文本中的需要自定义去除的特殊字符
ps:
   text = '\t\npls\r\u3000'
   replace_escape_chars(text)
   输出：
        pls
"""
import sys

PY_VERSION = sys.version_info[0]
if PY_VERSION == 2:
    text_type = unicode
if PY_VERSION == 3:
    text_type = str


def replace_special_chars(text, replaceed_chars=('\n', '\t', '\r', u'\u3000', u'\xa0', '\v', '&nbsp;'), replace_with=u'', encoding=None):
    """
    :param text: 替换文本
    :param replaceed_chars: 被替换的字符
    :param replace_with: 替换后的字符
    :param encoding: 文本编码
    :return: text
    """

    def to_unicode(text, encoding=None, errors='strict'):
        if isinstance(text, text_type):
            return text
        if not isinstance(text, (bytes, text_type)):
            return None  # 给定的文本类型不对 不是字符串
        if encoding is None:
            encoding = 'utf-8'
        return text.decode(encoding, errors)
        
    text = to_unicode(text, encoding)
    for char in replaceed_chars:
        text = text.replace(char, replace_with)
    return text
