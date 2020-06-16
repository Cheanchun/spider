# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""

cnt = 0
with open('info.txt', mode='r') as fp:
    with open('sel_config.py', mode='a+') as wp:
        content = fp.readline()
        while content:
            cnt += 1
            col, site = content.split('\t')[0], content.split('\t')[1]
            col = col.strip('"')
            con = """
    {
        "site_config": {
            'index_url': '"""+site.strip()+"""',
            'list_parse_rule': "//div[@class='w1']/ul/li/span[1]/a",
            'total_page': 1,  # 
            'handler': '3-seac',
            'category': '"""+col+"""',
            'website': '中华人民共和国国家民族事务委员会',
            'redis_key': 'policy:audit:seac-"""+str(cnt)+"""',
        },
        "sel_config": {
            'chrome_init': ['acceptSslCerts'],
            'proxy_type': '',
            'next_page_btn': {
                'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
                'by_id': '',
                'by_class': '',
            },
            'waiting_page': {
                'by_xpath': "",
                'by_id': '',
                'by_class': '',
            },
        },
    },
            """
            wp.write(con + '\n')
            content = fp.readline()
