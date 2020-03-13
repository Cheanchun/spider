import re
import time

import redis
import requests
from lxml import etree

r = redis.StrictRedis(host="47.105.54.129", port=6388, password="admin", )

# proxies = []
proxies = r.zrangebyscore("proxy", 100, 100)
print(proxies)
url = "https://www.baidu.com"
resp = requests.get(url=url, proxies={"http://": "http://" + proxies.pop().decode("utf-8")}, allow_redirects=False)
print(resp)

html = etree.HTML(resp.text)
items = html.xpath("//div[@class='w1180']//div[@class='li-itemmod']")
'''//div[@class='li-side']/p[1]/strong'''
# print(items)
# print(len(items))
i = 0
for item in items:
    name = item.xpath("./div[@class='li-info']/h3/a/text()")[0].strip()
    addr = item.xpath("./div[@class='li-info']/address/text()")[0].strip()
    biuld_year = item.xpath("./div[@class='li-info']/p[@class='date']/text()")[0].strip()
    sale_num = item.xpath("./div[@class='li-info']/p[@class='bot-tag']/span/a/text()")[0].strip()
    url = item.xpath("./div[@class='li-info']/h3/a/@href")[0].strip()
    avg_price = item.xpath("./div[@class='li-side']/p[1]/strong/text()")[0].strip()
    _float = item.xpath(".//p[@class='price-txt']/text()")[0] if item.xpath(
        ".//p[@class='price-txt']/text()") else ""
    resp_local = requests.get(url=url, proxies={"http://": "http://" + proxies.pop().decode("utf-8")},
                              allow_redirects=False)
    with open("./info.txt", mode="w+", encoding="utf-8") as fp:
        fp.write(resp_local.text)
        num = 0
    while resp_local.status_code != 200 and num < 3:
        time.sleep(0.5)
        resp_local = requests.get(url=url, proxies={"http://": "http://" + proxies.pop().decode("utf-8")},
                                  allow_redirects=False)
        num += 1
    #     数据解析
    a = info_html = etree.HTML(resp_local.text)
    b = info_html.xpath("//dl[@class='basic-parms-mod']/dd[1]/text()")  # 住房类型
    c = info_html.xpath("//dd[@class='other-dd'][1]/text()")  # 物业收费
    d = info_html.xpath("//dl[@class='basic-parms-mod']/dd[3]/text()")  # 建筑面积
    e = info_html.xpath("//dd[@class='other-dd'][2]/text()")  # 总户数
    f = info_html.xpath("//dd[@class='other-dd'][3]/text()")  # 停车位
    g = info_html.xpath("//dl[@class='basic-parms-mod']/dd[7]/text()")  # 容积率
    h = info_html.xpath("//dd[@class='other-dd'][4]/text()")  # 绿化率
    i1 = info_html.xpath("//dd[@class='dd-column'][1]/text()")  # 开发商
    j = info_html.xpath("//dd[@class='dd-column'][2]/text()")  # 物业公司
    k = info_html.xpath("//dd[@class='dd-column'][3]/text()")  # 所属商圈
    print(a, b, c, d, e, f, g, h, i1, j, k, )
    local = re.search(string=resp_local.text, pattern='lat : "(.+?)",\W+lng : "(.+?)"')
    if local:
        position = "{},{}".format(local[1], local[2])
    else:
        position = ""

    print("name:", name, "addr:", addr, "year:", biuld_year[5:], "on sale:", sale_num[1:-1], "avg_price:",
          avg_price, "float:", _float.replace("↑", "+") if "↑" in _float else _float.replace("↓", "-"), "position",
          position, "url:", url)
    print(i)
    i += 1
