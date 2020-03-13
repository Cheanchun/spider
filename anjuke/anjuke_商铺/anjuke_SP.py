# encoding: utf-8
import datetime
import random
import time

import re
import redis
import requests
from lxml import etree

HOST = "47.105.54.129"
PORT = 6388
PWD = "admin"

r = redis.StrictRedis(host=HOST, port=PORT, password=PWD)
date = str(datetime.datetime.today().date())
agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
]
headers = [
    {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': '_ga=GA1.2.1985573990.1550408562; 58tj_uuid=66ea09d6-8237-4903-a5bd-a022b7a0fdf4; ajk_member_id=65331467; als=0; aQQ_ajkauthinfos=g9RpaQGH6WzcBYuu1GAYlF3kbmqBcZ8Nf56RBKPxp9fOmbkOqBeRffPeIi5wD%2FMdah4c4p7bEL0mS4vc0zgM; aQQ_ajkguid=EF049CBF-FC09-1EC3-1C93-CE6981BEC407; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1550408571; isp=true; lui=65331467%3A1; sessid=9808F60E-F629-417A-140C-53C06C371E72; lps=http%3A%2F%2Fwww.anjuke.com%2F%7C; ctid=15; twe=2; _gid=GA1.2.1269612667.1560305195; init_refer=; new_uv=14; new_session=0; wmda_uuid=76d3d0add0281f9dff7d3a3144b941fa; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; wmda_uuid=62207e356b40dff41930b0577503b2a0; wmda_new_uuid=1; wmda_session_id_6289197098934=1560305513538-1b585e01-6b43-736a; wmda_visited_projects=%3B6289197098934; wmda_session_id_6289197098934=1560305513538-1b585e01-6b43-736a; __xsptplus8=8.14.1560305195.1560305582.8%232%7Csp0.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23jj31fBrLqoIS0rw5P9uYQTWTfysBj0RH%23',
        'referer': 'https://chengdu.anjuke.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    },
    {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'lps=https%3A%2F%2Fcd.sp.anjuke.com%2Fzu%2Fp2%2F%7Chttps%3A%2F%2Fcd.sp.anjuke.com%2Fzu%2F%3Ffrom%3Dnavigation; aQQ_ajkguid=288678ad-3dd7-478a-8616-039ebf555e06; sessid=7f2c80be-93b5-43da-83f2-50c7d42c771d; __xsptplusUT_8=1; 58tj_uuid=6f6beb6d-89b7-4620-86f0-38eb86200a6b; new_session=1; init_refer=https%253A%252F%252Fcd.sp.anjuke.com%252Fzu%252F%253Ffrom%253Dnavigation; new_uv=1; als=0; wmda_uuid=8714a3943e8905475daf4a1f33c01d84; wmda_new_uuid=1; wmda_session_id_6289197098934=1560306613647-50608af6-c323-9943; wmda_visited_projects=%3B6289197098934; __xsptplus8=8.1.1560306614.1560306614.1%234%7C%7C%7C%7C%7C%23%23fiDss_QryeqPqkSwEGtZFG6E2qJQnyPg%23',
        'referer': 'https://cd.sp.anjuke.com/zu/?from=navigation',
        'upgrade-insecure-requests': '1',
        'user-agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",

    }

]
urls = []
area_url = ['https://bj.sp.anjuke.com/zu/p%s/', 'https://tj.sp.anjuke.com/zu/p%s/', 'https://dl.sp.anjuke.com/zu/p%s/',
            'https://sjz.sp.anjuke.com/zu/p%s/', 'https://heb.sp.anjuke.com/zu/p%s/',
            'https://sy.sp.anjuke.com/zu/p%s/',
            'https://ty.sp.anjuke.com/zu/p%s/', 'https://cc.sp.anjuke.com/zu/p%s/', 'https://wei.sp.anjuke.com/zu/p%s/',
            'https://hhht.sp.anjuke.com/zu/p%s/', 'https://yt.sp.anjuke.com/zu/p%s/',
            'https://sh.sp.anjuke.com/zu/p%s/',
            'https://hz.sp.anjuke.com/zu/p%s/', 'https://su.sp.anjuke.com/zu/p%s/', 'https://nj.sp.anjuke.com/zu/p%s/',
            'https://wx.sp.anjuke.com/zu/p%s/', 'https://jn.sp.anjuke.com/zu/p%s/', 'https://qd.sp.anjuke.com/zu/p%s/',
            'https://ks.sp.anjuke.com/zu/p%s/', 'https://nb.sp.anjuke.com/zu/p%s/', 'https://nc.sp.anjuke.com/zu/p%s/',
            'https://fz.sp.anjuke.com/zu/p%s/', 'https://hf.sp.anjuke.com/zu/p%s/', 'https://xz.sp.anjuke.com/zu/p%s/',
            'https://zb.sp.anjuke.com/zu/p%s/', 'https://sz.sp.anjuke.com/zu/p%s/', 'https://gz.sp.anjuke.com/zu/p%s/',
            'https://fs.sp.anjuke.com/zu/p%s/', 'https://cs.sp.anjuke.com/zu/p%s/', 'https://san.sp.anjuke.com/zu/p%s/',
            'https://hui.sp.anjuke.com/zu/p%s/', 'https://dg.sp.anjuke.com/zu/p%s/', 'https://hk.sp.anjuke.com/zu/p%s/',
            'https://zh.sp.anjuke.com/zu/p%s/', 'https://zs.sp.anjuke.com/zu/p%s/', 'https://xm.sp.anjuke.com/zu/p%s/',
            'https://nn.sp.anjuke.com/zu/p%s/', 'https://qz.sp.anjuke.com/zu/p%s/', 'https://lzh.sp.anjuke.com/zu/p%s/',
            'https://cd.sp.anjuke.com/zu/p%s/', 'https://cq.sp.anjuke.com/zu/p%s/', 'https://wh.sp.anjuke.com/zu/p%s/',
            'https://zz.sp.anjuke.com/zu/p%s/', 'https://xa.sp.anjuke.com/zu/p%s/', 'https://km.sp.anjuke.com/zu/p%s/',
            'https://gy.sp.anjuke.com/zu/p%s/', 'https://lz.sp.anjuke.com/zu/p%s/', 'https://ly.sp.anjuke.com/zu/p%s/']
while area_url:
    url = area_url.pop(0)
    page_num = [i for i in range(1, 31)]
    random.shuffle(page_num)
    urls += [url % i for i in page_num]
if not r.exists("all_urls"):
    for url in urls:
        r.lpush("all_urls", url)

print(urls, len(urls))
# time.sleep(10000)

with open("./anjukeSP{}.json".format(time.time()), mode="a+", encoding="utf-8") as fp:
    while r.exists("all_urls"):
        url = urls.pop(0)
        print("-----------------  开始爬取url:%s  ------------------------" % url)
        time.sleep(random.randint(5, 10))
        proxy = {"https://": ""}
        # session.proxies = proxy
        resp = requests.get(url, headers=random.choice(headers), allow_redirects=False)
        if "没有结果，请换个搜索词或试试筛选吧!" in resp.text:
            continue
        print(resp.status_code)
        html = etree.HTML(resp.text)
        items = html.xpath("//div[@id='list-content']/div[@class='list-item']")  #
        for item in items:
            data = {}
            try:
                floor = item.xpath(".//dl/dd/span[2]/text()")[0]
            except Exception as e:
                print("--------------------------商铺楼层解析错误:%s:%s-----------------------" % e.args, url)
                continue
            if "1" in floor or "一" in floor:
                # 字段:抓取时间.数据来源(安居客/中原地产)/网页url/具体地址/经纬度/租金/租期/面积
                data["crawler_date"] = date
                data["data_from"] = "安居客"
                page_url = item.xpath("./@link")[0]  # item.xpath("./@link")
                resp_info = requests.get(url=page_url, headers=random.choice(headers), allow_redirects=False)
                lat = re.search(pattern='lat: "(.+)"', string=resp_info.text)
                lng = re.search(pattern='lng: "(.+)"', string=resp_info.text)
                if lat and lng:
                    data["lng"] = lng.group(1)  # 经度
                    data["lat"] = lat.group(1)  # 纬度
                data["address"] = item.xpath("./dl/dd[2]/span//text()")[0]  # item.xpath("./dl/dd[2]/span//text()")

                #  出租信息 :
                rent_info = [i.strip() for i in item.xpath("./div/div//text()") if i.strip()]
                if len(rent_info) == 2:
                    data["rent"] = rent_info[0]
                    data["rent_time"] = rent_info[1]
                else:
                    print("-----------------------租金和租期获取错误:%s----------------------" % url)
                    time.sleep(2)
                data["size"] = item.xpath(".//dd/span/text()")[0]  # item.xpath(".//dd/span/text()")[0]
                print(data)
                # data = json.dumps(data, skipkeys=True, ensure_ascii=False, encoding="utf-8")
                fp.write(str(data) + "," + "\n")
            else:
                print("-------------------------floor info:%s-------------------------" % floor)
                time.sleep(1)
        fp.flush()
        print("-----------数据保存成功--------------")
