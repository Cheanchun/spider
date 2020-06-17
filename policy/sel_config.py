# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
config = (
    # {
    #     "site_config": {
    #         'index_url': 'http://www.cde.org.cn/regulat.do?method=getList&fclass=all&year=all',
    #         'list_parse_rule': "//tbody/tr/td[2]/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-cde',
    #         'category': '法规与规章 >> 中心规章',
    #         'website': '国家药品审计中心',
    #         'redis_key': 'policy:audit:cde',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='easysite-page-wrap']/a[3]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//table/tbody/tr/td[1]/font/a[2]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://interview.mofcom.gov.cn/mofcom_interview/front/swfg/view',
    #         'list_parse_rule': "//td/div[@class='art-tit']/a",
    #         'total_page': 3,  # 71
    #         'handler': '1-proxy-mfm',
    #         'category': '首页 > 商务法规库',
    #         'website': '中华人民共和国商务部',
    #         'redis_key': 'policy:audit:mfm',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@id='next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://xxgk.spb.gov.cn/extranet/index.html',
    #         'list_parse_rule': "//table[@class='table']/tbody/tr/td/a",
    #         'total_page': 3,  # 50
    #         'handler': '3-spb',
    #         'category': '信息公开 > 公开指南 > 政务信息公开目录',
    #         'website': '国家邮政局',
    #         'redis_key': 'policy:audit:spb',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//p/span[@class='next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//table[@class='table']/tbody/tr/td/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.shclearing.com/cpyyw/tzgg/',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 3,  # 18
    #         'handler': '3-shclearing',
    #         'category': '首页 >> 产品与业务 >> 通知公告',
    #         'website': '上海清算所',
    #         'redis_key': 'policy:audit:shclearing-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='gray_text12'][10]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.shclearing.com/cpyyw/czxzjzn/',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 3,  # 18
    #         'handler': '3-shclearing',
    #         'category': 首页 >> 产品与业务 >> 操作须知与指南',
    #         'website': '上海清算所',
    #         'redis_key': 'policy:audit:shclearing-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='gray_text12'][10]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.shclearing.com/cpyyw/ywgz/',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '3-shclearing',
    #         'category': '首页 >> 产品与业务 >> 业务规则',
    #         'website': '上海清算所',
    #         'redis_key': 'policy:audit:shclearing-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='gray_text12'][10]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.shclearing.com/cpyyw/ywgz/',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '3-shclearing',
    #         'category': '首页 >> 产品与业务 >> 业务规则',
    #         'website': '上海清算所',
    #         'redis_key': 'policy:audit:shclearing-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='gray_text12'][10]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/wjw/hygq/list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list mt20']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '首页 > 新闻 > 回应关切',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list mt20']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/wjw/zcfg/list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list mt20']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '首页 > 信息 > 政策法规',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list mt20']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/wjw/gztz/list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list mt20']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '首页 > 信息 > 工作通知',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list mt20']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/wjw/rsxx/list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list mt20']/li/a",
    #         'total_page': 1,  # 1
    #         'handler': '2-nhc',
    #         'category': '首页 > 信息 > 人事信息',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list mt20']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/wjw/zqyj/list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list mt20']/li/a",
    #         'total_page': 2,  # 5
    #         'handler': '2-nhc',
    #         'category': '首页 > 互动 > 征求意见',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-5',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list mt20']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/wjw/gongs/list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list mt20']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '首页 > 新闻 > 公示',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-6',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list mt20']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/wjw/gfxwjj/list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list mt20']/li/a",
    #         'total_page': 2,  # 42
    #         'handler': '2-nhc',
    #         'category': '首页 > 信息 > 政策法规',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-7',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list mt20']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/wjw/zcjd/list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list mt20']/li/a",
    #         'total_page': 2,  # 6
    #         'handler': '2-nhc',
    #         'category': '首页 > 信息 > 政策法规 > 政策解读',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-8',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list mt20']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/wjw/rdts/list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list mt20']/li/a",
    #         'total_page': 2,  # 11
    #         'handler': '2-nhc',
    #         'category': '首页 > 信息',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-9',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list mt20']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/bgt/zcwj2/new_zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 3
    #         'handler': '2-nhc',
    #         'category': '办公厅 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-10',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/bgt/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '办公厅 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-11',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/guihuaxxs/pqt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-nhc',
    #         'category': '规划发展与信息化司 > 最新信息',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-12',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/guihuaxxs/zcwj2/zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_lis zcwjlist']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-nhc',
    #         'category': '规划发展与信息化司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-13',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_lis zcwjlist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/guihuaxxs/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-nhc',
    #         'category': '规划发展与信息化司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-14',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/caiwusi/zcwj2/new_zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 8
    #         'handler': '2-nhc',
    #         'category': '财务司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-15',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "ul[@class='zxxx_list zcwjlist']/li[1]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/caiwusi/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 13
    #         'handler': '2-nhc',
    #         'category': '财务司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-16',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/fzs/zcwj2/new_zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '法规司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-17',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/fzs/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 1,  # 9
    #         'handler': '2-nhc',
    #         'category': '法规司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-18',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/fzs/pqt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 35
    #         'handler': '2-nhc',
    #         'category': '法规司 > 最新信息',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-19',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/tigs/zcwj2/new_zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 3
    #         'handler': '2-nhc',
    #         'category': '体制改革司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-20',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/jkj/zcwj2/new_zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 22
    #         'handler': '2-nhc',
    #         'category': '疾病预防控制局 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-21',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/yzygj/zcwj2/new_zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 40
    #         'handler': '2-nhc',
    #         'category': '医政医管局 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-22',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/yzygj/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 27
    #         'handler': '2-nhc',
    #         'category': '医政医管局 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-23',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/jws/zcwj2/new_zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 7
    #         'handler': '2-nhc',
    #         'category': '基层卫生健康司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-24',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/jws/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "/ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 16
    #         'handler': '2-nhc',
    #         'category': '基层卫生健康司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-25',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/ltj/s2907/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '离退休干部局 > 组织活动',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-26',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #  # todo 翻页空白
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/cms-search/xxgk/searchList.htm?type=search&page=1#',
    #         'list_parse_rule': "//ul[@class='wgblist']/li/a",
    #         'total_page': 2,  # 396
    #         'handler': '2-nhc',
    #         'category': '中华人民共和国国家卫生健康委员会>信息>政府信息公开>公开目录',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-27',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='wgblist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/yjb/zcwj2/zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 3
    #         'handler': '2-nhc',
    #         'category': '卫生应急办公室 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-28',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/yjb/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 17
    #         'handler': '2-nhc',
    #         'category': '卫生应急办公室 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-29',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/qjjys/zcwj2/new_zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 9
    #         'handler': '2-nhc',
    #         'category': '科技教育司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-30',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/qjjys/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 16
    #         'handler': '2-nhc',
    #         'category': '科技教育司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-31',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/zhjcj/zcwj2/zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 8
    #         'handler': '2-nhc',
    #         'category': '综合监督局 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-32',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    # #todo 翻页空白
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/zhjcj/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 8
    #         'handler': '2-nhc',
    #         'category': '综合监督局 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-33',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/yaozs/zcwj2/new_zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 3
    #         'handler': '2-nhc',
    #         'category': '药物政策与基本药物制度司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-34',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/yaozs/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 6
    #         'handler': '2-nhc',
    #         'category': '药物政策与基本药物制度司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-35',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/sps/zcwj2/zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 23
    #         'handler': '2-nhc',
    #         'category': '食品安全标准与监测评估司 >  政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-36',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/sps/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 19
    #         'handler': '2-nhc',
    #         'category': '食品安全标准与监测评估司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-37',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/lljks/zcwj2/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '老龄健康司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-38',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/lljks/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '老龄健康司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-39',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/fys/zcwj2/new_zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '妇幼健康司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-40',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/fys/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '妇幼健康司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-41',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/zyjks/zcwj2/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '职业健康司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-42',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/zyjks/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 1,  # 1
    #         'handler': '2-nhc',
    #         'category': '职业健康司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-43',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/rkjcyjtfzs/zcwj2/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 8
    #         'handler': '2-nhc',
    #         'category': '人口监测与家庭发展司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-44',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/rkjcyjtfzs/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 22
    #         'handler': '2-nhc',
    #         'category': '人口监测与家庭发展司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-45',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/xcs/zcwj2/new_zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 6
    #         'handler': '2-nhc',
    #         'category': '宣传司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-46',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/xcs/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 1,  # 42
    #         'handler': '2-nhc',
    #         'category': '宣传司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-47',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/gjhzs/zcwj2/zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 1,  # 1
    #         'handler': '2-nhc',
    #         'category': '国际合作司 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-48',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/gjhzs/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 38
    #         'handler': '2-nhc',
    #         'category': '国际合作司 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-49',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/jgdw/zcwj2/zcwj.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list zcwjlist']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '机关党委 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-50',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list zcwjlist']/li[1]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/jgdw/pgzdt/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '2-nhc',
    #         'category': '机关党委 > 工作动态',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-51',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nhc.gov.cn/ltj/pzhgli/new_list.shtml#',
    #         'list_parse_rule': "//ul[@class='zxxx_list']/li/a",
    #         'total_page': 2,  # 7
    #         'handler': '2-nhc',
    #         'category': '离退休干部局 > 政策文件',
    #         'website': '中华人民共和国卫生健康委员会',
    #         'redis_key': 'policy:audit:nhc-52',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='pagination_index'][2]/span[@class='arrow']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='zxxx_list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2050/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a/font",
    #         'total_page': 1,  # 1224
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 公告通告',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2051/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a/font",
    #         'total_page': 1,  # 153
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 法规文件',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2052/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a/font",
    #         'total_page': 1,  # 1
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 新闻发布',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2143/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 9
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 规划财务',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2067/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 30
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 政策解读',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-5',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2054/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 194
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 国务院要闻',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-6',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2056/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a/font",
    #         'total_page': 1,  # 2
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 药品监管要闻',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-7',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2055/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 23
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 市场监管要闻',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-8',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2114/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a/font",
    #         'total_page': 1,  # 2
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 药品标准公告',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-9',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2120/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 3
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 医疗器械行业标准公告',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-10',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2176/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 15
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 医疗器械 >> 医疗器械监管动态',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-11',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2177/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 26
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 医疗器械 >> 医疗器械公告通告',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-12',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2178/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 41
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 医疗器械 >> 医疗器械法规文件',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-13',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2179/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 医疗器械 >> 医疗器械政策解读',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-14',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2061/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 156
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 产品召回 >> 医疗器械召回',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-15',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2188/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 化妆品 >> 化妆品监管动态',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-16',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2190/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 11
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 化妆品 >> 化妆品公告通告',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-17',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2189/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 2,  # 6
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 化妆品 >> 化妆品法规文件',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-18',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2166/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 信息化标准',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-19',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2168/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 14
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 药品 >> 药品监管动态',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-20',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2169/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a/font",
    #         'total_page': 1,  # 2
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 药品 >> 药品公告通告',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-21',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2170/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 69
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 药品 >> 药品法规文件',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-22',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2171/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 8
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 药品 >> 药品政策解读',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-23',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2172/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a/font",
    #         'total_page': 1,  # 15
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 药品 >> 药品安全警示',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-24',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2060/index.html#',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 1,  # 1
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 产品召回 >> 药品召回',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-25',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.nmpa.gov.cn/WS04/CL2157/',
    #         'list_parse_rule': "//td[@class='ListColumnClass15']/a",
    #         'total_page': 3,  # 3
    #         'handler': '2-proxy-nmpa',
    #         'category': '网站首页 >> 产品召回 >> 医疗器械不良事件通报',
    #         'website': '国家药品监督管理局',
    #         'redis_key': 'policy:audit:nhc-26',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@class='pageTdE15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='ListColumnClass15']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    # {
    #     "site_config": {
    #         'index_url': 'http://gongbao.court.gov.cn/ArticleList.html?serial_no=sfwj',
    #         'list_parse_rule': "//ul[@id='datas']/li/span/a",
    #         'total_page': 2,  # 23
    #         'handler': '3-court',
    #         'category': '首页 > 司法文件',
    #         'website': '中华人民共和国最高人民法院',
    #         'redis_key': 'policy:audit:court-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@id='pager']/a[4]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@id='datas']/li/span/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://gongbao.court.gov.cn/ArticleList.html?serial_no=sfjs',
    #         'list_parse_rule': "//ul[@id='datas']/li/span/a",
    #         'total_page': 2,  # 21
    #         'handler': '3-court',
    #         'category': '首页 > 司法文件',
    #         'website': '中华人民共和国最高人民法院',
    #         'redis_key': 'policy:audit:court-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@id='pager']/a[4]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@id='datas']/li/span/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://gongbao.court.gov.cn/ArticleList.html?serial_no=flxd',
    #         'list_parse_rule': "//ul[@id='datas']/li/span/a",
    #         'total_page': 2,  # 15
    #         'handler': '3-court',
    #         'category': '首页 > 司法文件',
    #         'website': '中华人民共和国最高人民法院',
    #         'redis_key': 'policy:audit:court-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@id='pager']/a[4]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@id='datas']/li/span/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    ## todo 打开速度缓慢  start
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinamoney.com.cn/chinese/whzlgzgd/',
    #         'list_parse_rule': "//div[@class='san-grid-m']/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-chinamoney',
    #         'category': '市场自律>外汇市场自律机制>自律机制概览>自律规范',
    #         'website': '全国外汇市场自律机制',
    #         'redis_key': 'policy:audit:chinamoney-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': [],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//li[@class='page-btn page-next']/a[@class='page-icon']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='san-grid-m']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinamoney.com.cn/chinese/syzgmore/?tabNum=2',
    #         'list_parse_rule': "//div[@class='san-grid-m']/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-chinamoney',
    #         'category': '市场自律>利率定价自律>规章制度',
    #         'website': '全国外汇市场自律机制',
    #         'redis_key': 'policy:audit:chinamoney-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//li[@class='page-btn page-next']/a[@class='page-icon']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='san-grid-m']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinamoney.com.cn/chinese/llhgsspg/',
    #         'list_parse_rule': "//div[@class='san-grid-m']/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-chinamoney',
    #         'category': '市场自律>利率定价自律>合格审慎评估>公告',
    #         'website': '全国外汇市场自律机制',
    #         'redis_key': 'policy:audit:chinamoney-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//li[@class='page-btn page-next']/a[@class='page-icon']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='san-grid-m']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinamoney.com.cn/chinese/scggbbscgg/',
    #         'list_parse_rule': "//div[@class='san-grid-m']/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-chinamoney',
    #         'category': '市场公告>本币市场公告',
    #         'website': '全国外汇市场自律机制',
    #         'redis_key': 'policy:audit:chinamoney-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//li[@class='page-btn page-next']/a[@class='page-icon']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='san-grid-m']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinamoney.com.cn/chinese/scgg-whscgg/',
    #         'list_parse_rule': "//div[@class='san-grid-m']/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-chinamoney',
    #         'category': '市场公告>外汇市场公告',
    #         'website': '全国外汇市场自律机制',
    #         'redis_key': 'policy:audit:chinamoney-5',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//li[@class='page-btn page-next']/a[@class='page-icon']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='san-grid-m']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinamoney.com.cn/chinese/scggyhywgg/',
    #         'list_parse_rule': "//div[@class='san-grid-m']/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-chinamoney',
    #         'category': '市场公告>央行业务公告',
    #         'website': '全国外汇市场自律机制',
    #         'redis_key': 'policy:audit:chinamoney-6',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//li[@class='page-btn page-next']/a[@class='page-icon']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='san-grid-m']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinamoney.com.cn/chinese/zcfg/',
    #         'list_parse_rule': "//div[@class='san-grid-m']/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-chinamoney',
    #         'category': '市场指南>政策法规',
    #         'website': '全国外汇市场自律机制',
    #         'redis_key': 'policy:audit:chinamoney-7',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//li[@class='page-btn page-next']/a[@class='page-icon']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='san-grid-m']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinamoney.com.cn/chinese/rszn2/',
    #         'list_parse_rule': "//div[@class='san-grid-m']/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-chinamoney',
    #         'category': '市场指南>本币市场指南>入市指南2',
    #         'website': '全国外汇市场自律机制',
    #         'redis_key': 'policy:audit:chinamoney-8',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//li[@class='page-btn page-next']/a[@class='page-icon']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='san-grid-m']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinamoney.com.cn/chinese/jygz2/',
    #         'list_parse_rule': "//div[@class='san-grid-m']/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-chinamoney',
    #         'category': '市场指南>本币市场指南>交易规则2',
    #         'website': '全国外汇市场自律机制',
    #         'redis_key': 'policy:audit:chinamoney-9',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//li[@class='page-btn page-next']/a[@class='page-icon']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='san-grid-m']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinamoney.com.cn/chinese/rszn/',
    #         'list_parse_rule': "//div[@class='san-grid-m']/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-chinamoney',
    #         'category': '市场指南>外汇市场指南>入市指南',
    #         'website': '全国外汇市场自律机制',
    #         'redis_key': 'policy:audit:chinamoney-10}',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//li[@class='page-btn page-next']/a[@class='page-icon']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='san-grid-m']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinamoney.com.cn/chinese/jygz2/',
    #         'list_parse_rule': "//div[@class='san-grid-m']/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-chinamoney',
    #         'category': '市场指南>外汇市场指南>交易规则',
    #         'website': '全国外汇市场自律机制',
    #         'redis_key': 'policy:audit:chinamoney-11}',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//li[@class='page-btn page-next']/a[@class='page-icon']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='san-grid-m']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    # # todo 打开速度缓慢  end

    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinatax.gov.cn/chinatax/manuscriptList/n810606',
    #         'list_parse_rule': "//ul[@class='list']/li[2]/a",
    #         'total_page': 2,  # 70
    #         'handler': '1-proxy-chinatax_19',
    #         'category': '首页  >  信息公开  >  通知公告',
    #         'website': '国家税务总局',
    #         'redis_key': 'policy:audit:chinatax-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinatax.gov.cn/n810214/n810621/n810678/index.html',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-proxy-chinatax_19',
    #         'category': '首页  >  信息公开  >  政府采购  >  相关规定',
    #         'website': '国家税务总局',
    #         'redis_key': 'policy:audit:chinatax-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinatax.gov.cn/n810214/n810636/index.html',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 1,  # 1
    #         'handler': '1-proxy-chinatax_19',
    #         'category': '首页  >  信息公开  >  行政许可',
    #         'website': '国家税务总局',
    #         'redis_key': 'policy:audit:chinatax-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinatax.gov.cn/chinatax/manuscriptList/n810631',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 2,  # 2
    #         'handler': '1-proxy-chinatax_19',
    #         'category': '首页  >  信息公开  >  税收统计',
    #         'website': '国家税务总局',
    #         'redis_key': 'policy:audit:chinatax-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    # todo  该栏目没有数据
    #     {
    #         "site_config": {
    #             'index_url': 'http://www.chinatax.gov.cn/chinatax/manuscriptList/n810616',
    #             'list_parse_rule': "//ul[@class='list']/li/a",
    #             'total_page': 1,  # 2
    #             'handler': '1-proxy-chinatax_19',
    #             'category': '首页  >  信息公开  >  财政信息',
    #             'website': '国家税务总局',
    #             'redis_key': 'policy:audit:chinatax-5',
    #         },
    #         "sel_config": {
    #             'chrome_init': ['acceptSslCerts'],
    #             'proxy_type': '',
    #             'next_page_btn': {
    #                 'by_xpath': "//a[@class='next']",
    #                 'by_id': '',
    #                 'by_class': '',
    #             },
    #             'waiting_page': {
    #                 'by_xpath': "//ul[@class='list']/li/a",
    #                 'by_id': '',
    #                 'by_class': '',
    #             },
    #         },
    #     },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinatax.gov.cn/chinatax/manuscriptList/n2015391',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-proxy-chinatax_19',
    #         'category': '首页  >  信息公开  >  建议提案办理',
    #         'website': '国家税务总局',
    #         'redis_key': 'policy:audit:chinatax-6',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinatax.gov.cn/chinatax/whmanuscriptList/n810755',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 1,  # 70
    #         'handler': '1-proxy-chinatax_19',
    #         'category': '首页  >  税收政策  >  最新文件',
    #         'website': '国家税务总局',
    #         'redis_key': 'policy:audit:chinatax-7',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinatax.gov.cn/chinatax/manuscriptList/n810760',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 1,  # 27
    #         'handler': '1-proxy-chinatax_19',
    #         'category': '首页  >  税收政策  >  政策解读',
    #         'website': '国家税务总局',
    #         'redis_key': 'policy:audit:chinatax-8',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinatax.gov.cn/chinatax/manuscriptList/n810780',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 1,  # 184
    #         'handler': '1-proxy-chinatax_19',
    #         'category': '首页  >  新闻发布  >  媒体视点',
    #         'website': '国家税务总局',
    #         'redis_key': 'policy:audit:chinatax-9',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    # todo 没找到相应栏目
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinatax.gov.cn/n810214/n810641/n810687/index.html',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-proxy-chinatax_19',
    #         'category': '首页 > 信息公开 > 政府信息公开 > 政府信息公开规定',
    #         'website': '国家税务总局',
    #         'redis_key': 'policy:audit:chinatax-10',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    # todo 未找到栏目
    # {
    #     "site_config": {
    #         'index_url': 'http://hd.chinatax.gov.cn/gdnps/',
    #         'list_parse_rule': "//ul[@class='list']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-proxy-chinatax_19',
    #         'category': '首页 >信息公开 >主动公开基本目录',
    #         'website': '国家税务总局',
    #         'redis_key': 'policy:audit:chinatax-11',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='list']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.sapprft.gov.cn/sapprft/utils/govInfosys.shtml?Category6ID=39&DisplayName=%E5%86%B3%E5%AE%9A&channelID=6593',
    #         'list_parse_rule': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #         'total_page': 1,  # 2
    #         'handler': '3-sapprft',
    #         'category': '政府信息公开>决定',
    #         'website': '国家广播电视局',
    #         'redis_key': 'policy:audit:sapprft-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.sapprft.gov.cn/sapprft/utils/govInfosys.shtml?Category6ID=40&DisplayName=%E4%BB%A4&channelID=6593',
    #         'list_parse_rule': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #         'total_page': 1,  # 3
    #         'handler': '3-sapprft',
    #         'category': '政府信息公开>令',
    #         'website': '国家广播电视局',
    #         'redis_key': 'policy:audit:sapprft-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.sapprft.gov.cn/sapprft/utils/govInfosys.shtml?Category6ID=41&DisplayName=%E5%85%AC%E5%91%8A&channelID=6593',
    #         'list_parse_rule': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #         'total_page': 1,  # 3
    #         'handler': '3-sapprft',
    #         'category': '政府信息公开>公告',
    #         'website': '国家广播电视局',
    #         'redis_key': 'policy:audit:sapprft-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.sapprft.gov.cn/sapprft/utils/govInfosys.shtml?Category6ID=42&DisplayName=%E6%84%8F%E8%A7%81&channelID=6593',
    #         'list_parse_rule': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #         'total_page': 1,  # 2
    #         'handler': '3-sapprft',
    #         'category': '政府信息公开>意见',
    #         'website': '国家广播电视局',
    #         'redis_key': 'policy:audit:sapprft-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.sapprft.gov.cn/sapprft/utils/govInfosys.shtml?Category6ID=43&DisplayName=%E9%80%9A%E7%9F%A5&channelID=6593',
    #         'list_parse_rule': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #         'total_page': 1,  # 2
    #         'handler': '3-sapprft',
    #         'category': '政府信息公开>通知',
    #         'website': '国家广播电视局',
    #         'redis_key': 'policy:audit:sapprft-5',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.sapprft.gov.cn/sapprft/utils/govInfosys.shtml?Category6ID=44&DisplayName=%E9%80%9A%E6%8A%A5&channelID=6593',
    #         'list_parse_rule': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #         'total_page': 1,  # 2
    #         'handler': '3-sapprft',
    #         'category': '政府信息公开>通报',
    #         'website': '国家广播电视局',
    #         'redis_key': 'policy:audit:sapprft-6',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.sapprft.gov.cn/sapprft/utils/govInfosys.shtml?Category6ID=45&DisplayName=%E6%89%B9%E5%A4%8D&channelID=6593',
    #         'list_parse_rule': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #         'total_page': 1,  # 2
    #         'handler': '3-sapprft',
    #         'category': '政府信息公开>批复',
    #         'website': '国家广播电视局',
    #         'redis_key': 'policy:audit:sapprft-7',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.sapprft.gov.cn/sapprft/utils/govInfosys.shtml?Category6ID=46&DisplayName=%E5%87%BD&channelID=6593',
    #         'list_parse_rule': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #         'total_page': 1,  # 2
    #         'handler': '3-sapprft',
    #         'category': '政府信息公开>函',
    #         'website': '国家广播电视局',
    #         'redis_key': 'policy:audit:sapprft-8',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.sapprft.gov.cn/sapprft/utils/govInfosys.shtml?Category6ID=47&DisplayName=%E5%85%B6%E4%BB%96&channelID=6593',
    #         'list_parse_rule': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #         'total_page': 1,  # 6
    #         'handler': '3-sapprft',
    #         'category': '政府信息公开>其他',
    #         'website': '国家广播电视局',
    #         'redis_key': 'policy:audit:sapprft-9',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@id='ajaxElement_2_736']//a[@class='extLink']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://gkml.customs.gov.cn/tabid/1033/Default.aspx',
    #         'list_parse_rule': "//table[@id='ess_ctr445_ListG_Info_dg']//a",
    #         'total_page': 1,  # 1784
    #         'handler': '1-2-customs_gkml',
    #         'category': '首页>海关总署政务公开首页>政府信息公开>公开目录',
    #         'website': '海关总署',
    #         'redis_key': 'policy:audit:customs_gkml-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//tr/td[1]/a[@class='Normal'][28]/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//table[@id='ess_ctr445_ListG_Info_dg']//a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    # {
    #     "site_config": {
    #         'index_url': 'http://www.mps.gov.cn/n2254314/n2254409/n4904353/index.html',
    #         'list_parse_rule': "//span[@id='comp_4939820']/dl/dd/a",
    #         'total_page': 1,  # 3
    #         'handler': '3-mps',
    #         'category': '首页 > 法律法规',
    #         'website': '中华人民共和国公安部',
    #         'redis_key': 'policy:audit:mps-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//td[@id='pag_4939820']/a[3]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//span[@id='comp_4939820']/dl/dd/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://app.mps.gov.cn/gdnps/index.jsp#',
    #         'list_parse_rule': "//div[@class='item']/ul/li/a",
    #         'total_page': 1,  # 3
    #         'handler': '3-mps',
    #         'category': '首页>机构分类',
    #         'website': '中华人民共和国公安部',
    #         'redis_key': 'policy:audit:mps-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='item']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://xxgk.sasac.gov.cn:8080/gdnps/',
    #         'list_parse_rule': "//tbody[@id='contentBody']/tr/td/div/a",
    #         'total_page': 1,  # 3
    #         'handler': '3-mps',
    #         'category': '首页>信息公开目录',
    #         'website': '国务院国有资产监督管理委员会',
    #         'redis_key': '3-sasac',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@id='goPageId']/a[7]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//tbody[@id='contentBody']/tr/td/div/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.pcpex.com:81/cms/f/list-a3d9a5ca5c17455d80863c4dc4a07ed9.html',
    #         'list_parse_rule': "//tbody/tr/td[1]/a",
    #         'total_page': 1,  # 3
    #         'handler': '2-mot',
    #         'category': '首页 / 政策法规 / 政策法规',
    #         'website': '中国石油交易中心',
    #         'redis_key': '3-pcpex',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//li[@class='disabled'][2]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//tbody/tr/td[1]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.forestry.gov.cn/main/95/index.html',
    #         'list_parse_rule': "//ul/li[@class='cl']/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-forestry',
    #         'category': '中国林业网>信息发布>规划与资金>部门预算',
    #         'website': '林业草原局',
    #         'redis_key': 'policy:audit:forestry-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/li[@class='cl']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.forestry.gov.cn/main/5071/index.html',
    #         'list_parse_rule': "//ul/li[@class='cl']/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-forestry',
    #         'category': '中国林业网>信息发布>国际合作>双边协议>双边部门间协议',
    #         'website': '林业草原局',
    #         'redis_key': 'policy:audit:forestry-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/li[@class='cl']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.forestry.gov.cn/main/5070/index.html',
    #         'list_parse_rule': "//ul/li[@class='cl']/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-forestry',
    #         'category': '中国林业网>信息发布>国际合作>双边协议>双边政府间协议',
    #         'website': '林业草原局',
    #         'redis_key': 'policy:audit:forestry-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/li[@class='cl']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.forestry.gov.cn/main/4861/index.html',
    #         'list_parse_rule': "//ul/li[@class='cl']/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-forestry',
    #         'category': '中国林业网>信息发布>信息公开>建议提案复文>建议复文',
    #         'website': '林业草原局',
    #         'redis_key': 'policy:audit:forestry-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/li[@class='cl']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.forestry.gov.cn/main/3957/index.html',
    #         'list_parse_rule': "//ul/li[@class='cl']/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-forestry',
    #         'category': '中国林业网>信息发布>政策解读',
    #         'website': '林业草原局',
    #         'redis_key': 'policy:audit:forestry-5',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/li[@class='cl']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.forestry.gov.cn/main/107/index.html',
    #         'list_parse_rule': "//ul/li[@class='cl']/a",
    #         'total_page': 1,  # 6
    #         'handler': '2-forestry',
    #         'category': '中国林业网>信息发布>电子政务>相关政策',
    #         'website': '林业草原局',
    #         'redis_key': 'policy:audit:forestry-6',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/li[@class='cl']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.forestry.gov.cn/main/5461/index.html',
    #         'list_parse_rule': "//ul/li[@class='cl']/a",
    #         'total_page': 1,  # 5
    #         'handler': '2-forestry',
    #         'category': '中国林业网>信息发布>政策科技>林业政策',
    #         'website': '林业草原局',
    #         'redis_key': 'policy:audit:forestry-7',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/li[@class='cl']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.forestry.gov.cn/main/4862/index.html',
    #         'list_parse_rule': "//ul/li[@class='cl']/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-forestry',
    #         'category': '中国林业网>信息发布>信息公开>建议提案复文>提案复文',
    #         'website': '林业草原局',
    #         'redis_key': 'policy:audit:forestry-8',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/li[@class='cl']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.forestry.gov.cn/main/3956/index.html',
    #         'list_parse_rule': "//ul/li[@class='cl']/a",
    #         'total_page': 1,  # 2
    #         'handler': '2-forestry',
    #         'category': '中国林业网>信息发布>政策法规>政策法规动态',
    #         'website': '林业草原局',
    #         'redis_key': 'policy:audit:forestry-9',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/li[@class='cl']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.customs.gov.cn/customs/302249/302266/302269/index.html',
    #         'list_parse_rule': "//div/ul[@class='conList_ul']/li/a",
    #         'total_page': 1,  # 33
    #         'handler': '1-2-customs',
    #         'category': '首页 > 信息公开 > 海关法规 > 最新公告"  JS加密',
    #         'website': '海关总署',
    #         'redis_key': 'policy:audit:customs-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='easysite-page-wrap']/a[3]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div/ul[@class='conList_ul']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.customs.gov.cn/customs/302427/302428/index.html',
    #         'list_parse_rule': "//div/ul[@class='conList_ul']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-2-customs',
    #         'category': '首页 > 在线服务 > 行政许可',
    #         'website': '海关总署',
    #         'redis_key': 'policy:audit:customs-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='easysite-page-wrap']/a[3]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div/ul[@class='conList_ul']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.customs.gov.cn/customs/302249/302266/302268/index.html',
    #         'list_parse_rule': "//div/ul[@class='conList_ul']/li/a",
    #         'total_page': 1,  # 1
    #         'handler': '1-2-customs',
    #         'category': '首页 > 信息公开 > 海关法规 > 最新署令',
    #         'website': '海关总署',
    #         'redis_key': 'policy:audit:customs-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='easysite-page-wrap']/a[3]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div/ul[@class='conList_ul']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.customs.gov.cn/customs/302249/302266/302267/index.html',
    #         'list_parse_rule': "//div/ul[@class='conList_ul']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-2-customs',
    #         'category': '首页 > 信息公开 > 海关法规',
    #         'website': '海关总署',
    #         'redis_key': 'policy:audit:customs-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div/ul[@class='conList_ul']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.customs.gov.cn/customs/302249/302270/302272/index.html',
    #         'list_parse_rule': "//ul[@class='conList_ull']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-2-customs',
    #         'category': '首页 > 信息公开 > 政策解读 > 历期政策解读',
    #         'website': '海关总署',
    #         'redis_key': 'policy:audit:customs-5',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='pagingNormal next']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@class='conList_ull']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.customs.gov.cn/customs/zsgk93/302256/302258/index.html',
    #         'list_parse_rule': "//div/ul[@class='conList_ul']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-2-customs',
    #         'category': '首页 > 总署概况 > 总署通告 > 最新署令',
    #         'website': '海关总署',
    #         'redis_key': 'policy:audit:customs-6',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div/ul[@class='conList_ul']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.customs.gov.cn/customs/zsgk93/302256/302257/index.html',
    #         'list_parse_rule': "//div/ul[@class='conList_ul']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-2-customs',
    #         'category': '首页 > 总署概况 > 总署通告 > 最新公告',
    #         'website': '海关总署',
    #         'redis_key': 'policy:audit:customs-7',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div/ul[@class='conList_ul']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.customs.gov.cn/customs/zsgk93/302256/302257/index.html',
    #         'list_parse_rule': "//div/ul[@class='conList_ul']/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-2-customs',
    #         'category': '首页 > 总署概况 > 总署通告 > 最新公告',
    #         'website': '海关总署',
    #         'redis_key': 'policy:audit:customs-7',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='con']/a[8]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div/ul[@class='conList_ul']/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    # #todo 网站打开不稳定 start
    # {
    #     "site_config": {
    #         'index_url': 'https://www.sge.com.cn/guize/rljysxj?cflag=1&p=1',
    #         'list_parse_rule': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-sge',
    #         'category': ' 首页 > 制度与规则 > 询价 > 交易所询价',
    #         'website': '上海金交所',
    #         'redis_key': 'policy:audit:sge-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='btn border_ea noLeft_border']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'https://www.sge.com.cn/guize/qs?cflag=1&p=1',
    #         'list_parse_rule': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-sge',
    #         'category': ' 首页 > 制度与规则 > 清算',
    #         'website': '上海金交所',
    #         'redis_key': 'policy:audit:sge-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='btn border_ea noLeft_border']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'https://www.sge.com.cn/guize/jg?cflag=1&p=1',
    #         'list_parse_rule': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-sge',
    #         'category': ' 首页 > 制度与规则 > 交割',
    #         'website': '上海金交所',
    #         'redis_key': 'policy:audit:sge-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='btn border_ea noLeft_border']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'https://www.sge.com.cn/guize/dj?cflag=1&p=1',
    #         'list_parse_rule': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-sge',
    #         'category': ' 首页 > 制度与规则 > 上海金定价',
    #         'website': '上海金交所',
    #         'redis_key': 'policy:audit:sge-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='btn border_ea noLeft_border']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'https://www.sge.com.cn/guize/fxqbg?cflag=1&p=1',
    #         'list_parse_rule': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-sge',
    #         'category': ' 首页 > 制度与规则 > 反洗钱专栏 > 反洗钱报告',
    #         'website': '上海金交所',
    #         'redis_key': 'policy:audit:sge-5',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='btn border_ea noLeft_border']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'https://www.sge.com.cn/jjsnotice?cflag=1&p=1',
    #         'list_parse_rule': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-sge',
    #         'category': ' 首页 > 上金所公告',
    #         'website': '上海金交所',
    #         'redis_key': 'policy:audit:sge-6',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='btn border_ea noLeft_border']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'https://www.sge.com.cn/guize/jj?cflag=1&p=1',
    #         'list_parse_rule': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-sge',
    #         'category': ' 首页 > 制度与规则 > 竞价 > 现货实盘合约',
    #         'website': '上海金交所',
    #         'redis_key': 'policy:audit:sge-7',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='btn border_ea noLeft_border']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'https://www.sge.com.cn/guize/ywgz?cflag=1&p=1',
    #         'list_parse_rule': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-sge',
    #         'category': ' 首页 > 制度与规则 > 业务规则 > 交易所业务规则',
    #         'website': '上海金交所',
    #         'redis_key': 'policy:audit:sge-8',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='btn border_ea noLeft_border']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'https://www.sge.com.cn/guize/rule?cflag=1&p=1',
    #         'list_parse_rule': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-sge',
    #         'category': ' 首页 > 制度与规则 > 黄金市场相关政策',
    #         'website': '上海金交所',
    #         'redis_key': 'policy:audit:sge-9',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='btn border_ea noLeft_border']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'https://www.sge.com.cn/xwzx/NewsCenter_sge?cflag=1&p=1',
    #         'list_parse_rule': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-sge',
    #         'category': ' 首页 >  交易所新闻',
    #         'website': '上海金交所',
    #         'redis_key': 'policy:audit:sge-10',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='btn border_ea noLeft_border']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='articleList border_ea mt30 mb30']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    # #todo 网站打开不稳定 end
    # {
    #     "site_config": {
    #         'index_url': 'http://www.czce.com.cn/cn/flfg/flfg/sfjs/H77050103index_1.htm',
    #         'list_parse_rule': "//ul/table/tbody/tr[1]/td/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-czce',
    #         'category': '首页> 法律及规则>法律法规>司法解释',
    #         'website': '郑州商品交易所',
    #         'redis_key': 'policy:audit:czce-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//ul/table/tbody/tr[2]/td/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/table/tbody/tr[1]/td/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.czce.com.cn/cn/flfg/flfg/xzfg/H77050102index_1.htm',
    #         'list_parse_rule': "//ul/table/tbody/tr[1]/td/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-czce',
    #         'category': '首页>法律及规则>法律法规>行政法规',
    #         'website': '郑州商品交易所',
    #         'redis_key': 'policy:audit:czce-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//ul/table/tbody/tr[2]/td/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/table/tbody/tr[1]/td/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.czce.com.cn/cn/flfg/flfg/bmgz/H77050104index_1.htm',
    #         'list_parse_rule': "//ul/table/tbody/tr[1]/td/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-czce',
    #         'category': '首页>法律及规则>法律法规>部门规章',
    #         'website': '郑州商品交易所',
    #         'redis_key': 'policy:audit:czce-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//ul/table/tbody/tr[2]/td/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/table/tbody/tr[1]/td/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.czce.com.cn/cn/flfg/zcjywgz/ggytz/H77050304index_1.htm',
    #         'list_parse_rule': "//ul/table/tbody/tr[1]/td/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-czce',
    #         'category': '首页>法律及规则>章程及业务规则>公告与通知',
    #         'website': '郑州商品交易所',
    #         'redis_key': 'policy:audit:czce-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//ul/table/tbody/tr[2]/td/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/table/tbody/tr[1]/td/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.czce.com.cn/cn/flfg/zcjywgz/ssxz/H77050303index_1.htm',
    #         'list_parse_rule': "//ul/table/tbody/tr[1]/td/li/a",
    #         'total_page': 1,  # 2
    #         'handler': '3-czce',
    #         'category': '首页>法律及规则>章程及业务规则>实施细则 ',
    #         'website': '郑州商品交易所',
    #         'redis_key': 'policy:audit:czce-5',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//ul/table/tbody/tr[2]/td/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul/table/tbody/tr[1]/td/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://ginfo.mohurd.gov.cn/',
    #         'list_parse_rule': "//div[@id='InfoList']/table/tbody/tr/td[2]/a",
    #         'total_page': 1,  # 296
    #         'handler': '1-mhd',
    #         'category': '首页>政府信息公开>信息公开目录',
    #         'website': '中华人民共和国住房和城乡建设部',
    #         'redis_key': 'policy:audit:mhd',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@id='ctl00_lbtPageDown']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@id='InfoList']/table/tbody/tr/td[2]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.neeq.com.cn/rule/law_list.html',
    #         'list_parse_rule': "//a[@class='Tit hrefaddviews']",
    #         'total_page': 1,  # 2
    #         'handler': '3-neeq',
    #         'category': '首页> 法律规则> 法律法规',
    #         'website': '中国中小企业股份转让系统',
    #         'redis_key': 'policy:audit:neeq-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//a[@class='Tit hrefaddviews']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.neeq.com.cn/rule/regulation_list.html',
    #         'list_parse_rule': "//a[@class='Tit hrefaddviews']",
    #         'total_page': 1,  # 2
    #         'handler': '3-neeq',
    #         'category': '首页> 法律规则> 部门规章',
    #         'website': '中国中小企业股份转让系统',
    #         'redis_key': 'policy:audit:neeq-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//a[@class='Tit hrefaddviews']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.neeq.com.cn/rule/Business_rules.html',
    #         'list_parse_rule': "//a[@class='Tit hrefaddviews']",
    #         'total_page': 1,  # 2
    #         'handler': '3-neeq',
    #         'category': '首页> 法律规则> 业务规则',
    #         'website': '中国中小企业股份转让系统',
    #         'redis_key': 'policy:audit:neeq-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//a[@class='Tit hrefaddviews']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.neeq.com.cn/rule/Service_info.html',
    #         'list_parse_rule': "//a[@class='Tit hrefaddviews']",
    #         'total_page': 1,  # 2
    #         'handler': '3-neeq',
    #         'category': '首页> 法律规则> 服务指南',
    #         'website': '中国中小企业股份转让系统',
    #         'redis_key': 'policy:audit:neeq-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//a[@class='Tit hrefaddviews']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://bxjg.circ.gov.cn/web/site0/tab5223/',
    #         'list_parse_rule': "//span[@id='lan1']/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-circ',
    #         'category': '首页>政策法规>行政法规',
    #         'website': '银保监会',
    #         'redis_key': 'policy:audit:circ-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//span[@id='lan1']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://bxjg.circ.gov.cn/web/site0/tab5226/',
    #         'list_parse_rule': "//span[@id='lan1']/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-circ',
    #         'category': '首页>政策法规>其他法规',
    #         'website': '银保监会',
    #         'redis_key': 'policy:audit:circ-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//span[@id='lan1']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://bxjg.circ.gov.cn/web/site0/tab7924/',
    #         'list_parse_rule': "//td[@class='hui14']/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-circ',
    #         'category': '首页>发布与解读>政策解读',
    #         'website': '银保监会',
    #         'redis_key': 'policy:audit:circ-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='Normal page_custom'][4]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='hui14']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://bxjg.circ.gov.cn/web/site0/tab5222/',
    #         'list_parse_rule': "//span[@id='lan1']/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-circ',
    #         'category': '首页>政策法规>法律',
    #         'website': '银保监会',
    #         'redis_key': 'policy:audit:circ-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//span[@id='lan1']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://bxjg.circ.gov.cn/web/site0/tab5224/',
    #         'list_parse_rule': "//span[@id='lan1']/a",
    #         'total_page': 1,  # 7
    #         'handler': '1-circ',
    #         'category': '首页>政策法规>部门规章',
    #         'website': '银保监会',
    #         'redis_key': 'policy:audit:circ-5',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//span[@id='lan1']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://bxjg.circ.gov.cn/web/site0/tab5214/',
    #         'list_parse_rule': "//span[@id='lan1']/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-circ',
    #         'category': '首页>工作动态>公告通知>公告',
    #         'website': '银保监会',
    #         'redis_key': 'policy:audit:circ-6',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//span[@id='lan1']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://bxjg.circ.gov.cn/web/site0/tab5216/',
    #         'list_parse_rule': "//span[@id='lan1']/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-circ',
    #         'category': '首页>工作动态>公告通知>通知',
    #         'website': '银保监会',
    #         'redis_key': 'policy:audit:circ-7',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//span[@id='lan1']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://bxjg.circ.gov.cn/web/site0/tab5225/',
    #         'list_parse_rule': "//span[@id='lan1']/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-circ',
    #         'category': '首页>政策法规>规范性文件',
    #         'website': '银保监会',
    #         'redis_key': 'policy:audit:circ-8',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//span[@id='lan1']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://bxjg.circ.gov.cn/web/site0/tab5207/',
    #         'list_parse_rule': "//td[@class='hui14']/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-circ',
    #         'category': '首页>发布与解读>新闻动态',
    #         'website': '银保监会',
    #         'redis_key': 'policy:audit:circ-9',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='hui14']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://bxjg.circ.gov.cn/web/site0/tab5220/',
    #         'list_parse_rule': "//span[@id='lan1']/a",
    #         'total_page': 1,  # 2
    #         'handler': '1-circ',
    #         'category': '首页>工作动态>人事信息>人事任免',
    #         'website': '银保监会',
    #         'redis_key': 'policy:audit:circ-10',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//span[@id='lan1']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.seac.gov.cn/seac/xxgk/zcfb/index.shtml',
    #         'list_parse_rule': "//div[@class='w1']/ul/li/span[1]/a",
    #         'total_page': 1,  #
    #         'handler': '3-seac',
    #         'category': '首页 > 信息公开 > 政策发布',
    #         'website': '中华人民共和国国家民族事务委员会',
    #         'redis_key': 'policy:audit:seac-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.seac.gov.cn/seac/zcfg/flfg/index.shtml',
    #         'list_parse_rule': "//div[@class='w1']/ul/li/a",
    #         'total_page': 1,  #
    #         'handler': '3-seac',
    #         'category': '首页 > 政策法规 > 法律法规',
    #         'website': '中华人民共和国国家民族事务委员会',
    #         'redis_key': 'policy:audit:seac-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='w1']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.seac.gov.cn/seac/xxgk/fzgh/index.shtml',
    #         'list_parse_rule': "//div[@class='w1']/ul/li/span[1]/a",
    #         'total_page': 1,  #
    #         'handler': '3-seac',
    #         'category': '首页 > 信息公开 > 发展规划',
    #         'website': '中华人民共和国国家民族事务委员会',
    #         'redis_key': 'policy:audit:seac-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.seac.gov.cn/seac/zcfg/zcwj/index.shtml',
    #         'list_parse_rule': "//div[@class='w1']/ul/li/a",
    #         'total_page': 1,  #
    #         'handler': '3-seac',
    #         'category': '首页 > 政策法规 > 政策文件',
    #         'website': '中华人民共和国国家民族事务委员会',
    #         'redis_key': 'policy:audit:seac-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='w1']/ul/li/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.seac.gov.cn/seac/xxgk/zcjd/index.shtml',
    #         'list_parse_rule': "//div[@class='w1']/ul/li/span[1]/a",
    #         'total_page': 1,  #
    #         'handler': '3-seac',
    #         'category': '首页 > 信息公开 > 政策解读',
    #         'website': '中华人民共和国国家民族事务委员会',
    #         'redis_key': 'policy:audit:seac-5',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.seac.gov.cn/xxgk/xxgk/xxgkml.shtml',
    #         'list_parse_rule': "//ul[@id='infoUl']/li/a[@class='s2']",
    #         'total_page': 1,  #
    #         'handler': '3-seac',
    #         'category': '首页 > 信息公开 > 信息公开目录',
    #         'website': '中华人民共和国国家民族事务委员会',
    #         'redis_key': 'policy:audit:seac-6',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='page']/a[@class='next']/font/font",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//ul[@id='infoUl']/li/a[@class='s2']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.cbrc.gov.cn/chinese/home/docViewPage/110014&current=1',
    #         'list_parse_rule': "//td[@class='cc']/a[@class='STYLE8']",
    #         'total_page': 1,  #
    #         'handler': '1-proxy-cbrc',
    #         'category': '中国银行业监督管理委员会＞政务信息＞政策法规＞法规及解读',
    #         'website': '中国银行业监督管理委员会',
    #         'redis_key': 'policy:audit:cbrc-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//tr[36]/td[@class='cc']/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='cc']/a[@class='STYLE8']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.cbrc.gov.cn/more.do?itemUuid=800103&current=1',
    #         'list_parse_rule': "//div[@class='maincontent']/ul/li/a",
    #         'total_page': 1,  #
    #         'handler': '1-proxy-cbrc',
    #         'category': '首页>主题分类>规章政策',
    #         'website': '中国银行业监督管理委员会',
    #         'redis_key': 'policy:audit:cbrc-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//tr[36]/td[@class='cc']/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='maincontent']/ul/li[1]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.cbrc.gov.cn/searchFen.do?year=&type=null&number=null&docTitle=null&indexNo=null&startDate=null&endDate=null&agencyType=null&interViewType=null&zjgxflag=true&current=1',
    #         'list_parse_rule': "//div[@class='maincontent']/ul/li[1]/a",
    #         'total_page': 3,  #291
    #         'handler': '1-proxy-cbrc',
    #         'category': '首页>最近更新',
    #         'website': '中国银行业监督管理委员会',
    #         'redis_key': 'policy:audit:cbrc-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//div[@class='fenyelogo']/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='maincontent']/ul/li[1]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.cbrc.gov.cn/chinese/newListDoc/111004/1.html',
    #         'list_parse_rule': "//tbody/tr/td[@class='cc']/a",
    #         'total_page': 1,  #
    #         'handler': '1-proxy-cbrc',
    #         'category': '首页>公告通知',
    #         'website': '中国银行业监督管理委员会',
    #         'redis_key': 'policy:audit:cbrc-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//tbody/tr[18]/td[@class='cc']/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//tbody/tr/td[@class='cc']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.cbrc.gov.cn/chinese/home/docViewPage/110013',
    #         'list_parse_rule': "//td[@class='cc']/a[@class='STYLE8']",
    #         'total_page': 1,  #
    #         'handler': '1-proxy-cbrc',
    #         'category': '中国银行业监督管理委员会＞政务信息＞政策法规＞相关金融法律',
    #         'website': '中国银行业监督管理委员会',
    #         'redis_key': 'policy:audit:cbrc-5',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='cc']/a[@class='STYLE8']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.cbrc.gov.cn/chinese/home/docViewPage/110014',
    #         'list_parse_rule': "//td[@class='cc']/a[@class='STYLE8']",
    #         'total_page': 1,  #11
    #         'handler': '1-proxy-cbrc',
    #         'category': '中国银行业监督管理委员会＞政务信息＞政策法规＞法规及解读',
    #         'website': '中国银行业监督管理委员会',
    #         'redis_key': 'policy:audit:cbrc-6',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//tr[36]/td[@class='cc']/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//td[@class='cc']/a[@class='STYLE8']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.cbrc.gov.cn/chinese/newListDoc/111001/1.html',
    #         'list_parse_rule': "//tbody/tr/td[@class='cc']/a",
    #         'total_page': 1,  #2
    #         'handler': '1-proxy-cbrc',
    #         'category': '中国银行业监督管理委员会＞图片新闻',
    #         'website': '中国银行业监督管理委员会',
    #         'redis_key': 'policy:audit:cbrc-7',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//tbody/tr[18]/td[@class='cc']/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//tbody/tr/td[@class='cc']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.cbrc.gov.cn/chinese/newListDoc/111002/1.html',
    #         'list_parse_rule': "//tbody/tr/td[@class='cc']/a",
    #         'total_page': 1,  #
    #         'handler': '1-proxy-cbrc',
    #         'category': '中国银行业监督管理委员会＞最新更新',
    #         'website': '中国银行业监督管理委员会',
    #         'redis_key': 'policy:audit:cbrc-8',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//tbody/tr[18]/td[@class='cc']/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//tbody/tr/td[@class='cc']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.cbrc.gov.cn/chinese/newListDoc/111003/1.html',
    #         'list_parse_rule': "//tbody/tr/td[@class='cc']/a",
    #         'total_page': 1,  #
    #         'handler': '1-proxy-cbrc',
    #         'category': '中国银行业监督管理委员会＞政策法规',
    #         'website': '中国银行业监督管理委员会',
    #         'redis_key': 'policy:audit:cbrc-9',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//tbody/tr[18]/td[@class='cc']/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//tbody/tr/td[@class='cc']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.cbrc.gov.cn/chinese/newListDoc/111005/1.html',
    #         'list_parse_rule': "//tbody/tr/td[@class='cc']/a",
    #         'total_page': 1,  #12
    #         'handler': '1-proxy-cbrc',
    #         'category': '中国银行业监督管理委员会＞监管动态',
    #         'website': '中国银行业监督管理委员会',
    #         'redis_key': 'policy:audit:cbrc-10',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//tbody/tr[18]/td[@class='cc']/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//tbody/tr/td[@class='cc']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.cbrc.gov.cn/chinese/newListDoc/111006/1.html',
    #         'list_parse_rule': "//tbody/tr/td[@class='cc']/a",
    #         'total_page': 1,  #
    #         'handler': '1-proxy-cbrc',
    #         'category': '中国银行业监督管理委员会＞时政要闻',
    #         'website': '中国银行业监督管理委员会',
    #         'redis_key': 'policy:audit:cbrc-11',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//tbody/tr[18]/td[@class='cc']/a[1]",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//tbody/tr/td[@class='cc']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinabond.com.cn/jsp/include/CB_CN/issue/issuemiddleinclude.jsp?form_subbonds=&form_bondtype=21770&form_bondtype1=21770&form_issueyear=&form_issuenum=&form_keyword=&form_salescompany=&form_salescompanyName=%C8%AB%B2%BF%D6%F7%B3%D0%CF%FA%C9%CC%28%CA%E4%C8%EB%B9%D8%BC%FC%D7%D6%B2%E9%D1%AF%29&form_issuepersonal=&form_issuepersonalName=%C8%AB%B2%BF%B7%A2%D0%D0%C8%CB%28%CA%E4%C8%EB%B9%D8%BC%FC%D7%D6%B2%E9%D1%AF%29&form_cxpj=ROOT%3E%D2%B5%CE%F1%B2%D9%D7%F7%3E%B7%A2%D0%D0%D3%EB%B8%B6%CF%A2%B6%D2%B8%B6%3E%D5%AE%C8%AF%D6%D6%C0%E0%3E%B9%FA%D5%AE&form_zzlx=%B9%FA%D5%AE&xxlx=fxwj&_tp_fxwj=1#',
    #         'list_parse_rule': "//li[@class='liqxd1']/span[@class='unlock']/a",
    #         'total_page': 1,  # 116
    #         'handler': '3-chinabond',
    #         'category': '首页>业务操作>发行与付息兑付>债券种类>国债>发行文件',
    #         'website': '中国债券信息网中央结算公司',
    #         'redis_key': 'policy:audit:chinabond-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//ul[@id='pg_fxwj']/li[12]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//li[@class='liqxd1']/span[@class='unlock']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinabond.com.cn/jsp/include/CB_CN/issue/issuemiddleinclude.jsp?form_subbonds=&form_bondtype=21770&form_bondtype1=21770&form_issueyear=&form_issuenum=&form_keyword=&form_salescompany=&form_salescompanyName=%C8%AB%B2%BF%D6%F7%B3%D0%CF%FA%C9%CC%28%CA%E4%C8%EB%B9%D8%BC%FC%D7%D6%B2%E9%D1%AF%29&form_issuepersonal=&form_issuepersonalName=%C8%AB%B2%BF%B7%A2%D0%D0%C8%CB%28%CA%E4%C8%EB%B9%D8%BC%FC%D7%D6%B2%E9%D1%AF%29&form_cxpj=ROOT%3E%D2%B5%CE%F1%B2%D9%D7%F7%3E%B7%A2%D0%D0%D3%EB%B8%B6%CF%A2%B6%D2%B8%B6%3E%D5%AE%C8%AF%D6%D6%C0%E0%3E%B9%FA%D5%AE&form_zzlx=%B9%FA%D5%AE&xxlx=fxjg&_tp_fxwj=1#',
    #         'list_parse_rule': "//li[@class='liqxd1']/span[@class='unlock']/a",
    #         'total_page': 1,  #100
    #         'handler': '3-chinabond',
    #         'category': '首页>业务操作>发行与付息兑付>债券种类>国债>发行结果',
    #         'website': '中国债券信息网中央结算公司',
    #         'redis_key': 'policy:audit:chinabond-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//ul[@id='pg_fxwj']/li[12]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//li[@class='liqxd1']/span[@class='unlock']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinabond.com.cn/jsp/include/CB_CN/issue/issuemiddleinclude.jsp?form_subbonds=&form_bondtype=21770&form_bondtype1=21770&form_issueyear=&form_issuenum=&form_keyword=&form_salescompany=&form_salescompanyName=%C8%AB%B2%BF%D6%F7%B3%D0%CF%FA%C9%CC%28%CA%E4%C8%EB%B9%D8%BC%FC%D7%D6%B2%E9%D1%AF%29&form_issuepersonal=&form_issuepersonalName=%C8%AB%B2%BF%B7%A2%D0%D0%C8%CB%28%CA%E4%C8%EB%B9%D8%BC%FC%D7%D6%B2%E9%D1%AF%29&form_cxpj=ROOT%3E%D2%B5%CE%F1%B2%D9%D7%F7%3E%B7%A2%D0%D0%D3%EB%B8%B6%CF%A2%B6%D2%B8%B6%3E%D5%AE%C8%AF%D6%D6%C0%E0%3E%B9%FA%D5%AE&form_zzlx=%B9%FA%D5%AE&xxlx=fxjh&_tp_fxwj=1#',
    #         'list_parse_rule': "//li[@class='liqxd1']/span[@class='unlock']/a",
    #         'total_page': 1,  #11
    #         'handler': '3-chinabond',
    #         'category': '首页>业务操作>发行与付息兑付>债券种类>国债>发行计划',
    #         'website': '中国债券信息网中央结算公司',
    #         'redis_key': 'policy:audit:chinabond-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//ul[@id='pg_fxwj']/li[12]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//li[@class='liqxd1']/span[@class='unlock']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinabond.com.cn/jsp/include/CB_CN/issue/issuemiddleinclude.jsp?form_subbonds=&form_bondtype=21770&form_bondtype1=21770&form_issueyear=&form_issuenum=&form_keyword=&form_salescompany=&form_salescompanyName=%C8%AB%B2%BF%D6%F7%B3%D0%CF%FA%C9%CC%28%CA%E4%C8%EB%B9%D8%BC%FC%D7%D6%B2%E9%D1%AF%29&form_issuepersonal=&form_issuepersonalName=%C8%AB%B2%BF%B7%A2%D0%D0%C8%CB%28%CA%E4%C8%EB%B9%D8%BC%FC%D7%D6%B2%E9%D1%AF%29&form_cxpj=ROOT%3E%D2%B5%CE%F1%B2%D9%D7%F7%3E%B7%A2%D0%D0%D3%EB%B8%B6%CF%A2%B6%D2%B8%B6%3E%D5%AE%C8%AF%D6%D6%C0%E0%3E%B9%FA%D5%AE&form_zzlx=%B9%FA%D5%AE&xxlx=fxyc&_tp_fxwj=1#',
    #         'list_parse_rule': "//li[@class='liqxd1']/span[@class='unlock']/a",
    #         'total_page': 1,  #
    #         'handler': '3-chinabond',
    #         'category': '首页>业务操作>发行与付息兑付>债券种类>国债>发行预测',
    #         'website': '中国债券信息网中央结算公司',
    #         'redis_key': 'policy:audit:chinabond-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//ul[@id='pg_fxwj']/li[12]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//li[@class='liqxd1']/span[@class='unlock']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.chinabond.com.cn/jsp/include/CB_CN/issue/issuemiddleinclude.jsp?form_subbonds=&form_bondtype=21770&form_bondtype1=21770&form_issueyear=&form_issuenum=&form_keyword=&form_salescompany=&form_salescompanyName=%C8%AB%B2%BF%D6%F7%B3%D0%CF%FA%C9%CC%28%CA%E4%C8%EB%B9%D8%BC%FC%D7%D6%B2%E9%D1%AF%29&form_issuepersonal=&form_issuepersonalName=%C8%AB%B2%BF%B7%A2%D0%D0%C8%CB%28%CA%E4%C8%EB%B9%D8%BC%FC%D7%D6%B2%E9%D1%AF%29&form_cxpj=ROOT%3E%D2%B5%CE%F1%B2%D9%D7%F7%3E%B7%A2%D0%D0%D3%EB%B8%B6%CF%A2%B6%D2%B8%B6%3E%D5%AE%C8%AF%D6%D6%C0%E0%3E%B9%FA%D5%AE&form_zzlx=%B9%FA%D5%AE&xxlx=fxdf&_tp_fxwj=1#',
    #         'list_parse_rule': "//li[@class='liqxd1']/span[@class='unlock']/a",
    #         'total_page': 1,  #
    #         'handler': '3-chinabond',
    #         'category': '首页>业务操作>发行与付息兑付>债券种类>国债>付息兑付',
    #         'website': '中国债券信息网中央结算公司',
    #         'redis_key': 'policy:audit:chinabond-5',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//ul[@id='pg_fxwj']/li[12]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//li[@class='liqxd1']/span[@class='unlock']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://xxgk.mca.gov.cn:8081/new_gips/gipsSearch',
    #         'list_parse_rule': "//tbody/tr/td[1]/a",
    #         'total_page': 1,  #
    #         'handler': '3-mca',
    #         'category': '首页> 信息公开> 政府信息公开专栏> 信息公开目录',
    #         'website': '中华人民共和国民政部',
    #         'redis_key': 'policy:audit:mca',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//ul[@id='pg_fxwj']/li[12]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//tbody/tr/td[1]/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.iachina.cn/col/col1724/index.html',
    #         'list_parse_rule': "//li/div[@class='list-top']/a",
    #         'total_page': 1,  #143
    #         'handler': '3-iachina',
    #         'category': '监管要闻   ',
    #         'website': '中国保险业协会',
    #         'redis_key': 'policy:audit:iachina-1',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='default_pgBtn default_pgNext']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//li/div[@class='list-top']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.iachina.cn/col/col22/index.html',
    #         'list_parse_rule': "//div[@class='xhyw-title']/a",
    #         'total_page': 1,  #252
    #         'handler': '3-iachina',
    #         'category': '协会要闻  ',
    #         'website': '中国保险业协会',
    #         'redis_key': 'policy:audit:iachina-2',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='default_pgBtn default_pgNext']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//div[@class='xhyw-title']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
    #
    # {
    #     "site_config": {
    #         'index_url': 'http://www.iachina.cn/col/col23/index.html',
    #         'list_parse_rule': "//li/div[@class='list-top']/a",
    #         'total_page': 1,  #260
    #         'handler': '3-iachina',
    #         'category': '行业要文  ',
    #         'website': '中国保险业协会',
    #         'redis_key': 'policy:audit:iachina-3',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='default_pgBtn default_pgNext']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//li/div[@class='list-top']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },

    # {
    #     "site_config": {
    #         'index_url': 'http://www.iachina.cn/col/col24/index.html',
    #         'list_parse_rule': "//li/div[@class='list-top']/a",
    #         'total_page': 3,  #37
    #         'handler': '3-iachina',
    #         'category': '公告通知  ',
    #         'website': '中国保险业协会',
    #         'redis_key': 'policy:audit:iachina-4',
    #     },
    #     "sel_config": {
    #         'chrome_init': ['acceptSslCerts'],
    #         'proxy_type': '',
    #         'next_page_btn': {
    #             'by_xpath': "//a[@class='default_pgBtn default_pgNext']",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #         'waiting_page': {
    #             'by_xpath': "//li/div[@class='list-top']/a",
    #             'by_id': '',
    #             'by_class': '',
    #         },
    #     },
    # },
)
