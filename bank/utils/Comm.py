# coding=utf-8
import json

import requests
from lxml.etree import _Element

default_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36",

}


class CommSession(object):
    def __init__(self, headers=None, verify=False):
        self._session = requests.session()
        if not headers:
            self._session.headers = default_headers
        self._session.verify = verify

    def session(self, index_url=None):
        if index_url:
            self._session.get(index_url)
        return self._session


# t = u"""
# <table cellspacing="0" cellpadding="0" align="center">
#     <tbody>
#         <tr>
#             <td>产品代码</td>
#             <td colspan="3">90514043</td>
#         </tr>
#         <tr>
#             <td>预约申购期(起)</td>
#             <td>2017-04-21 18:00至23:59:59</td>
#             <td>预约申购期(止)</td>
#             <td>2017-04-26 18:00至23:59:59</td>
#         </tr>
#         <tr>
#             <td>投资周期起始日/申购确认日</td>
#             <td>2017-04-28</td>
#             <td>投资周期终止日</td>
#             <td>2017-06-23</td>
#         </tr>
#         <tr>
#             <td>当期投资周期期限(天)</td>
#             <td>56</td>
#             <td>理财收益支付日</td>
#             <td>2017-06-23</td>
#         </tr>
#         <tr>
#             <td>当期客户理财参考年化净收益率/开放日净值</td>
#             <td>4.4500%</td>
#             <td>当期销售管理费率</td>
#             <td>0.3000%</td>
#         </tr>
#         <tr>
#             <td>预约赎回期(起)</td>
#             <td>2017-04-28 18:00至23:59:59</td>
#             <td>预约赎回期(止)</td>
#             <td>2017-06-21 18:00至23:59:59</td>
#         </tr>
#         <tr>
#             <td>赎回确认日/兑付日</td>
#             <td colspan="3">2017-06-23</td>
#         </tr>
#     </tbody>
# </table>
# """
# from lxml import etree
# fp = open('../../t.html',mode='r')
# content = fp.read()
# ta = etree.HTML(content.decode('u8'))


def table_parse(table):
    # print type(table)
    assert isinstance(table, _Element)
    # print len(table.xpath('//tr'))
    sqe = []
    td_cols = []
    for tr in table.xpath('//tr'):
        # print len(tr.xpath('//td'))
        col_count = 0
        col = []
        for td_col in tr.xpath('.//td'):
            current_len = int(td_col.xpath('./@colspan')[0]) if td_col.xpath('./@colspan') else 1
            col_count += current_len
            for i in range(current_len):
                col.append(td_col.xpath('normalize-space(string(.))'))
        sqe.append(col)
        # td_cols.append(col_count)
        # print '-' * 50
    # print 'raw:{}'.format(len(table.xpath('//tr')))
    # print 'col:{}'.format(max(td_cols))
    # print json.dumps(sqe, ensure_ascii=False, encoding='u8')
    for raw in sqe:
        print(json.dumps(raw, ensure_ascii=False, encoding='u8'))

if __name__ == '__main__':
    pass
    # table_parse(ta)
