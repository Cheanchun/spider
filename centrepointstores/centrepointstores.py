"""


https://3hwowx4270-dsn.algolia.net/1/indexes/*/queries?X-Algolia-API-Key=4c4f62629d66d4e9463ddb94b9217afb&X-Algolia-Application-Id=3HWOWX4270&X-Algolia-Agent=Algolia%20for%20vanilla%20JavaScript%202.9.7
https://lm8x36l8la-dsn.algolia.net/1/indexes/*/queries?X-Algolia-API-Key=7a625e3a548ccdd0393b5565896c5d89&X-Algolia-Application-Id=LM8X36L8LA&X-Algolia-Agent=Algolia%20for%20vanilla%20JavaScript%202.9.7
https://lm8x36l8la-dsn.algolia.net/1/indexes/*/queries?X-Algolia-API-Key=7a625e3a548ccdd0393b5565896c5d89&X-Algolia-Application-Id=LM8X36L8LA&X-Algolia-Agent=Algolia%20for%20vanilla%20JavaScript%202.9.7
https://lm8x36l8la-dsn.algolia.net/1/indexes/*/queries?X-Algolia-API-Key=7a625e3a548ccdd0393b5565896c5d89&X-Algolia-Application-Id=LM8X36L8LA&X-Algolia-Agent=Algolia%20for%20vanilla%20JavaScript%202.9.7
Request Method: POST
"""
import json
import os
import time

import requests
from lxml import etree

url = 'https://lm8x36l8la-dsn.algolia.net/1/indexes/*/queries?X-Algolia-API-Key=7a625e3a548ccdd0393b5565896c5d89&X-Algolia-Application-Id=LM8X36L8LA&X-Algolia-Agent=Algolia%20for%20vanilla%20JavaScript%202.9.7'
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "894",
    "Content-type": "application/x-www-form-urlencoded",
    "Host": "lm8x36l8la-dsn.algolia.net",
    "Origin": "https://www.centrepointstores.com",
    "Pragma": "no-cache",
    "Referer": "https://www.centrepointstores.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",

}
proxy = {'https': '192.168.2.117:7890'}
index_headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    'cookie': '__cfduid=dbf290a2e65185e09cb277a1178594c8d1612602793; _traceId=8a6a0ad3-685b-11eb-9a3e-79e6cbc0ae13-W; _lmgLan=en; b3pi=!wK5vEDL/6jfSJJ8AWbC7yci1H+z77dc3uNvUpjmyt3sjzPSfRrKeh//ZFs55l35Ir/xogVv04DPikg==; lmg_uid=Ch/kL2AeXamuQygdUIPrAg==; b2pi=!Xz3n/gHx7oHuB2kAWbC7yci1H+z77dxDw+SMeLQM9HKKzkfV96KapgoL6+hWoN6690jzBchWzisGEQ==; mt.v=2.1652898.1612602796780; alg_location=; moe_uuid=3ff4a9ac-7225-4a83-b7ed-4567a25914e0; _lmgfpc=""; lmgftt=100; JSESSIONID=1C27AA9F07D306132B5E594CFF436DD9; __cf_bm=061ac3a1ec76ba6f0d90690d9b36ea810ecb3886-1612620212-1800-ASrUMvKiQ1bZ8LziFnDi0y8aX5ieaMYXPImuDUJFwunMUfFhJhEO6c9cgoY0CYS7q4NbG79fXjDNI8HbXfR2dgQ=; __cfruid=fd4d06b0b983f15e327a44f3adc796aa81f4f8c2-1612620212; mt.sc=%7B%22i%22%3A1612620216558%2C%22d%22%3A%5B%5D%7D; selectedDeptsa=women; preSelectedDeptsa=women',
    "referer": "https://www.centrepointstores.com/sa/en/404",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",

}


def get_product(cate, page=0, file_dir=''):
    post_data = {"requests":
        [
            {"indexName": "prod_sa_centrepoint_Product",
             "params": ""
             }
        ],
    }
    temp = "query=*&hitsPerPage=42&page={pn}&facets=*&facetFilters=%5B%22inStock%3A1%22%2C%22approvalStatus%3A1%22%2C%22allCategories%3A{cate}%22%2C%22badge.title.en%3A-LASTCHANCE%22%5D&getRankingInfo=1&clickAnalytics=true&attributesToHighlight=null&analyticsTags=%5B%22{cate}%22%2C%22en%22%5D&attributesToRetrieve=concept%2CmanufacturerName%2Curl%2C333WX493H%2C345WX345H%2C505WX316H%2C550WX550H%2C499WX739H%2Cbadge%2Cname%2Csummary%2CwasPrice%2Cprice%2CemployeePrice%2CshowMoreColor%2CproductType%2CchildDetail%2Csibiling%2CthumbnailImg%2CgallaryImages%2CisConceptDelivery&numericFilters=price%20%3E%201.9&query=*&maxValuesPerFacet=500&tagFilters=%5B%5B%22babyshop%22%2C%22splash%22%2C%22lifestyle%22%2C%22shoemart%22%2C%22centrepoint%22%2C%22shoexpress%22%2C%22lipsy%22%2C%22sportsone%22%2C%22sminternational%22%5D%5D"
    time.sleep(1)
    post_data['requests'][0]['params'] = temp.format(pn=page, cate=cate)
    resp = requests.post(url, headers=headers, json=post_data, proxies=proxy)
    with open(os.path.join(file_dir, '{}pageContent.json'.format(page)), mode='w+', encoding='u8') as fp:
        fp.write(json.dumps(resp.json(), ensure_ascii=False))
    return resp


def get_main_category():
    xpath = "//div[@id='filter-form-block-02']/ul[@id='filter-form-sub-categories']/li[@id]/a[@id]"
    index_url = 'https://www.centrepointstores.com/sa/en/c/cpwomen-clothing'
    p_url = 'https://www.centrepointstores.com/sa/en/c/cpwomen-clothing-bottoms'
    resp = requests.get(p_url, headers=index_headers, proxies=proxy)
    html = etree.HTML(resp.text)
    category_dict = {
        "Bottoms": ["cpwomen-clothing-bottoms-jeans",
                    "cpwomen-clothing-bottoms-joggers",
                    "cpwomen-clothing-bottoms-leggingsandjeggings",
                    "cpwomen-clothing-bottoms-pantsandchinos",
                    "cpwomen-clothing-bottoms-skirtsandshorts", ],
        "Dresses": ["cpwomen-clothing-dresses", ],
        "Jumpsuits & Playsuits": ["cpwomen-clothing-jumpsuitsandplaysuits", ],
        "Lingerie": ["cpwomen-clothing-lingerie-bras",
                     "cpwomen-clothing-lingerie-lingeriesets",
                     "cpwomen-clothing-lingerie-panties",
                     "cpwomen-clothing-lingerie-shapewear", ],
        "Maternity Wear": ["cpwomen-clothing-maternitywear-dresses",
                           "cpwomen-clothing-maternitywear-nightwear",
                           "cpwomen-clothing-maternitywear-shapewear",
                           "cpwomen-clothing-maternitywear-swimwear",
                           "cpwomen-clothing-maternitywear-tops", ],
        "Modest Wear": ["cpwomen-clothing-modestwear", ],
        "Night Wear": ["cpwomen-clothing-nightwear-bottoms",
                       "cpwomen-clothing-nightwear-jumpsuits",
                       "cpwomen-clothing-nightwear-nightdress",
                       "cpwomen-clothing-nightwear-robes",
                       "cpwomen-clothing-nightwear-sets",
                       "cpwomen-clothing-nightwear-tops", ],
        "Sportswear & Activewear": ["cpwomen-clothing-sportswearandactivewear-bottoms",
                                    "cpwomen-clothing-sportswearandactivewear-hoodiesandsweatshirts",
                                    "cpwomen-clothing-sportswearandactivewear-sportsbras",
                                    "cpwomen-clothing-sportswearandactivewear-tshirtsandvests",
                                    "cpwomen-clothing-sportswearandactivewear-trackpantsandtracksuits", ],
        "Tops": ["cpwomen-clothing-tops-cardigansandsweaters",
                 "cpwomen-clothing-tops-coatsandjackets",
                 "cpwomen-clothing-tops-hoodiesandsweatshirts",
                 "cpwomen-clothing-tops-kimonos",
                 "cpwomen-clothing-tops-shirtsandblouses",
                 "cpwomen-clothing-tops-tshirtsandvests",
                 "cpwomen-clothing-tops-tunics", ],
        "Winter Wear": ["cpwomen-clothing-winterwear-cardigansandsweaters",
                        "cpwomen-clothing-winterwear-coatsandjackets",
                        "cpwomen-clothing-winterwear-hoodiesandsweatshirts", ],

    }
    category = [
        # Bottoms
        "cpwomen-clothing-bottoms-jeans",
        "cpwomen-clothing-bottoms-joggers",
        "cpwomen-clothing-bottoms-leggingsandjeggings",
        "cpwomen-clothing-bottoms-pantsandchinos",
        "cpwomen-clothing-bottoms-skirtsandshorts",
        # Dresses
        "cpwomen-clothing-dresses",
        # Jumpsuits & Playsuits
        "cpwomen-clothing-jumpsuitsandplaysuits",
        # Lingerie
        "cpwomen-clothing-lingerie-bras",
        "cpwomen-clothing-lingerie-lingeriesets",
        "cpwomen-clothing-lingerie-panties",
        "cpwomen-clothing-lingerie-shapewear",
        # Maternity Wear
        "cpwomen-clothing-maternitywear-dresses",
        "cpwomen-clothing-maternitywear-nightwear",
        "cpwomen-clothing-maternitywear-shapewear",
        "cpwomen-clothing-maternitywear-swimwear",
        "cpwomen-clothing-maternitywear-tops",
        # Modest Wear
        "cpwomen-clothing-modestwear",
        # Night Wear
        "cpwomen-clothing-nightwear-bottoms",
        "cpwomen-clothing-nightwear-jumpsuits",
        "cpwomen-clothing-nightwear-nightdress",
        "cpwomen-clothing-nightwear-robes",
        "cpwomen-clothing-nightwear-sets",
        "cpwomen-clothing-nightwear-tops",
        # Sportswear & Activewear
        "cpwomen-clothing-sportswearandactivewear-bottoms",
        "cpwomen-clothing-sportswearandactivewear-hoodiesandsweatshirts",
        "cpwomen-clothing-sportswearandactivewear-sportsbras",
        "cpwomen-clothing-sportswearandactivewear-tshirtsandvests",
        "cpwomen-clothing-sportswearandactivewear-trackpantsandtracksuits",
        # Tops
        "cpwomen-clothing-tops-cardigansandsweaters",
        "cpwomen-clothing-tops-coatsandjackets",
        "cpwomen-clothing-tops-hoodiesandsweatshirts",
        "cpwomen-clothing-tops-kimonos",
        "cpwomen-clothing-tops-shirtsandblouses",
        "cpwomen-clothing-tops-tshirtsandvests",
        "cpwomen-clothing-tops-tunics",
        # Winter Wear
        "cpwomen-clothing-winterwear-cardigansandsweaters",
        "cpwomen-clothing-winterwear-coatsandjackets",
        "cpwomen-clothing-winterwear-hoodiesandsweatshirts",
    ]
    return category
    cnt = 1
    item = html.xpath(xpath.format(0))
    while item:
        category.append(item)
        item = html.xpath(xpath.format(cnt))
        cnt += 1


def data_parse(resp: requests.Response):
    final_data = {}
    source_data = resp.json().get('results')[0].get('hits')
    for item in source_data:
        final_data['p_id'] = ''
        final_data['p_name'] = ''
        final_data['p_detail_url'] = ''
        final_data['p_picture'] = item.get('333WX493H')
        final_data['fact_price'] = item.get('price')
        final_data['ori_price'] = item.get('wasPrice')
        final_data['p_color'] = ''
        final_data['size'] = ''
    return resp.json().get('results')[0].get('nbPages')


def item(p_id='5528116'):
    p_url = "https://www.centrepointstores.com/ae/en/p/1019624/variantDetail"
    print(p_url)
    h = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "cookie": "__cfduid=d7b2608a561c12dcddcd6ac2385f65c251612627263; _traceId=833e520b-6894-11eb-993e-f9c451542b77-W; _lmgLan=en; lmg_uid=Ch/kMWAevT9vE6yOY5O8Ag==; b2pi=!CF8K9CfUlzwdHxoAWbC7yci1H+z77ermlADx0RWhHgG1PwYSGHt7Qecjn78v+48FT0DhnNpiWObFkg==; __cf_bm=03bf3cc5e6d661061e14fdce229f9162966a394a-1612627263-1800-Af1oqYFhHQs6Lfwlgybk4F4lbg7GpSI+n1XsVPB4uLoYcLljH+mhSnfdRIA156sJvUVkCQjMAHIscNSXq5mYGvQ=; __cfruid=441572584abdbc2579591c713334c7d450203e12-1612627263; b3pi=!F+H5EuVmj9oY4mUAWbC7yci1H+z77WwSXuEIySNfO4B1KFT11ZZXyc1o0Bq9i31yViO/Mtf3+M6eHjo=; JSESSIONID=CA43EC17DD4E6BBC8117FF26D53431F5; _app_deviceId=user_16126278269193559; mt.v=2.114842813.1612627830703; mt.sc=%7B%22i%22%3A1612627836634%2C%22d%22%3A%5B%5D%7D; moe_uuid=3ff4a9ac-7225-4a83-b7ed-4567a25914e0; b1pi=!1Lol/hXwPi+a0nYAWbC7yci1H+z77ebgMH/tLjWZC8GeAF1Y/MHtk+CHY6NngvBoiSxHumM51ti5aA==; alg_location=",
        "pragma": "no-cache",
        "referer": "https://www.centrepointstores.com/ae/en/c/cpwomen-clothing?p=2",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",

    }
    resp = requests.get(p_url, headers=h, proxies=proxy)
    print(resp.status_code)


def main():
    categorys = get_main_category()
    for category in categorys:
        # time.sleep(10)
        file_dir = os.path.join(os.getcwd(), category)
        os.mkdir(file_dir)
        print('category:{}'.format(category))
        resp = get_product(category)
        t_page = data_parse(resp)
        for page in range(1, t_page + 1):
            time.sleep(1)
            print('page:{}'.format(page))
            resp = get_product(category, page, file_dir)
            data_parse(resp)


if __name__ == '__main__':
    item()
