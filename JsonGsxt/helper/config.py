import sys

PROXY_URL = "http://http.tiqu.alicdns.com/getip3?num=1&type=2&pro=0&city=0&yys=0&port=1&pack=43054&ts=0&ys=0&cs=0&lb=1&sb=0&pb=45&mr=2&regions=&gm=4"
In_URL = "http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html?noticeType=21&areaid=100000&noticeTitle=&regOrg=%d"
Remove_URL = "http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html?noticeType=22&areaid=100000&noticeTitle=&regOrg=%d"
NOTICE_BASE_URL = "http://www.gsxt.gov.cn/affiche-query-info-inspect.html?noticeId=%s&datafrom=&provinceid=100000"
REDIS_IN_KEY = "remove_shixin"
REDIS_OUT_KEY = "remove_shixin"
SCORE = 0
USE_PROXY_API = True
USE_PROXY_IMG = False
TITLE_PATTERN_1 = "关于(.+?)(移出+?|的移出+?)"
TITLE_PATTERN_2 = "(.+?)(移出+?|的移出+?)"
REG_NUM_PATTERN = "([0-9A-Z]{18})[\)）/]|([0-9A-Z]{13})[\)）/]|([0-9A-Z]{15})[\)）/]"
IMG_PATH = "/home/chean/remove_notice/img_temp/notice_temp.png"
CREATE_PATH_CMD_1 = "cp -a /home/chean/remove_notice/pre_data/失信企业移出信息收集.docx {path}/{date}/失信企业移出信息收集.docx;"
CREATE_PATH_CMD_2 = "cp -a /home/chean/remove_notice/pre_data/失信名单移出登记表.xlsx {path}/{date}/失信名单移出登记表.xlsx"
FILE_DOC_NAME = "失信企业移出信息收集.docx"
FILE_EXC_NAME = "失信名单移出登记表.xlsx"


class BaseConfig(object):
    """API信息获取spider 配置"""
    HOME_PATH = sys.path[0]
    HOST = "127.0.0.1"
    PORT = 6388
    DB_INDEX = 15
    REDIS_SET_NAME = "remove_shixin"
    PASSWORD = "admin"
    FILE_PATH = "/datas/remove_shixin"
    SEARCH_TYPE = "ent_tab"
    # todo 有新的地区直接加载这里
    SPECIAL_AREA = ["广州市荔湾区工商行政管理局", "广州市白云区工商行政管理局",
                    "广州市海珠区工商行政管理局", "广州市增城区工商行政管理局",
                    "广州市工商行政管理局", "辽宁省市场监督管理局",
                    "广州市荔湾区市场监督管理局", "广州市天河区工商行政管理局",
                    "广州市天河区工商行政管理局", "广州市市场监督管理局",
                    "广州市越秀区工商行政管理局", "广州市番禺区市场监督管理局",
                    "广州市海珠区市场监督管理局", "广州市天河区市场监督管理局",
                    "吉林省市场监督管理厅", "广州市越秀区市场监督管理局",
                    "广州市白云区市场监督管理局", "广州市从化区市场监督管理局",
                    "广州市增城区市场监督管理局", "吉林省工商行政管理局",
                    "广州市黄埔区市场和质量监督管理局", "广州市从化区工商行政管理局",
                    "广州市南沙区市场和质量监督管理局", "广州市黄埔区市场监督管理局",
                    "辽宁省工商行政管理局",
                    ]
    # todo 新地区如需新的解析规则,添加在这里,注意添加顺序,在列表后面依次添加
    SPECIAL_AREA_PATTERNS = ["(.+?)（统一社会信用",
                             "</p><p>(.+?)\(统一社会信用",
                             "(<p text-align: center font-size:16px>|<p>)(.+)</p>",
                             "(.+?)[\W]+（统一社会信用",
                             ]
