# coding:utf-8
# 智能解析网页
import re
from html import unescape

import numpy as np
import util
from lxml.html import fromstring, etree
from page import Response

DELETE_TAG = ["style", "script", "link", "video", "iframe", "source", "picture", "header", "blockquote", "head",
              "input"]
DELETE_CLASS = ["reply", "footer", "right", "menu", "BodyEnd", "AboutCtrl", "Xgzx", "card", "user-info", "yuedu",
                "pinglun", "shoucang", "js-font"]


class IntelligentParse:
    """
        第一获取网页源码 同时去除js 样式 Iframe等
        第二步计算每一个节点的要求的变量（进行对应的数学计算）
            数学计算分为三步：
                1.TDi计算
                2.sbDi计算
                3.score计算
            以最后score的值进行判断是否为正文文本
        """

    def __init__(self, url, method="GET", custom_delete_class=None):
        self.url = url
        self.method = method
        self.custome_delete_clss = custom_delete_class
        self.math_value_info = {}
        self.element = None

    def intelligent_main(self):
        # 1.进行页面的预处理
        self.pretreat()  # 1

        # 2.进行数学的函数运算 得出最佳值
        # 优化--------->
        # for node in self.iter_node(self.element):
        for node in util.iter_node(self.element):
            node_flag = hash(node)
            # 2.1 进行TDI的计算
            tdi, ti, lti, tgi, ltgi, node_text, html_node = self.math_treat_tdi(node=node)  # 2
            # print(tdi,ti,lti,tgi,ltgi,node_text)

            # 2.2 计算文本的符号密度 sbdi
            sbdi = self.math_treat_sbdi(ti=ti, lti=lti, node_text=node_text)  # 3

            # 2.3 获取节点的p标签数 pnumi
            node_p_list = node.xpath(".//p")
            pnumi = len(node_p_list)
            self.math_value_info[node_flag] = [tdi, ti, lti, tgi, ltgi, node_text, html_node, sbdi, pnumi]

        # 3.进行score的计算
        html = self.math_treat_score()  # 4
        print(html)

    # 1
    def pretreat(self):
        # html = requests.get(url=self.url).content.decode("utf-8")
        html = Response().response(url=self.url, method=self.method)
        html = re.sub('</?br.*?>', '', html)
        element = fromstring(html)
        etree.strip_elements(element, *DELETE_TAG)
        # 优化---------->
        # for node in self.iter_node(element):
        for node in util.iter_node(element):
            # 1.先将不是p标签，但是该标签下有文本同时没有子标签的标签改为p标签
            if node.tag.lower() == "div" or node.tag.lower() == "span":
                if node.text and node.text.strip() and not node.getchildren():
                    node.tag = "p"
            # 2.将标签下没有文本同时没有子标签的标签移除掉
            if not node.text and not node.getchildren() and node.tag.lower() != "img":
                node.drop_tree()

            # 3.将没有内容的p标签去除
            if node.tag.lower() == 'p' and not node.xpath('.//img'):
                if not (node.text and node.text.strip()):
                    parent = node.getparent()
                    if parent is not None:
                        node.drop_tag()
            # 4.去除一些不需要的class 对应的标签
            class_name = node.get('class', '')
            if class_name:
                if self.custome_delete_clss:
                    DELETE_CLASS.extend(self.custome_delete_clss)
                for attribute in DELETE_CLASS:
                    if attribute.lower() in class_name.lower():
                        parent = node.getparent()
                        if parent is not None:
                            parent.remove(node)
                        break
            # 5.ul下li标签太多时去除该标签
            if node.tag.lower() == "ul":
                li_num = len(node.xpath(".//li"))
                # li标签是否有a标签
                for _ in node.getchildren():
                    if _.xpath('.//a') and li_num >= 2:
                        parent = node.getparent()
                        if parent is not None:
                            parent.remove(node)
                        break

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

        node_hash = hash(node)
        # 1.获取节点 node
        # 2.计算节点的文本长度 ti
        node_text = util.clean(text=node.text_content().strip())
        ti = len(node_text)
        # 对带有class特别明显的标签进行加分
        tag_class = node.get('class', '')
        if re.compile('|'.join(["content",
                                "news_txt",
                                "article"])).search(tag_class.lower()):
            ti = 2.5 * ti

        # 3.计算节点带链接的文本长度 lti
        node_as_text_list = []
        for node_a in util.tags(html=node, element_list=["a"]):
            # 3.1获取节点带链接的节点 node_a 以及文本长度
            node_a_text = util.clean(node_a.text_content())
            # print(node_a_text)
            node_as_text_list.append(len(node_a_text))
        lti = sum(node_as_text_list)

        # 4.计算节点标签数 tgi
        tgi = len(node.xpath('.//*'))

        # 5.计算节点带链接的标签数 ltgi
        ltgi = len(node.xpath('.//a'))

        html_node = unescape(etree.tostring(node, encoding='utf-8').decode())
        # html_node = node

        # 6.计算文本密度tdi
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
        # 1.获取文本中符号的数量 sbi
        CHAR = set(u'''！，。？、；：“”‘’《》%（）,.?:;'"!%()''')
        char_count = 0
        for char in node_text:
            if char in CHAR:
                char_count += 1
        sbi = char_count
        # 2.计算文本的符号密度 sbdi
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
        # 节点文本密度
        ndi = [v[0] for v in self.math_value_info.values()]
        # print(ndi)

        # 节点文本密度ndi的标准差 sd
        sd = np.std(ndi, ddof=1)
        # print(sd)

        # 计算score值
        score_info = {}
        for node_hash, node_info in self.math_value_info.items():
            score = np.log(sd) * node_info[0] * np.log10(node_info[-1] + 2) * np.log(node_info[-2])
            score_info[node_hash] = {
                "score": score,
                "html": node_info[-3]
            }
        k = sorted(score_info.items(), key=lambda x: x[1]["score"], reverse=True)
        return k[0][1]["html"]
