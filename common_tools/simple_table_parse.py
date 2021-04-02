#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Alex
@date: 2020/06/29 15:02:38
@file: simple_table_parse.py
@usage: 简单表格解析，只能解析一层表格，返回二维列表
"""
from lxml import etree


class SimpleTableParse(object):
    def __init__(self, html_text=None, table_xpath=None, table=None):
        """
        初始化
        :param html_text: 页面文本
        :param table_xpath: table xpath
        :param table: table element
        """
        if html_text and table_xpath:
            self.html = etree.HTML(html_text)
            self.table_html = self.html.xpath(table_xpath)
            if not self.table_html:
                raise ValueError('table xpath can not parse element')
            self.table_html = self.table_html[0]
        elif table:
            self.table_html = table
        else:
            raise ValueError('table xpath is empty')

        self.array_list = None

    def init_true_table(self):
        """
        根据表格行列，初始化二维列表
        :return:
        """
        self.array_list = []
        cols_num = []
        for tr in self.trs:
            num = 0
            tds = tr.xpath('./th|./td')
            for td in tds:
                if td.xpath('./@colspan'):
                    num += int(''.join(td.xpath('./@colspan')).strip())
                else:
                    num += 1
            cols_num.append(num)
        cols = max(cols_num)
        rows = len(self.trs)
        for row in range(rows):
            new_list = []
            for col in range(cols):
                new_list.append('$')
            self.array_list.append(new_list)

    def get_table_data(self):
        """
        获取table数据
        :return:
        """
        tr_len = len(self.trs)
        for tri in range(tr_len):
            tds = self.trs[tri].xpath('./th|./td')
            td_len = len(tds)
            for tdi in range(td_len):
                rowspan = ''.join(tds[tdi].xpath('./@rowspan')).strip()
                colspan = ''.join(tds[tdi].xpath('./@colspan')).strip()
                data = ''.join(tds[tdi].xpath('.//text()')).strip()
                if rowspan:
                    self.fill_table_data(index_y=tri, data=data, direction='y', length=int(rowspan))
                elif colspan and not rowspan:
                    self.fill_table_data(index_y=tri, data=data, direction='x', length=int(colspan))
                elif colspan and rowspan:
                    self.fill_table_data(index_y=tri, data=data, direction='x', length=int(colspan) - 1)
                else:
                    self.fill_table_data(index_y=tri, data=data, direction='x', length=1)

    def fill_table_data(self, index_y, data, direction, length):
        """
        填充数据
        :param index_y:
        :param data:
        :param direction:
        :param length:
        :return:
        """
        data_list = self.array_list[index_y]
        index_x = data_list.index('$')
        for i in range(length):
            if direction == 'x':
                self.array_list[index_y][index_x] = data
                index_x += 1
            else:
                self.array_list[index_y][index_x] = data
                index_y += 1

    def parse_table(self):
        """
        开始解析
        :return:
        """
        self.trs = self.table_html.xpath('.//tr')
        self.init_true_table()
        self.get_table_data()
        return self.array_list


if __name__ == '__main__':
    table_str = """"""
    res = SimpleTableParse(html_text=table_str, table_xpath='//table').parse_table()

