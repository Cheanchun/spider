# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""

cnt = 0
with open('info.txt',mode='r') as fp:
    with open('config.py', mode='a+') as wp:
        content = fp.readline()
        while content:

            cnt += 1
            col, site = content.split('\t')[0], content.split('\t')[1]
            col = col.strip('"')
            con = """
    UrlConfig("{}",
              "",
              1,
              "//ul[@class='xwfb_listbox']/li/a/@href",
              '1-proxy-mof',
              u"{}",
              u'中华人民共和国财政部',
              None,
              'policy:mofcom:mof{}',
              None,
              None,
              2),
            """
            wp.write(con.format(site.strip(), col, cnt) + '\n')
            content = fp.readline()
