# coding:utf-8
# 智能解析网页
import re
import numpy as np
from lxml.etree import tounicode
from lxml.html import fromstring, etree, HtmlElement
# from html import unescape

import util
from page import Response


class IntelligentParse:
    """
        one.获取网页源码 同时去除js 样式 Iframe等
        two.计算每一个节点的要求的变量（进行对应的数学计算）
            数学计算分为三步：
                1.TDi计算
                2.sbDi计算
                3.score计算
            以最后score的值进行判断是否为正文文本
    """

    def __init__(self, url=None, page_source=None, method="GET", custom_delete_class=None):
        """
        :param url: 
        :param page_source: 
        :param method: 
        :param custom_delete_class: 
        """
        self.url = url
        self.page_source = page_source
        self.method = method
        self.custome_delete_clss = custom_delete_class
        self.math_value_info = {}
        self.element = None

    def intelligent_main(self):
        self.pretreat()  # 1
        for node in util.iter_node(self.element):
            node_flag = hash(node)
            # 2.1 进行TDI的计算
            tdi, ti, lti, tgi, ltgi, node_text, html_node = self.math_treat_tdi(node=node)  # 2

            # 2.2 计算文本的符号密度 sbdi
            sbdi = self.math_treat_sbdi(ti=ti, lti=lti, node_text=node_text)  # 3

            # 2.3 获取节点的p标签数 pnumi
            node_p_list = node.xpath(".//p")
            pnumi = len(node_p_list)
            self.math_value_info[node_flag] = [tdi, ti, lti, tgi, ltgi, node_text, html_node, sbdi, pnumi]
        # 3.进行score的计算
        html = self.math_treat_score()
        return html.replace("\n","").replace("\r","").replace("\t","").strip()

    # 1
    def pretreat(self):
        if self.page_source:
            html = self.page_source
        else:
            html = Response().response(url=self.url, method=self.method)
        html = re.sub('</?br.*?>', '', html)
        element = fromstring(html)
        etree.strip_elements(element, *util.DELETE_TAG)
        # 优化---------->
        for node in util.iter_node(element):
            if node.tag == "div":
                if node.text and len(node.text.strip()) > 30 and not len(node.getchildren()):
                    util._remove(node) #于03-16优化

            if node.tag.lower() == "div" or node.tag.lower() == "span":
                if node.text and node.text.strip() and not node.getchildren():
                    node.tag = "p"

            if not node.text and not node.getchildren() and node.tag.lower() != "img":
                util._remove(node) #于03-16优化

            if node.tag.lower() == 'p' and not node.xpath('.//img'):
                if not (node.text and node.text.strip()):
                    parent = node.getparent()
                    if parent is not None:
                        node.drop_tag()

            class_name = node.get('class', '')
            if class_name:
                if self.custome_delete_clss:
                    util.DELETE_CLASS.extend(self.custome_delete_clss)
                for attribute in util.DELETE_CLASS:
                    if attribute.lower() in class_name.lower():
                        util._remove(node) #于03-16优化
                        break

            if node.tag.lower() == "ul":
                li_num = len(node.xpath(".//li"))
                for _ in node.getchildren():
                    if _.xpath('.//a') and li_num >= 2:
                        util._remove(node) #于03-16 优化
                        break

            if node.tag == "img":
                if not re.compile("http(s)?").search(node.attrib.get("src","")):
                    util._remove(node) #于03-16优化

        self.element = element

    # 2
    def math_treat_tdi(self, node):
        """
        计算文本密度TDI的值 
        公式：
            TDi = (Ti - LTi)  / (TGi - LTGi)
        参数：
            Ti-->节点i的字符串数 即就是节点i的文本长度
            LTi-->节点i带链接的字符串数 即就是节点i带链接的文本的长度
            TGi-->节点i的标签数
            LTGi-->节点i带链接的标签数
        步骤：
            1.得到节点
            2.计算节点的文本长度
            3.计算节点带链接的文本长度
            4.计算节点的标签数
            5.计算节点带链接的标签数
        """
        # print(node)
        node_text = util.clean(text=node.text_content().strip())
        ti = len(node_text)
        tag_class = node.get('class', '')
        if re.compile('|'.join(["content",
                                "news_txt",
                                "article"])).search(tag_class.lower()):
            ti = 2.5 * ti

        node_as_text_list = []
        for node_a in util.tags(html=node, element_list=["a"]):
            node_a_text = util.clean(node_a.text_content())
            node_as_text_list.append(len(node_a_text))
        lti = sum(node_as_text_list)

        tgi = len(node.xpath('.//*'))

        ltgi = len(node.xpath('.//a'))

        # html_node = unescape(etree.tostring(node, encoding='utf-8').decode())
        html_node = tounicode(node)


        if (tgi - ltgi) == 0:
            return 0, ti, lti, tgi, ltgi, node_text, html_node
        tdi = (ti - lti) / (tgi - ltgi)
        return tdi, ti, lti, tgi, ltgi, node_text, html_node

    # 3
    def math_treat_sbdi(self, ti, lti, node_text):
        """
        计算文本中符号密度 sbdi值
        公式：
            sbdi = (ti - lti) / (sbi + 1)
        参数：
            sbi-->文本中符号的数量
        """
        CHAR = set(u'''！，。？、；：“”‘’《》%（）,.?:;'"!%()''')
        char_count = 0
        for char in node_text:
            if char in CHAR:
                char_count += 1
        sbi = char_count
        sbdi = (ti - lti) / (sbi + 1)
        if not sbdi:
            return 1
        return sbdi

    # 4
    def math_treat_score(self):
        """
        计算score的值
        公式：
            score = log(sd)*ndi*log10(pnumi + 2)*log(sbdi)
        参数：
            sd-->ndi的标准差
            ndi-->文本密度
            pnumi-->节点的p标签数
        """
        ndi = [v[0] for v in self.math_value_info.values()]

        sd = np.std(ndi, ddof=1)

        score_info = {}
        for node_hash, node_info in self.math_value_info.items():
            score = np.log(sd) * node_info[0] * np.log10(node_info[-1] + 2) * np.log(node_info[-2])
            score_info[node_hash] = {
                "score": score,
                "html": node_info[-3]
            }
        k = sorted(score_info.items(), key=lambda x: x[1]["score"], reverse=True)
        #后备补充处理
        html = k[0][1]["html"]
        element = fromstring(html)

        for _ in util.iter_node(element):
            for elem in _.getchildren():
                if isinstance(type(elem),object) and len(elem):
                    link_length = 0
                    for i in elem.findall(".//a"):
                        link_length += self.text_length(i)
                    total_length = self.text_length(elem)
                    link_density =float(link_length) / max(total_length, 1)
                    weight = total_length
                    delete_flag = link_density*10/(weight or 1000000)*1000
                    if delete_flag > 0.5 and elem.tag not in ["p","span","strong"]:
                        if elem.tag == "div":
                            a_num = [i.tag for i in elem.getchildren() if i.tag == "a"]
                            p_num = len(elem.findall('.//p'))
                            if not p_num or (p_num and len(a_num) > p_num):
                                elem.drop_tree()
            #特殊网站处理
            if _.tag == "a" and "id" in _.attrib.keys():
                _.tag = "div"
        return tounicode(element)
        # return unescape(etree.tostring(element, encoding='utf-8').decode())

    def text_length(self,e):
        return len(util.clean(e.text_content() or ""))
