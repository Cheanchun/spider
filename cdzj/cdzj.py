# coding:utf-8
import datetime

import pymongo
import requests
from lxml import etree

url = 'https://zw.cdzj.chengdu.gov.cn/zwdt/SCXX/Default.aspx?action=ucEveryday2'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    # "Cookie": "yfx_c_g_u_id_10000057=_ck19080522060316519906274923176; yfx_mr_10000057=%3A%3Amarket_type_free_search%3A%3A%3A%3Abaidu%3A%3A%3A%3A%3A%3A%3A%3Awww.baidu.com%3A%3A%3A%3Apmf_from_free_search; yfx_key_10000057=; ASP.NET_SessionId=el0arsuwdm001l3mn4if0355; FntCookie=TraditionalOrSimplized=0",
    "Host": "zw.cdzj.chengdu.gov.cn",
    "Pragma": "no-cache",
    "Referer": "https://zw.cdzj.chengdu.gov.cn/zwdt/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}


def get_page():
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        return resp
    else:
        print('page get fail...')


def parse_data(resp: requests.Response):
    date = datetime.datetime.now()
    html = etree.HTML(resp.text)
    final_data = {}
    trs = html.xpath("//div[@class='rightContent']/div[@class='rightContent']//tr[position()>2]//text()")
    clean_trs = []
    for item in trs:
        if item.strip():
            clean_trs.append(item.strip())
        else:
            clean_trs.append(0)
    print(clean_trs)
    final_data['crawler_time'] = date
    final_data['fir_center_area'] = clean_trs[1]
    final_data['fir_center_house_count'] = clean_trs[2]
    final_data['fir_house_total_size'] = clean_trs[3]
    final_data['fir_business_total_size'] = clean_trs[4]

    final_data['fir_country_area'] = clean_trs[6]
    final_data['fir_country_count'] = clean_trs[7]
    final_data['fir_country_house_total_size'] = clean_trs[8]
    final_data['fir_country_business_total_size'] = clean_trs[9]

    final_data['sec_center_area'] = clean_trs[16]
    final_data['sec_center_house_count'] = clean_trs[17]
    final_data['sec_house_total_size'] = clean_trs[18]
    final_data['sec_business_total_size'] = clean_trs[19]

    final_data['sec_country_area'] = clean_trs[21]
    final_data['sec_country_house_count'] = clean_trs[22]
    final_data['sec_country_total_size'] = clean_trs[23]
    final_data['sec_country_total_size'] = clean_trs[24]
    return final_data


def save_data(data):
    cnn = pymongo.MongoClient(host='47.105.54.129', port=27017)
    db = cnn.shixin
    res = db.authenticate('chean', 'scc57295729')  # 验证
    col = db.cdzj
    col.insert(data)


if __name__ == '__main__':
    data = parse_data(get_page())
    save_data(data)
