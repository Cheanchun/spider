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
              "//div[@class='rebox_news']/ul/li/a/@href",
              '3-fmprc',
              u"{}",
              u'中华人民共和国外交部',
              'abuyun',
              'policy:mofcom:fmprc{}',
              None,
              None,
              2),
            """
            wp.write(con.format(site.strip(), col, cnt) + '\n')
            content = fp.readline()
