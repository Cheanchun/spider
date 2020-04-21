import sys


class BaseConfig(object):
    '''API信息获取spider 配置'''
    # JiYan user/passwd
    HOME_PATH = sys.path[0]
    USER = 'zsyhcdjy'
    PASSWD = 'secneo123'
    # redis配置
    HOST = "47.105.54.129"
    PORT = 6388
    DB_INDEX = 14  # 失信移除
    REDIS_SET_NAME = "order_company"
    PASSWORD = "admin"
    DOC_OUT_PUT_PATH = ""
    EXCEL_OUT_PUT_PATH = ""
    # 'tab': 'ent_tab',  # 查询所有
    # 'tab': 'ill_tab',  # 仅仅查询严重失信企业的信息
    # 'tab': 'excep_tab',  # 经营异常,所有异常的状态均能查询
    SEARCH_TYPE = "ent_tab"
