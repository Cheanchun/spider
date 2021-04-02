# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import json
import time

import pymongo
import redis
import requests
from lxml import etree

url = 'https://ppwapi.simuwang.com/fund/getNavData'  # 数据请求
index_url = 'https://dc.simuwang.com/product/HF00005V8X.html?cid=CO0000029C'
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "66",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "Hm_lvt_c3f6328a1a952e922e996c667234cdae=1617098359,1617261604; need_update_password=1; smppw_tz_auth=1; http_tK_cache=a71ab2beb738b91c113ee3491c0de05f9881b79b; cur_ck_time=1617262764; ck_request_key=jHhggNiAN2cq85XLsVHeRSHXSmFYf2Q5qjxeN69aBBY%3D; passport=1033896%09u3960723742121%09BQUFBQwAAQldUwQBWlBWDFJcAQEGCgkJAFZeXgYHAVY%3D9710d4c4e7; certification=1; qualified_investor=1; evaluation_result=2; focus-certification-pop=-1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221033896%22%2C%22first_id%22%3A%221033896%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221788292c1ad34e-018aa92c391987-5c173a1b-1049088-1788292c1ae527%22%7D; Hm_lpvt_c3f6328a1a952e922e996c667234cdae=1617267840",
    "Host": "ppwapi.simuwang.com",
    "Origin": "https://dc.simuwang.com",
    "Referer": "https://dc.simuwang.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
}

user_redis = redis.Redis(host='47.105.54.129', port=6388, password='admin')
cnn = pymongo.MongoClient(host='47.105.54.129', port=27017)
db = cnn.shixin
db.authenticate("chean", "scc57295729")


def data_request(_id, pn):
    """

    :param _id:
    :param pn:
    :return:
    """

    post_data = {
        "id": _id,
        "muid": "1033896",
        "page": pn,
        "size": "20",
        "ENCODE": "2",
        "USER_ID": "1033896",

    }
    resp = requests.post(url, data=post_data, headers=headers)
    return resp.json()


def get_css(url):
    index_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "Hm_lvt_c3f6328a1a952e922e996c667234cdae=1617098359,1617261604; need_update_password=1; smppw_tz_auth=1; http_tK_cache=a71ab2beb738b91c113ee3491c0de05f9881b79b; cur_ck_time=1617262764; ck_request_key=jHhggNiAN2cq85XLsVHeRSHXSmFYf2Q5qjxeN69aBBY%3D; passport=1033896%09u3960723742121%09BQUFBQwAAQldUwQBWlBWDFJcAQEGCgkJAFZeXgYHAVY%3D9710d4c4e7; certification=1; qualified_investor=1; evaluation_result=2; focus-certification-pop=-1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221033896%22%2C%22first_id%22%3A%221033896%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221788292c1ad34e-018aa92c391987-5c173a1b-1049088-1788292c1ae527%22%7D; Hm_lpvt_c3f6328a1a952e922e996c667234cdae=1617277407",
        "Host": "dc.simuwang.com",
        "If-None-Match": 'W/"1d17e-io308fQP6cgs/rbs5h431zc5XTs"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    }
    url = 'https://dc.simuwang.com/product/HF00004XUU.html'
    resp = requests.get(url, headers=index_headers)
    return resp.json()


def convert_num(css_num, item_map):
    return item_map.get(css_num)


def convert(h):
    h_class = h.xpath('//*/@class')
    values = h.xpath('//text()')
    s = ''
    for c, v, in zip(h_class, values):
        if convert_num(c, item_map):
            s += str(v)
    return s


if __name__ == '__main__':
    with open('t.txt', mode='r', encoding='u8') as fp:
        content = fp.readline().strip()
        cnt = 0
        while content:
            time.sleep(10)

            cnt += 1
            page = 1
            p_name = content.split()[0].strip()
            p_url = content.split()[1].strip()
            p_code = p_url.rsplit('/')[-1].split('.')[0]
            col = db['simuwang']
            print('[当前进度：{cnt}/48]-[产品名称：{p_name}]-[抓取地址:{url}]'.format(cnt=cnt, p_name=p_name, url=p_url))
            content = fp.readline().strip()
            res_data = data_request(p_code, page).get('data')
            pager = res_data.get('pager')
            data_list = res_data.get('data')
            css_style = user_redis.get(p_code)
            item_map = json.loads(css_style, encoding='u8')
            while data_list:
                for item in data_list:
                    final_data = {'product_name': p_name, 'url': p_url}
                    date = item.get('pd')
                    value_html_1 = etree.HTML(item.get('n'))
                    value_html_2 = etree.HTML(item.get('cnw'))
                    value_html_3 = etree.HTML(item.get('cn'))
                    total_pure_value = convert(value_html_1)
                    final_data['value_date'] = item.get('pd')
                    final_data['pure_value'] = convert(value_html_1)
                    final_data['total_value(yes)'] = convert(value_html_3)
                    final_data['total_value(no)'] = convert(value_html_2)
                    final_data['delta'] = item.get('pc') + '%'
                    col.insert(final_data)
                time.sleep(2)
                print('[正在抓取第--{}--页]'.format(page))
                page += 1
                res_data = data_request(p_code, page).get('data')
                data_list = res_data.get('data')
