#coding:utf-8
import re

from lxml.html import HtmlElement


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
            yield from iter_node(sub_element)