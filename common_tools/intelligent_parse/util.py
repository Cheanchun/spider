#coding:utf-8
import re
from lxml.html import HtmlElement

DELETE_TAG = ["select","form","style", "script", "link", "video", "iframe", "source", "picture", "header", "blockquote", "head",
              "input"]
DELETE_CLASS = ["post","reply","footer","-right","menu","BodyEnd","AboutCtrl","Xgzx","card","user-info","yuedu","pinglun","shoucang","js-font","copyright","rightbox_title","interested-article-box","z_cen_wntj","rdph","pdtj","comment","nav",
                "news-links",
                "gives",
                "news-key",
                "hdear",
                "exceptional-box",
                "z_cen_sq",
                "news-push",
                "search",
                "machineContainer",
                "weixinloginedAlert",
                "hidden",
                "qrcode",
                "pagebottom",
                "Jdzt",
                "tuijian",
                "jump",
                "up_down",
                "login",
                "layer-reprinted",
                "swiper-slide",
                "foot"
                ]
HANDLE_TAG = [
    "b",
    "strong",
    "i",
    "em",
    "u"
]

def clean(text):
    text = re.sub(' +', ' ', text, flags=re.S)
    return text.strip()

def tags(html,element_list):
    for element in element_list:
        for e in html.findall(".//%s" % element):
            yield e

def iter_node(element):
    yield element
    for sub_element in element:
        if issubclass(type(sub_element),HtmlElement):
            for i in iter_node(sub_element):
                yield i

def _remove(node):
    parent = node.getparent()
    if parent is not None:
        parent.remove(node)