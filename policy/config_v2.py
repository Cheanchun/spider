# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
config = [
    {
        "site_config": {
            'index_url': 'http://www.customs.gov.cn/customs/zsgk93/302256/302257/index.html',
            'list_parse_rule': "//div/ul[@class='conList_ul']/li/a",
            'total_page': 33,
            'handler': '1-proxy-nao',
            'category': '首页>公开目录',
            'website': '审计署',
            'redis_key': 'policy:audit:audit_gdnps',
        },
        "sel_config": {
            'chrome_init': ['acceptSslCerts'],
            'proxy_type': '',
            'next_page_btn': {
                'by_xpath': "//div[@class='easysite-page-wrap']/a[3]",
                'by_id': '',
                'by_class': '',
            },
            'waiting_page': {
                'by_xpath': "//div[@class='easysite-page-wrap']/a[3]",
                'by_id': '',
                'by_class': '',
            },
        },
    }
]
