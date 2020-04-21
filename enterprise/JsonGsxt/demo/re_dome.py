# -*- coding: utf-8 -*-
"""
@Date       :2018/12/28
@Author     :
@Software   :Pycharm
"""
import json

import re
import redis

r = redis.Redis(host="47.105.54.129", port=6388, password="admin", db=1)
data_list = r.zrange(name="in_shixin", start=0, end=r.zcard("in_shixin"))
# data_list = r.zrange(name="in_shixin", start=0, end=100)
for item in data_list:
    print json.dumps(item, skipkeys=True, ensure_ascii=False, encoding="utf-8")
    title1 = eval(item.replace("null","None")).get(u"noticeTitle")
    # st = u"关于艾旺计算机信息网络系统（上海）有限公司北京办事处列入严重违法失信企业名单的决定"
    title = u"关于南宁光旭糖业有限责任公司列入严重违法失信企业名单公告"
    res = re.search(pattern=u"列入(.+单)的?.", string=title) # todo test
    if res:
        print res.group(1)
    else:
        print "match fail---------------"
        pass
