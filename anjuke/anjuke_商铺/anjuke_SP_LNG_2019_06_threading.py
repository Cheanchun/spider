# encoding: utf-8
import datetime
import random
import re
import sys
import time

import pymongo
import redis
import requests
from lxml import etree
import threading

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
        'user-agent': random.choice(agents),
    },
    {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'lps=https%3A%2F%2Fcd.sp.anjuke.com%2Fzu%2Fp2%2F%7Chttps%3A%2F%2Fcd.sp.anjuke.com%2Fzu%2F%3Ffrom%3Dnavigation; aQQ_ajkguid=288678ad-3dd7-478a-8616-039ebf555e06; sessid=7f2c80be-93b5-43da-83f2-50c7d42c771d; __xsptplusUT_8=1; 58tj_uuid=6f6beb6d-89b7-4620-86f0-38eb86200a6b; new_session=1; init_refer=https%253A%252F%252Fcd.sp.anjuke.com%252Fzu%252F%253Ffrom%253Dnavigation; new_uv=1; als=0; wmda_uuid=8714a3943e8905475daf4a1f33c01d84; wmda_new_uuid=1; wmda_session_id_6289197098934=1560306613647-50608af6-c323-9943; wmda_visited_projects=%3B6289197098934; __xsptplus8=8.1.1560306614.1560306614.1%234%7C%7C%7C%7C%7C%23%23fiDss_QryeqPqkSwEGtZFG6E2qJQnyPg%23',
        'referer': 'https://cd.sp.anjuke.com/zu/?from=navigation',
        'upgrade-insecure-requests': '1',
        'user-agent': random.choice(agents),
    }

]

lock = threading.Lock()

area_url = ['https://anshan.sp.anjuke.com/zu/p%s', 'https://anyang.sp.anjuke.com/zu/p%s',
            'https://anqing.sp.anjuke.com/zu/p%s', 'https://ankang.sp.anjuke.com/zu/p%s',
            'https://anshun.sp.anjuke.com/zu/p%s', 'https://aba.sp.anjuke.com/zu/p%s',
            'https://akesu.sp.anjuke.com/zu/p%s', 'https://ali.sp.anjuke.com/zu/p%s',
            'https://alaer.sp.anjuke.com/zu/p%s', 'https://alashanmeng.sp.anjuke.com/zu/p%s',
            'https://aomen.sp.anjuke.com/zu/p%s', 'https://anda.sp.anjuke.com/zu/p%s',
            'https://anqiu.sp.anjuke.com/zu/p%s', 'https://anning.sp.anjuke.com/zu/p%s',
            'https://anguo.sp.anjuke.com/zu/p%s', 'https://aershan.sp.anjuke.com/zu/p%s',
            'https://atushi.sp.anjuke.com/zu/p%s', 'https://anlu.sp.anjuke.com/zu/p%s',
            'https://beijing.sp.anjuke.com/zu/p%s', 'https://baoding.sp.anjuke.com/zu/p%s',
            'https://baotou.sp.anjuke.com/zu/p%s', 'https://binzhou.sp.anjuke.com/zu/p%s',
            'https://baoji.sp.anjuke.com/zu/p%s', 'https://bengbu.sp.anjuke.com/zu/p%s',
            'https://benxi.sp.anjuke.com/zu/p%s', 'https://beihai.sp.anjuke.com/zu/p%s',
            'https://bayinguoleng.sp.anjuke.com/zu/p%s', 'https://bazhong.sp.anjuke.com/zu/p%s',
            'https://bayannaoer.sp.anjuke.com/zu/p%s', 'https://bozhou.sp.anjuke.com/zu/p%s',
            'https://baiyin.sp.anjuke.com/zu/p%s', 'https://baicheng.sp.anjuke.com/zu/p%s',
            'https://baise.sp.anjuke.com/zu/p%s', 'https://baishan.sp.anjuke.com/zu/p%s',
            'https://boertala.sp.anjuke.com/zu/p%s', 'https://bijie.sp.anjuke.com/zu/p%s',
            'https://baoshan.sp.anjuke.com/zu/p%s', 'https://bazh.sp.anjuke.com/zu/p%s',
            'https://beian.sp.anjuke.com/zu/p%s', 'https://beipiao.sp.anjuke.com/zu/p%s',
            'https://botou.sp.anjuke.com/zu/p%s', 'https://bole.sp.anjuke.com/zu/p%s',
            'https://beiliu.sp.anjuke.com/zu/p%s', 'https://chengdu.sp.anjuke.com/zu/p%s',
            'https://chongqing.sp.anjuke.com/zu/p%s', 'https://cs.sp.anjuke.com/zu/p%s',
            'https://cz.sp.anjuke.com/zu/p%s', 'https://cc.sp.anjuke.com/zu/p%s',
            'https://cangzhou.sp.anjuke.com/zu/p%s', 'https://changji.sp.anjuke.com/zu/p%s',
            'https://chifeng.sp.anjuke.com/zu/p%s', 'https://changde.sp.anjuke.com/zu/p%s',
            'https://chenzhou.sp.anjuke.com/zu/p%s', 'https://chengde.sp.anjuke.com/zu/p%s',
            'https://changzhi.sp.anjuke.com/zu/p%s', 'https://chizhou.sp.anjuke.com/zu/p%s',
            'https://chuzhou.sp.anjuke.com/zu/p%s', 'https://chaoyang.sp.anjuke.com/zu/p%s',
            'https://chaozhou.sp.anjuke.com/zu/p%s', 'https://chuxiong.sp.anjuke.com/zu/p%s',
            'https://chaohu.sp.anjuke.com/zu/p%s', 'https://changdu.sp.anjuke.com/zu/p%s',
            'https://changge.sp.anjuke.com/zu/p%s', 'https://chongzuo.sp.anjuke.com/zu/p%s',
            'https://changshushi.sp.anjuke.com/zu/p%s', 'https://changyi.sp.anjuke.com/zu/p%s',
            'https://changning.sp.anjuke.com/zu/p%s', 'https://chibi.sp.anjuke.com/zu/p%s',
            'https://cengxi.sp.anjuke.com/zu/p%s', 'https://chishui.sp.anjuke.com/zu/p%s',
            'https://cixi.sp.anjuke.com/zu/p%s', 'https://chongzhou.sp.anjuke.com/zu/p%s',
            'https://dalian.sp.anjuke.com/zu/p%s', 'https://dg.sp.anjuke.com/zu/p%s',
            'https://deyang.sp.anjuke.com/zu/p%s', 'https://dali.sp.anjuke.com/zu/p%s',
            'https://dezhou.sp.anjuke.com/zu/p%s', 'https://dongying.sp.anjuke.com/zu/p%s',
            'https://daqing.sp.anjuke.com/zu/p%s', 'https://dandong.sp.anjuke.com/zu/p%s',
            'https://datong.sp.anjuke.com/zu/p%s', 'https://dazhou.sp.anjuke.com/zu/p%s',
            'https://dafeng.sp.anjuke.com/zu/p%s', 'https://dehong.sp.anjuke.com/zu/p%s',
            'https://dingzhou.sp.anjuke.com/zu/p%s', 'https://diqing.sp.anjuke.com/zu/p%s',
            'https://dingxi.sp.anjuke.com/zu/p%s', 'https://dxanling.sp.anjuke.com/zu/p%s',
            'https://dongtai.sp.anjuke.com/zu/p%s', 'https://dengzhou.sp.anjuke.com/zu/p%s',
            'https://dehui.sp.anjuke.com/zu/p%s', 'https://dangyang.sp.anjuke.com/zu/p%s',
            'https://dongfang.sp.anjuke.com/zu/p%s', 'https://danzhou.sp.anjuke.com/zu/p%s',
            'https://dunhuashi.sp.anjuke.com/zu/p%s', 'https://danyang.sp.anjuke.com/zu/p%s',
            'https://dashiqiao.sp.anjuke.com/zu/p%s', 'https://dengta.sp.anjuke.com/zu/p%s',
            'https://dunhuang.sp.anjuke.com/zu/p%s', 'https://delingha.sp.anjuke.com/zu/p%s',
            'https://daye.sp.anjuke.com/zu/p%s', 'https://duyun.sp.anjuke.com/zu/p%s',
            'https://dongxing.sp.anjuke.com/zu/p%s', 'https://dongyang.sp.anjuke.com/zu/p%s',
            'https://dexing.sp.anjuke.com/zu/p%s', 'https://danjiangkou.sp.anjuke.com/zu/p%s',
            'https://dujiangyan.sp.anjuke.com/zu/p%s', 'https://donggang.sp.anjuke.com/zu/p%s',
            'https://dengfeng.sp.anjuke.com/zu/p%s', 'https://eerduosi.sp.anjuke.com/zu/p%s',
            'https://enshi.sp.anjuke.com/zu/p%s', 'https://ezhou.sp.anjuke.com/zu/p%s',
            'https://enping.sp.anjuke.com/zu/p%s', 'https://emeishan.sp.anjuke.com/zu/p%s',
            'https://foshan.sp.anjuke.com/zu/p%s', 'https://fz.sp.anjuke.com/zu/p%s',
            'https://fuyang.sp.anjuke.com/zu/p%s', 'https://fushun.sp.anjuke.com/zu/p%s',
            'https://fuxin.sp.anjuke.com/zu/p%s', 'https://fuzhoushi.sp.anjuke.com/zu/p%s',
            'https://fangchenggang.sp.anjuke.com/zu/p%s', 'https://feichengshi.sp.anjuke.com/zu/p%s',
            'https://fengchengshi.sp.anjuke.com/zu/p%s', 'https://fengzhen.sp.anjuke.com/zu/p%s',
            'https://fenyang.sp.anjuke.com/zu/p%s', 'https://fukang.sp.anjuke.com/zu/p%s',
            'https://fuquan.sp.anjuke.com/zu/p%s', 'https://fuqing.sp.anjuke.com/zu/p%s',
            'https://fuan.sp.anjuke.com/zu/p%s', 'https://fengcheng.sp.anjuke.com/zu/p%s',
            'https://fuding.sp.anjuke.com/zu/p%s', 'https://guangzhou.sp.anjuke.com/zu/p%s',
            'https://gy.sp.anjuke.com/zu/p%s', 'https://guilin.sp.anjuke.com/zu/p%s',
            'https://ganzhou.sp.anjuke.com/zu/p%s', 'https://guangan.sp.anjuke.com/zu/p%s',
            'https://guigang.sp.anjuke.com/zu/p%s', 'https://guangyuan.sp.anjuke.com/zu/p%s',
            'https://ganzi.sp.anjuke.com/zu/p%s', 'https://gannan.sp.anjuke.com/zu/p%s',
            'https://guantao.sp.anjuke.com/zu/p%s', 'https://guoluo.sp.anjuke.com/zu/p%s',
            'https://guyuan.sp.anjuke.com/zu/p%s', 'https://gongzhulingshi.sp.anjuke.com/zu/p%s',
            'https://gaoyou.sp.anjuke.com/zu/p%s', 'https://gaomishi.sp.anjuke.com/zu/p%s',
            'https://guangshui.sp.anjuke.com/zu/p%s', 'https://gaizhou.sp.anjuke.com/zu/p%s',
            'https://geermu.sp.anjuke.com/zu/p%s', 'https://guanghan.sp.anjuke.com/zu/p%s',
            'https://gejiu.sp.anjuke.com/zu/p%s', 'https://guiping.sp.anjuke.com/zu/p%s',
            'https://guixi.sp.anjuke.com/zu/p%s', 'https://gaoanshi.sp.anjuke.com/zu/p%s',
            'https://gaozhou.sp.anjuke.com/zu/p%s', 'https://gaoyaoshi.sp.anjuke.com/zu/p%s',
            'https://gujiao.sp.anjuke.com/zu/p%s', 'https://gaobeidian.sp.anjuke.com/zu/p%s',
            'https://hangzhou.sp.anjuke.com/zu/p%s', 'https://hf.sp.anjuke.com/zu/p%s',
            'https://heb.sp.anjuke.com/zu/p%s', 'https://haikou.sp.anjuke.com/zu/p%s',
            'https://huizhou.sp.anjuke.com/zu/p%s', 'https://handan.sp.anjuke.com/zu/p%s',
            'https://huhehaote.sp.anjuke.com/zu/p%s', 'https://huanggang.sp.anjuke.com/zu/p%s',
            'https://huainan.sp.anjuke.com/zu/p%s', 'https://huangshan.sp.anjuke.com/zu/p%s',
            'https://hebi.sp.anjuke.com/zu/p%s', 'https://hengyang.sp.anjuke.com/zu/p%s',
            'https://huzhou.sp.anjuke.com/zu/p%s', 'https://hengshui.sp.anjuke.com/zu/p%s',
            'https://hanzhong.sp.anjuke.com/zu/p%s', 'https://huaian.sp.anjuke.com/zu/p%s',
            'https://huangshi.sp.anjuke.com/zu/p%s', 'https://heze.sp.anjuke.com/zu/p%s',
            'https://huaihua.sp.anjuke.com/zu/p%s', 'https://huaibei.sp.anjuke.com/zu/p%s',
            'https://huludao.sp.anjuke.com/zu/p%s', 'https://heyuan.sp.anjuke.com/zu/p%s',
            'https://honghe.sp.anjuke.com/zu/p%s', 'https://hami.sp.anjuke.com/zu/p%s',
            'https://hegang.sp.anjuke.com/zu/p%s', 'https://hulunbeier.sp.anjuke.com/zu/p%s',
            'https://haibei.sp.anjuke.com/zu/p%s', 'https://haidong.sp.anjuke.com/zu/p%s',
            'https://hainan.sp.anjuke.com/zu/p%s', 'https://hechi.sp.anjuke.com/zu/p%s',
            'https://heihe.sp.anjuke.com/zu/p%s', 'https://hexian.sp.anjuke.com/zu/p%s',
            'https://hezhou.sp.anjuke.com/zu/p%s', 'https://hailaer.sp.anjuke.com/zu/p%s',
            'https://huoqiu.sp.anjuke.com/zu/p%s', 'https://hetian.sp.anjuke.com/zu/p%s',
            'https://huangnan.sp.anjuke.com/zu/p%s', 'https://hexi.sp.anjuke.com/zu/p%s',
            'https://huadian.sp.anjuke.com/zu/p%s', 'https://heshan.sp.anjuke.com/zu/p%s',
            'https://hailin.sp.anjuke.com/zu/p%s', 'https://haicheng.sp.anjuke.com/zu/p%s',
            'https://hunchun.sp.anjuke.com/zu/p%s', 'https://huanghua.sp.anjuke.com/zu/p%s',
            'https://hejian.sp.anjuke.com/zu/p%s', 'https://hancheng.sp.anjuke.com/zu/p%s',
            'https://huaying.sp.anjuke.com/zu/p%s', 'https://houma.sp.anjuke.com/zu/p%s',
            'https://hanchuan.sp.anjuke.com/zu/p%s', 'https://huaying2.sp.anjuke.com/zu/p%s',
            'https://heshanshi.sp.anjuke.com/zu/p%s', 'https://huixian.sp.anjuke.com/zu/p%s',
            'https://huazhou.sp.anjuke.com/zu/p%s', 'https://huozhou.sp.anjuke.com/zu/p%s',
            'https://honghu.sp.anjuke.com/zu/p%s', 'https://hongjiang.sp.anjuke.com/zu/p%s',
            'https://helong.sp.anjuke.com/zu/p%s', 'https://haimen.sp.anjuke.com/zu/p%s',
            'https://haining.sp.anjuke.com/zu/p%s', 'https://haiyang.sp.anjuke.com/zu/p%s',
            'https://jinan.sp.anjuke.com/zu/p%s', 'https://jx.sp.anjuke.com/zu/p%s',
            'https://jilin.sp.anjuke.com/zu/p%s', 'https://jiangmen.sp.anjuke.com/zu/p%s',
            'https://jingmen.sp.anjuke.com/zu/p%s', 'https://jinzhou.sp.anjuke.com/zu/p%s',
            'https://jingdezhen.sp.anjuke.com/zu/p%s', 'https://jian.sp.anjuke.com/zu/p%s',
            'https://jining.sp.anjuke.com/zu/p%s', 'https://jinhua.sp.anjuke.com/zu/p%s',
            'https://jieyang.sp.anjuke.com/zu/p%s', 'https://jinzhong.sp.anjuke.com/zu/p%s',
            'https://jiujiang.sp.anjuke.com/zu/p%s', 'https://jiaozuo.sp.anjuke.com/zu/p%s',
            'https://jincheng.sp.anjuke.com/zu/p%s', 'https://jingzhou.sp.anjuke.com/zu/p%s',
            'https://jiamusi.sp.anjuke.com/zu/p%s', 'https://jiuquan.sp.anjuke.com/zu/p%s',
            'https://jixi.sp.anjuke.com/zu/p%s', 'https://jiyuan.sp.anjuke.com/zu/p%s',
            'https://jinchang.sp.anjuke.com/zu/p%s', 'https://jiayuguan.sp.anjuke.com/zu/p%s',
            'https://jiangyin.sp.anjuke.com/zu/p%s', 'https://jingjiang.sp.anjuke.com/zu/p%s',
            'https://jianyangshi.sp.anjuke.com/zu/p%s', 'https://jintan.sp.anjuke.com/zu/p%s',
            'https://jinshi.sp.anjuke.com/zu/p%s', 'https://jieshou.sp.anjuke.com/zu/p%s',
            'https://jishou.sp.anjuke.com/zu/p%s', 'https://jinghong.sp.anjuke.com/zu/p%s',
            'https://jinjiangshi.sp.anjuke.com/zu/p%s', 'https://jianou.sp.anjuke.com/zu/p%s',
            'https://jiangshan.sp.anjuke.com/zu/p%s', 'https://jinggangshan.sp.anjuke.com/zu/p%s',
            'https://jiaohe.sp.anjuke.com/zu/p%s', 'https://jiaozhoux.sp.anjuke.com/zu/p%s',
            'https://jurong.sp.anjuke.com/zu/p%s', 'https://jiande.sp.anjuke.com/zu/p%s',
            'https://jizhoushi.sp.anjuke.com/zu/p%s', 'https://jiangyoushi.sp.anjuke.com/zu/p%s',
            'https://km.sp.anjuke.com/zu/p%s', 'https://ks.sp.anjuke.com/zu/p%s',
            'https://kaifeng.sp.anjuke.com/zu/p%s', 'https://kashi.sp.anjuke.com/zu/p%s',
            'https://kelamayi.sp.anjuke.com/zu/p%s', 'https://kenli.sp.anjuke.com/zu/p%s',
            'https://lezilesu.sp.anjuke.com/zu/p%s', 'https://kuerle.sp.anjuke.com/zu/p%s',
            'https://kuitun.sp.anjuke.com/zu/p%s', 'https://kaili.sp.anjuke.com/zu/p%s',
            'https://kaiping.sp.anjuke.com/zu/p%s', 'https://kaiyuan.sp.anjuke.com/zu/p%s',
            'https://kaiyuan2.sp.anjuke.com/zu/p%s', 'https://lanzhou.sp.anjuke.com/zu/p%s',
            'https://langfang.sp.anjuke.com/zu/p%s', 'https://luoyang.sp.anjuke.com/zu/p%s',
            'https://liuzhou.sp.anjuke.com/zu/p%s', 'https://laiwu.sp.anjuke.com/zu/p%s',
            'https://luan.sp.anjuke.com/zu/p%s', 'https://luzhou.sp.anjuke.com/zu/p%s',
            'https://lijiang.sp.anjuke.com/zu/p%s', 'https://linyi.sp.anjuke.com/zu/p%s',
            'https://liaocheng.sp.anjuke.com/zu/p%s', 'https://lianyungang.sp.anjuke.com/zu/p%s',
            'https://lishui.sp.anjuke.com/zu/p%s', 'https://loudi.sp.anjuke.com/zu/p%s',
            'https://leshan.sp.anjuke.com/zu/p%s', 'https://liaoyang.sp.anjuke.com/zu/p%s',
            'https://lasa.sp.anjuke.com/zu/p%s', 'https://linfen.sp.anjuke.com/zu/p%s',
            'https://longyan.sp.anjuke.com/zu/p%s', 'https://luohe.sp.anjuke.com/zu/p%s',
            'https://liangshan.sp.anjuke.com/zu/p%s', 'https://liupanshui.sp.anjuke.com/zu/p%s',
            'https://liaoyuan.sp.anjuke.com/zu/p%s', 'https://laibin.sp.anjuke.com/zu/p%s',
            'https://lingcang.sp.anjuke.com/zu/p%s', 'https://linxia.sp.anjuke.com/zu/p%s',
            'https://linyishi.sp.anjuke.com/zu/p%s', 'https://linzhi.sp.anjuke.com/zu/p%s',
            'https://longnan.sp.anjuke.com/zu/p%s', 'https://lvliang.sp.anjuke.com/zu/p%s',
            'https://linhaishi.sp.anjuke.com/zu/p%s', 'https://longhaishi.sp.anjuke.com/zu/p%s',
            'https://lilingshi.sp.anjuke.com/zu/p%s', 'https://linqing.sp.anjuke.com/zu/p%s',
            'https://longkou.sp.anjuke.com/zu/p%s', 'https://laiyang.sp.anjuke.com/zu/p%s',
            'https://leiyang.sp.anjuke.com/zu/p%s', 'https://liyang.sp.anjuke.com/zu/p%s',
            'https://longjing.sp.anjuke.com/zu/p%s', 'https://linjiang.sp.anjuke.com/zu/p%s',
            'https://lingyuan.sp.anjuke.com/zu/p%s', 'https://linzhoushi.sp.anjuke.com/zu/p%s',
            'https://lingbao.sp.anjuke.com/zu/p%s', 'https://lucheng.sp.anjuke.com/zu/p%s',
            'https://lichuan.sp.anjuke.com/zu/p%s', 'https://lengshuijiang.sp.anjuke.com/zu/p%s',
            'https://lianyuan.sp.anjuke.com/zu/p%s', 'https://langzhong.sp.anjuke.com/zu/p%s',
            'https://luxishi.sp.anjuke.com/zu/p%s', 'https://lanxi.sp.anjuke.com/zu/p%s',
            'https://lechang.sp.anjuke.com/zu/p%s', 'https://lianjiangshi.sp.anjuke.com/zu/p%s',
            'https://leizhou.sp.anjuke.com/zu/p%s', 'https://lufengshi.sp.anjuke.com/zu/p%s',
            'https://lianzhou.sp.anjuke.com/zu/p%s', 'https://luoding.sp.anjuke.com/zu/p%s',
            'https://linxiang.sp.anjuke.com/zu/p%s', 'https://longquan.sp.anjuke.com/zu/p%s',
            'https://leping.sp.anjuke.com/zu/p%s', 'https://laoling.sp.anjuke.com/zu/p%s',
            'https://laizhoushi.sp.anjuke.com/zu/p%s', 'https://liuyang.sp.anjuke.com/zu/p%s',
            'https://laohekou.sp.anjuke.com/zu/p%s', 'https://laixi.sp.anjuke.com/zu/p%s',
            'https://mianyang.sp.anjuke.com/zu/p%s', 'https://maoming.sp.anjuke.com/zu/p%s',
            'https://maanshan.sp.anjuke.com/zu/p%s', 'https://mudanjiang.sp.anjuke.com/zu/p%s',
            'https://meishan.sp.anjuke.com/zu/p%s', 'https://meizhou.sp.anjuke.com/zu/p%s',
            'https://minggang.sp.anjuke.com/zu/p%s', 'https://mishan.sp.anjuke.com/zu/p%s',
            'https://meihekou.sp.anjuke.com/zu/p%s', 'https://manzhouli.sp.anjuke.com/zu/p%s',
            'https://mengzhou.sp.anjuke.com/zu/p%s', 'https://macheng.sp.anjuke.com/zu/p%s',
            'https://mianzhu.sp.anjuke.com/zu/p%s', 'https://mingguang.sp.anjuke.com/zu/p%s',
            'https://miluo.sp.anjuke.com/zu/p%s', 'https://nanjing.sp.anjuke.com/zu/p%s',
            'https://nb.sp.anjuke.com/zu/p%s', 'https://nc.sp.anjuke.com/zu/p%s',
            'https://nanning.sp.anjuke.com/zu/p%s', 'https://nantong.sp.anjuke.com/zu/p%s',
            'https://nanchong.sp.anjuke.com/zu/p%s', 'https://nanyang.sp.anjuke.com/zu/p%s',
            'https://ningde.sp.anjuke.com/zu/p%s', 'https://neijiang.sp.anjuke.com/zu/p%s',
            'https://nanping.sp.anjuke.com/zu/p%s', 'https://naqu.sp.anjuke.com/zu/p%s',
            'https://nujiang.sp.anjuke.com/zu/p%s', 'https://nananshi.sp.anjuke.com/zu/p%s',
            'https://ninganshi.sp.anjuke.com/zu/p%s', 'https://ningguo.sp.anjuke.com/zu/p%s',
            'https://nankang.sp.anjuke.com/zu/p%s', 'https://nanxiong.sp.anjuke.com/zu/p%s',
            'https://nehe.sp.anjuke.com/zu/p%s', 'https://nangong.sp.anjuke.com/zu/p%s',
            'https://panzhihua.sp.anjuke.com/zu/p%s', 'https://pingdingsha.sp.anjuke.com/zu/p%s',
            'https://panjin.sp.anjuke.com/zu/p%s', 'https://pingxiang.sp.anjuke.com/zu/p%s',
            'https://puyang.sp.anjuke.com/zu/p%s', 'https://putian.sp.anjuke.com/zu/p%s',
            'https://puer.sp.anjuke.com/zu/p%s', 'https://pingliang.sp.anjuke.com/zu/p%s',
            'https://puning.sp.anjuke.com/zu/p%s', 'https://pulandian.sp.anjuke.com/zu/p%s',
            'https://pingxiangshi.sp.anjuke.com/zu/p%s', 'https://pizhou.sp.anjuke.com/zu/p%s',
            'https://penglaishi.sp.anjuke.com/zu/p%s', 'https://pinghu.sp.anjuke.com/zu/p%s',
            'https://pingdu.sp.anjuke.com/zu/p%s', 'https://pengzhou.sp.anjuke.com/zu/p%s',
            'https://qd.sp.anjuke.com/zu/p%s', 'https://qinhuangdao.sp.anjuke.com/zu/p%s',
            'https://quanzhou.sp.anjuke.com/zu/p%s', 'https://qujing.sp.anjuke.com/zu/p%s',
            'https://qiqihaer.sp.anjuke.com/zu/p%s', 'https://quzhou.sp.anjuke.com/zu/p%s',
            'https://qingyuan.sp.anjuke.com/zu/p%s', 'https://qinzhou.sp.anjuke.com/zu/p%s',
            'https://qingyang.sp.anjuke.com/zu/p%s', 'https://qiandongnan.sp.anjuke.com/zu/p%s',
            'https://qianjiang.sp.anjuke.com/zu/p%s', 'https://qingxu.sp.anjuke.com/zu/p%s',
            'https://qiannan.sp.anjuke.com/zu/p%s', 'https://qitaihe.sp.anjuke.com/zu/p%s',
            'https://qianxinan.sp.anjuke.com/zu/p%s', 'https://qiananshi.sp.anjuke.com/zu/p%s',
            'https://qingzhoushi.sp.anjuke.com/zu/p%s', 'https://qingzhen.sp.anjuke.com/zu/p%s',
            'https://qionghai.sp.anjuke.com/zu/p%s', 'https://qingtongxia.sp.anjuke.com/zu/p%s',
            'https://qinyangshi.sp.anjuke.com/zu/p%s', 'https://qufu.sp.anjuke.com/zu/p%s',
            'https://qionglai.sp.anjuke.com/zu/p%s', 'https://qidong.sp.anjuke.com/zu/p%s',
            'https://rizhao.sp.anjuke.com/zu/p%s', 'https://rikeze.sp.anjuke.com/zu/p%s',
            'https://ruian.sp.anjuke.com/zu/p%s', 'https://ruzhoushi.sp.anjuke.com/zu/p%s',
            'https://renqiushi.sp.anjuke.com/zu/p%s', 'https://ruijin.sp.anjuke.com/zu/p%s',
            'https://rushan.sp.anjuke.com/zu/p%s', 'https://renhuai.sp.anjuke.com/zu/p%s',
            'https://ruichang.sp.anjuke.com/zu/p%s', 'https://ruili.sp.anjuke.com/zu/p%s',
            'https://rugao.sp.anjuke.com/zu/p%s', 'https://rongchengshi.sp.anjuke.com/zu/p%s',
            'https://shanghai.sp.anjuke.com/zu/p%s', 'https://shenzhen.sp.anjuke.com/zu/p%s',
            'https://suzhou.sp.anjuke.com/zu/p%s', 'https://sjz.sp.anjuke.com/zu/p%s',
            'https://sy.sp.anjuke.com/zu/p%s', 'https://sanya.sp.anjuke.com/zu/p%s',
            'https://shaoxing.sp.anjuke.com/zu/p%s', 'https://shantou.sp.anjuke.com/zu/p%s',
            'https://shiyan.sp.anjuke.com/zu/p%s', 'https://sanmenxia.sp.anjuke.com/zu/p%s',
            'https://sanming.sp.anjuke.com/zu/p%s', 'https://shaoguan.sp.anjuke.com/zu/p%s',
            'https://shangqiu.sp.anjuke.com/zu/p%s', 'https://suqian.sp.anjuke.com/zu/p%s',
            'https://suihua.sp.anjuke.com/zu/p%s', 'https://shaoyang.sp.anjuke.com/zu/p%s',
            'https://suining.sp.anjuke.com/zu/p%s', 'https://shangrao.sp.anjuke.com/zu/p%s',
            'https://siping.sp.anjuke.com/zu/p%s', 'https://shihezi.sp.anjuke.com/zu/p%s',
            'https://shunde.sp.anjuke.com/zu/p%s', 'https://suzhoushi.sp.anjuke.com/zu/p%s',
            'https://songyuan.sp.anjuke.com/zu/p%s', 'https://shuyang.sp.anjuke.com/zu/p%s',
            'https://shizuishan.sp.anjuke.com/zu/p%s', 'https://suizhou.sp.anjuke.com/zu/p%s',
            'https://shuozhou.sp.anjuke.com/zu/p%s', 'https://shanwei.sp.anjuke.com/zu/p%s',
            'https://sansha.sp.anjuke.com/zu/p%s', 'https://shangluo.sp.anjuke.com/zu/p%s',
            'https://shannan.sp.anjuke.com/zu/p%s', 'https://shennongjia.sp.anjuke.com/zu/p%s',
            'https://shuangyashan.sp.anjuke.com/zu/p%s', 'https://shishi.sp.anjuke.com/zu/p%s',
            'https://sanheshi.sp.anjuke.com/zu/p%s', 'https://shangzhi.sp.anjuke.com/zu/p%s',
            'https://shouguang.sp.anjuke.com/zu/p%s', 'https://shengzhou.sp.anjuke.com/zu/p%s',
            'https://suifenhe.sp.anjuke.com/zu/p%s', 'https://shifang.sp.anjuke.com/zu/p%s',
            'https://sihui.sp.anjuke.com/zu/p%s', 'https://shaowu.sp.anjuke.com/zu/p%s',
            'https://songzi.sp.anjuke.com/zu/p%s', 'https://shishou.sp.anjuke.com/zu/p%s',
            'https://shaoshan.sp.anjuke.com/zu/p%s', 'https://shenzhou.sp.anjuke.com/zu/p%s',
            'https://shahe.sp.anjuke.com/zu/p%s', 'https://tianjin.sp.anjuke.com/zu/p%s',
            'https://ty.sp.anjuke.com/zu/p%s', 'https://taizhou.sp.anjuke.com/zu/p%s',
            'https://tangshan.sp.anjuke.com/zu/p%s', 'https://taian.sp.anjuke.com/zu/p%s',
            'https://taiz.sp.anjuke.com/zu/p%s', 'https://tieling.sp.anjuke.com/zu/p%s',
            'https://tongliao.sp.anjuke.com/zu/p%s', 'https://tongling.sp.anjuke.com/zu/p%s',
            'https://tianshui.sp.anjuke.com/zu/p%s', 'https://tonghua.sp.anjuke.com/zu/p%s',
            'https://taishan.sp.anjuke.com/zu/p%s', 'https://tongchuan.sp.anjuke.com/zu/p%s',
            'https://tulufan.sp.anjuke.com/zu/p%s', 'https://tianmen.sp.anjuke.com/zu/p%s',
            'https://tumushuke.sp.anjuke.com/zu/p%s', 'https://tongcheng.sp.anjuke.com/zu/p%s',
            'https://tongren.sp.anjuke.com/zu/p%s', 'https://taiwan.sp.anjuke.com/zu/p%s',
            'https://taicang.sp.anjuke.com/zu/p%s', 'https://taixing.sp.anjuke.com/zu/p%s',
            'https://tengzhoushi.sp.anjuke.com/zu/p%s', 'https://taonan.sp.anjuke.com/zu/p%s',
            'https://tieli.sp.anjuke.com/zu/p%s', 'https://tongxiang.sp.anjuke.com/zu/p%s',
            'https://tianchang.sp.anjuke.com/zu/p%s', 'https://wuhan.sp.anjuke.com/zu/p%s',
            'https://wuxi.sp.anjuke.com/zu/p%s', 'https://weihai.sp.anjuke.com/zu/p%s',
            'https://weifang.sp.anjuke.com/zu/p%s', 'https://wulumuqi.sp.anjuke.com/zu/p%s',
            'https://wenzhou.sp.anjuke.com/zu/p%s', 'https://wuhu.sp.anjuke.com/zu/p%s',
            'https://wuzhou.sp.anjuke.com/zu/p%s', 'https://weinan.sp.anjuke.com/zu/p%s',
            'https://wuhai.sp.anjuke.com/zu/p%s', 'https://wenshan.sp.anjuke.com/zu/p%s',
            'https://wuwei.sp.anjuke.com/zu/p%s', 'https://wulanchabu.sp.anjuke.com/zu/p%s',
            'https://wafangdian.sp.anjuke.com/zu/p%s', 'https://wujiaqu.sp.anjuke.com/zu/p%s',
            'https://wuyishan.sp.anjuke.com/zu/p%s', 'https://wuzhong.sp.anjuke.com/zu/p%s',
            'https://wuzhishan.sp.anjuke.com/zu/p%s', 'https://wnelingshi.sp.anjuke.com/zu/p%s',
            'https://wuanshi.sp.anjuke.com/zu/p%s', 'https://wugang.sp.anjuke.com/zu/p%s',
            'https://wuchang.sp.anjuke.com/zu/p%s', 'https://weihui.sp.anjuke.com/zu/p%s',
            'https://wugangshi.sp.anjuke.com/zu/p%s', 'https://wenchang.sp.anjuke.com/zu/p%s',
            'https://wudalianchi.sp.anjuke.com/zu/p%s', 'https://wulanhaote.sp.anjuke.com/zu/p%s',
            'https://wuxue.sp.anjuke.com/zu/p%s', 'https://wanyuan.sp.anjuke.com/zu/p%s',
            'https://wuchuan.sp.anjuke.com/zu/p%s', 'https://wanning.sp.anjuke.com/zu/p%s',
            'https://xa.sp.anjuke.com/zu/p%s', 'https://xm.sp.anjuke.com/zu/p%s', 'https://xuzhou.sp.anjuke.com/zu/p%s',
            'https://xiangtan.sp.anjuke.com/zu/p%s', 'https://xiangyang.sp.anjuke.com/zu/p%s',
            'https://xinxiang.sp.anjuke.com/zu/p%s', 'https://xinyang.sp.anjuke.com/zu/p%s',
            'https://xianyang.sp.anjuke.com/zu/p%s', 'https://xingtai.sp.anjuke.com/zu/p%s',
            'https://xiaogan.sp.anjuke.com/zu/p%s', 'https://xining.sp.anjuke.com/zu/p%s',
            'https://xuchang.sp.anjuke.com/zu/p%s', 'https://xinzhou.sp.anjuke.com/zu/p%s',
            'https://xuancheng.sp.anjuke.com/zu/p%s', 'https://xianning.sp.anjuke.com/zu/p%s',
            'https://xinganmeng.sp.anjuke.com/zu/p%s', 'https://xinyu.sp.anjuke.com/zu/p%s',
            'https://bannan.sp.anjuke.com/zu/p%s', 'https://xianggang.sp.anjuke.com/zu/p%s',
            'https://xiangxi.sp.anjuke.com/zu/p%s', 'https://xiantao.sp.anjuke.com/zu/p%s',
            'https://xilinguole.sp.anjuke.com/zu/p%s', 'https://xintaishi.sp.anjuke.com/zu/p%s',
            'https://xinle.sp.anjuke.com/zu/p%s', 'https://xiangxiang.sp.anjuke.com/zu/p%s',
            'https://xilinhaote.sp.anjuke.com/zu/p%s', 'https://xinji.sp.anjuke.com/zu/p%s',
            'https://xinmin.sp.anjuke.com/zu/p%s', 'https://xinghua.sp.anjuke.com/zu/p%s',
            'https://xingping.sp.anjuke.com/zu/p%s', 'https://xingyi.sp.anjuke.com/zu/p%s',
            'https://xuanwei.sp.anjuke.com/zu/p%s', 'https://xingning.sp.anjuke.com/zu/p%s',
            'https://xiangcheng.sp.anjuke.com/zu/p%s', 'https://xinyi.sp.anjuke.com/zu/p%s',
            'https://xiaoyi.sp.anjuke.com/zu/p%s', 'https://xingcheng.sp.anjuke.com/zu/p%s',
            'https://xinyishi.sp.anjuke.com/zu/p%s', 'https://xingyang.sp.anjuke.com/zu/p%s',
            'https://xinzheng.sp.anjuke.com/zu/p%s', 'https://xinmi.sp.anjuke.com/zu/p%s',
            'https://yt.sp.anjuke.com/zu/p%s', 'https://yangzhou.sp.anjuke.com/zu/p%s',
            'https://yichang.sp.anjuke.com/zu/p%s', 'https://yinchuan.sp.anjuke.com/zu/p%s',
            'https://yangjiang.sp.anjuke.com/zu/p%s', 'https://yongzhou.sp.anjuke.com/zu/p%s',
            'https://yulinshi.sp.anjuke.com/zu/p%s', 'https://yancheng.sp.anjuke.com/zu/p%s',
            'https://yueyang.sp.anjuke.com/zu/p%s', 'https://yuncheng.sp.anjuke.com/zu/p%s',
            'https://yichun.sp.anjuke.com/zu/p%s', 'https://yingkou.sp.anjuke.com/zu/p%s',
            'https://yulin.sp.anjuke.com/zu/p%s', 'https://yibin.sp.anjuke.com/zu/p%s',
            'https://yiyang.sp.anjuke.com/zu/p%s', 'https://yiwu.sp.anjuke.com/zu/p%s',
            'https://yuxi.sp.anjuke.com/zu/p%s', 'https://yili.sp.anjuke.com/zu/p%s',
            'https://yangquan.sp.anjuke.com/zu/p%s', 'https://yanan.sp.anjuke.com/zu/p%s',
            'https://yingtan.sp.anjuke.com/zu/p%s', 'https://yanbian.sp.anjuke.com/zu/p%s',
            'https://yufu.sp.anjuke.com/zu/p%s', 'https://yaan.sp.anjuke.com/zu/p%s',
            'https://yangchun.sp.anjuke.com/zu/p%s', 'https://yanling.sp.anjuke.com/zu/p%s',
            'https://yichunshi.sp.anjuke.com/zu/p%s', 'https://yushu.sp.anjuke.com/zu/p%s',
            'https://yueqing.sp.anjuke.com/zu/p%s', 'https://yuzhou.sp.anjuke.com/zu/p%s',
            'https://yongxin.sp.anjuke.com/zu/p%s', 'https://yongkangshi.sp.anjuke.com/zu/p%s',
            'https://yushushi.sp.anjuke.com/zu/p%s', 'https://yongan.sp.anjuke.com/zu/p%s',
            'https://yidou.sp.anjuke.com/zu/p%s', 'https://yizheng.sp.anjuke.com/zu/p%s',
            'https://yanji.sp.anjuke.com/zu/p%s', 'https://yangzhong.sp.anjuke.com/zu/p%s',
            'https://yakeshi.sp.anjuke.com/zu/p%s', 'https://yining.sp.anjuke.com/zu/p%s',
            'https://yongji.sp.anjuke.com/zu/p%s', 'https://yingchengshi.sp.anjuke.com/zu/p%s',
            'https://yizhou.sp.anjuke.com/zu/p%s', 'https://yingde.sp.anjuke.com/zu/p%s',
            'https://yumen.sp.anjuke.com/zu/p%s', 'https://yucheng.sp.anjuke.com/zu/p%s',
            'https://yuyao.sp.anjuke.com/zu/p%s', 'https://yanshishi.sp.anjuke.com/zu/p%s',
            'https://yongcheng.sp.anjuke.com/zu/p%s', 'https://yixing.sp.anjuke.com/zu/p%s',
            'https://yicheng.sp.anjuke.com/zu/p%s', 'https://yuanjiang.sp.anjuke.com/zu/p%s',
            'https://zhengzhou.sp.anjuke.com/zu/p%s', 'https://zh.sp.anjuke.com/zu/p%s',
            'https://zs.sp.anjuke.com/zu/p%s', 'https://zhenjiang.sp.anjuke.com/zu/p%s',
            'https://zibo.sp.anjuke.com/zu/p%s', 'https://zhangjiakou.sp.anjuke.com/zu/p%s',
            'https://zhuzhou.sp.anjuke.com/zu/p%s', 'https://zhangzhou.sp.anjuke.com/zu/p%s',
            'https://zhanjiang.sp.anjuke.com/zu/p%s', 'https://zhaoqing.sp.anjuke.com/zu/p%s',
            'https://zaozhuang.sp.anjuke.com/zu/p%s', 'https://zhoushan.sp.anjuke.com/zu/p%s',
            'https://zunyi.sp.anjuke.com/zu/p%s', 'https://zhumadian.sp.anjuke.com/zu/p%s',
            'https://zigong.sp.anjuke.com/zu/p%s', 'https://ziyang.sp.anjuke.com/zu/p%s',
            'https://zhoukou.sp.anjuke.com/zu/p%s', 'https://zhangqiu.sp.anjuke.com/zu/p%s',
            'https://zhangjiajie.sp.anjuke.com/zu/p%s', 'https://zhucheng.sp.anjuke.com/zu/p%s',
            'https://zhuanghe.sp.anjuke.com/zu/p%s', 'https://zhengding.sp.anjuke.com/zu/p%s',
            'https://zhangbei.sp.anjuke.com/zu/p%s', 'https://zhangye.sp.anjuke.com/zu/p%s',
            'https://zhaotong.sp.anjuke.com/zu/p%s', 'https://weizhong.sp.anjuke.com/zu/p%s',
            'https://zhaoxian.sp.anjuke.com/zu/p%s', 'https://zouchengshi.sp.anjuke.com/zu/p%s',
            'https://zunhua.sp.anjuke.com/zu/p%s', 'https://zhaodong.sp.anjuke.com/zu/p%s',
            'https://zhangjiagang.sp.anjuke.com/zu/p%s', 'https://zhijiang.sp.anjuke.com/zu/p%s',
            'https://zhaoyuanshi.sp.anjuke.com/zu/p%s', 'https://zhongxiang.sp.anjuke.com/zu/p%s',
            'https://zixing.sp.anjuke.com/zu/p%s', 'https://zhangshu.sp.anjuke.com/zu/p%s',
            'https://zhalandun.sp.anjuke.com/zu/p%s', 'https://zhuji.sp.anjuke.com/zu/p%s',
            'https://zhuozhoushi.sp.anjuke.com/zu/p%s', 'https://zaoyangshi.sp.anjuke.com/zu/p%s',
            'https://zhangping.sp.anjuke.com/zu/p%s', 'https://chengdu.sp.anjuke.com/zu/p%s',
            'https://chengdu.sp.anjuke.com/zu/p%s', 'https://chengdu.sp.anjuke.com/zu/p%s',
            'https://nanjing.sp.anjuke.com/zu/p%s', 'https://hangzhou.sp.anjuke.com/zu/p%s',
            'https://hangzhou.sp.anjuke.com/zu/p%s', 'https://hangzhou.sp.anjuke.com/zu/p%s',
            'https://hangzhou.sp.anjuke.com/zu/p%s', 'https://chongqing.sp.anjuke.com/zu/p%s',
            'https://chongqing.sp.anjuke.com/zu/p%s', 'https://chongqing.sp.anjuke.com/zu/p%s',
            'https://chongqing.sp.anjuke.com/zu/p%s', 'https://chongqing.sp.anjuke.com/zu/p%s',
            'https://chongqing.sp.anjuke.com/zu/p%s', 'https://chongqing.sp.anjuke.com/zu/p%s',
            'https://chongqing.sp.anjuke.com/zu/p%s', 'https://chongqing.sp.anjuke.com/zu/p%s',
            'https://chongqing.sp.anjuke.com/zu/p%s', 'https://chongqing.sp.anjuke.com/zu/p%s',
            'https://dalian.sp.anjuke.com/zu/p%s', 'https://jinan.sp.anjuke.com/zu/p%s',
            'https://jinan.sp.anjuke.com/zu/p%s', 'https://jinan.sp.anjuke.com/zu/p%s',
            'https://zhengzhou.sp.anjuke.com/zu/p%s', 'https://zhengzhou.sp.anjuke.com/zu/p%s',
            'https://cs.sp.anjuke.com/zu/p%s', 'https://sjz.sp.anjuke.com/zu/p%s', 'https://sjz.sp.anjuke.com/zu/p%s',
            'https://sjz.sp.anjuke.com/zu/p%s', 'https://qd.sp.anjuke.com/zu/p%s', 'https://qd.sp.anjuke.com/zu/p%s',
            'https://xa.sp.anjuke.com/zu/p%s', 'https://xa.sp.anjuke.com/zu/p%s', 'https://xa.sp.anjuke.com/zu/p%s',
            'https://nb.sp.anjuke.com/zu/p%s', 'https://nb.sp.anjuke.com/zu/p%s', 'https://hf.sp.anjuke.com/zu/p%s',
            'https://hf.sp.anjuke.com/zu/p%s', 'https://hf.sp.anjuke.com/zu/p%s', 'https://hf.sp.anjuke.com/zu/p%s',
            'https://fz.sp.anjuke.com/zu/p%s', 'https://fz.sp.anjuke.com/zu/p%s', 'https://fz.sp.anjuke.com/zu/p%s',
            'https://km.sp.anjuke.com/zu/p%s', 'https://km.sp.anjuke.com/zu/p%s', 'https://gy.sp.anjuke.com/zu/p%s',
            'https://sy.sp.anjuke.com/zu/p%s', 'https://sy.sp.anjuke.com/zu/p%s', 'https://nc.sp.anjuke.com/zu/p%s',
            'https://nc.sp.anjuke.com/zu/p%s', 'https://cz.sp.anjuke.com/zu/p%s', 'https://jx.sp.anjuke.com/zu/p%s',
            'https://yt.sp.anjuke.com/zu/p%s', 'https://yt.sp.anjuke.com/zu/p%s', 'https://yt.sp.anjuke.com/zu/p%s',
            'https://haikou.sp.anjuke.com/zu/p%s', 'https://haikou.sp.anjuke.com/zu/p%s',
            'https://haikou.sp.anjuke.com/zu/p%s', 'https://haikou.sp.anjuke.com/zu/p%s',
            'https://haikou.sp.anjuke.com/zu/p%s', 'https://haikou.sp.anjuke.com/zu/p%s',
            'https://haikou.sp.anjuke.com/zu/p%s', 'https://cc.sp.anjuke.com/zu/p%s',
            'https://sanya.sp.anjuke.com/zu/p%s', 'https://sanya.sp.anjuke.com/zu/p%s',
            'https://sanya.sp.anjuke.com/zu/p%s', 'https://sanya.sp.anjuke.com/zu/p%s',
            'https://huizhou.sp.anjuke.com/zu/p%s', 'https://huizhou.sp.anjuke.com/zu/p%s',
            'https://huizhou.sp.anjuke.com/zu/p%s', 'https://jilin.sp.anjuke.com/zu/p%s',
            'https://lanzhou.sp.anjuke.com/zu/p%s', 'https://lanzhou.sp.anjuke.com/zu/p%s',
            'https://langfang.sp.anjuke.com/zu/p%s', 'https://luoyang.sp.anjuke.com/zu/p%s',
            'https://luoyang.sp.anjuke.com/zu/p%s', 'https://luoyang.sp.anjuke.com/zu/p%s',
            'https://luoyang.sp.anjuke.com/zu/p%s', 'https://luoyang.sp.anjuke.com/zu/p%s',
            'https://nanning.sp.anjuke.com/zu/p%s', 'https://nanning.sp.anjuke.com/zu/p%s',
            'https://nantong.sp.anjuke.com/zu/p%s', 'https://nantong.sp.anjuke.com/zu/p%s',
            'https://nantong.sp.anjuke.com/zu/p%s', 'https://quanzhou.sp.anjuke.com/zu/p%s',
            'https://quanzhou.sp.anjuke.com/zu/p%s', 'https://quanzhou.sp.anjuke.com/zu/p%s',
            'https://quanzhou.sp.anjuke.com/zu/p%s', 'https://shaoxing.sp.anjuke.com/zu/p%s',
            'https://taizhou.sp.anjuke.com/zu/p%s', 'https://tangshan.sp.anjuke.com/zu/p%s',
            'https://tangshan.sp.anjuke.com/zu/p%s', 'https://tangshan.sp.anjuke.com/zu/p%s',
            'https://tangshan.sp.anjuke.com/zu/p%s', 'https://tangshan.sp.anjuke.com/zu/p%s',
            'https://weifang.sp.anjuke.com/zu/p%s', 'https://weifang.sp.anjuke.com/zu/p%s',
            'https://weifang.sp.anjuke.com/zu/p%s', 'https://weifang.sp.anjuke.com/zu/p%s',
            'https://weifang.sp.anjuke.com/zu/p%s', 'https://xuzhou.sp.anjuke.com/zu/p%s',
            'https://xuzhou.sp.anjuke.com/zu/p%s', 'https://xuzhou.sp.anjuke.com/zu/p%s',
            'https://yangzhou.sp.anjuke.com/zu/p%s', 'https://yangzhou.sp.anjuke.com/zu/p%s',
            'https://yangzhou.sp.anjuke.com/zu/p%s', 'https://yangzhou.sp.anjuke.com/zu/p%s',
            'https://yichang.sp.anjuke.com/zu/p%s', 'https://yichang.sp.anjuke.com/zu/p%s',
            'https://yichang.sp.anjuke.com/zu/p%s', 'https://zhenjiang.sp.anjuke.com/zu/p%s',
            'https://zhenjiang.sp.anjuke.com/zu/p%s', 'https://binzhou.sp.anjuke.com/zu/p%s',
            'https://dongying.sp.anjuke.com/zu/p%s', 'https://taiz.sp.anjuke.com/zu/p%s',
            'https://daqing.sp.anjuke.com/zu/p%s', 'https://lianyungang.sp.anjuke.com/zu/p%s',
            'https://huzhou.sp.anjuke.com/zu/p%s', 'https://huzhou.sp.anjuke.com/zu/p%s',
            'https://yancheng.sp.anjuke.com/zu/p%s', 'https://maanshan.sp.anjuke.com/zu/p%s',
            'https://xuancheng.sp.anjuke.com/zu/p%s', 'https://bazhong.sp.anjuke.com/zu/p%s']


def get_all_urls():
    urls = []
    while area_url:
        url = area_url.pop(0)
        page_num = [i for i in range(1, 58)]
        random.shuffle(page_num)
        urls += [url % i for i in page_num]
    return urls


# time.sleep(10000)
class AnJuKe(threading.Thread):
    MONGODB_HOST = "127.0.0.1"
    MONGODB_PORT = 27017

    def __init__(self):
        super(AnJuKe, self).__init__()
        self.REDIS_KEY = 'anjuke_27'
        self.headers = None
        self.r = redis.StrictRedis(host='127.0.0.1', port=6379)
        conn = pymongo.MongoClient(host=self.MONGODB_HOST, port=self.MONGODB_PORT)
        self.db = conn.anjuke

    def _save_urls_to_redis(self):
        """

        :return:
        """

        if not self.r.exists(self.REDIS_KEY):
            urls = get_all_urls()
            print("url写入中...")
            for url in urls:
                self.r.sadd(self.REDIS_KEY, url)
            print("---------------url写入完成----------------------")

    def _get(self, url, headers):
        """

        :param url:
        :param session:
        :param headers:
        :return:
        """
        # ip = random.choice()
        h = {}
        # proxy = {"http": "http://{}".format(ip)}
        # print(u"使用代理：{}".format(proxy))
        if headers:
            for k, v in headers.items():
                h[k] = v
        if self.headers:
            for k, v in self.headers.items():
                h[k] = v
        try:
            resp = requests.get(url, headers=h, allow_redirects=False)
            if resp.ok:
                return resp
        except Exception as e:
            print(u"{}请求失败:{}".format(url, e.args))
            # PROXIES.pop(ip)
            # if not PROXIES:
            #     print(u"代理全部失效，程序退出")
            #     sys.exit()
            # time.sleep(10)

    def _paras_list_page_item(self, resp):
        """

        :param resp:
        :return:
        """
        if resp:
            html = etree.HTML(resp.text)
            return html.xpath("//div[@id='list-content']/div[@class='list-item']")
        else:
            print(u"--------列表页返回错误----------{}".format(resp.text))

    def _save_data(self, data):
        """
        数据保存
        :param data:
        :return:
        """
        temp = self.db.anjuke_SP
        res = temp.insert(data)
        print("data save to MONGODB:{}".format(res))

    def _paras_detail_page(self, items):
        """
        
        :return:
        """
        for item in items:
            time.sleep(random.randint(1, 3))
            data = {}
            try:
                floor = item.xpath(".//dl/dd/span[2]/text()")[0]
            except Exception as e:
                print(u"--------------------------商铺楼层解析错误:%s-----------------------" % e.args)
                continue
            data["crawler_date"] = date
            data["data_from"] = u"安居客"
            page_url = item.xpath("./@link")[0]
            if "1" in floor or u"一" in floor:
                # 字段:抓取时间.数据来源(安居客/中原地产)/网页url/具体地址/经纬度/租金/租期/面积
                # item.xpath("./@link")
                # page_url = "https://hf.sp.anjuke.com/zu/72941389/?pt=1"
                data["url"] = page_url  # 详情url
                resp_detail = self._get(url=page_url, headers=random.choice(headers))
                if not resp_detail:
                    continue
                html = etree.HTML(resp_detail.text)
                try:
                    lat = re.search(pattern='lat: "(.+)"', string=resp_detail.text)
                    lng = re.search(pattern='lng: "(.+)"', string=resp_detail.text)
                    if lat and lng:
                        data["lng"] = lng.group(1)  # 经度
                        data["lat"] = lat.group(1)  # 纬度
                    else:
                        data["lng"] = ""
                        data["lat"] = ""
                    data["rent"] = html.xpath(
                        "//div[@id='fy_info']/ul[@class='litem']/li[1]/span[@class='desc']/text()")[0].strip()  # 租金

                    data["desc"] = html.xpath(
                        "//div[@id='fy_info']/ul[@class='litem']/li[3]/span[@class='desc']/text()")[0].strip()  # 租期

                    data["size"] = html.xpath(
                        "//div[@id='fy_info']/ul[@class='ritem']/li[1]/span[@class='desc']/text()")[0].strip()  # 面积

                    data["address"] = html.xpath("//div[@id='fy_info']//span[@class='desc addresscommu']/text()")[0][
                                      1:-1].strip().replace(" ", "")  # 地址

                    # self._save_data(data)
                    print(data)
                except Exception as e:
                    print(u"--------数据获取失败{}:{} ---------".format(e.args, page_url))
                    continue
            else:
                print(u"-------------------------floor info:%s-------------------------" % floor)
                if u'其他' in floor or u'商铺/门面/店面' in floor:
                    break
                else:
                    continue

    def run(self):
        lock.acquire()
        self._save_urls_to_redis()
        lock.release()
        while self.r.exists(self.REDIS_KEY):
            url = self.r.spop(self.REDIS_KEY).decode('utf-8')
            print(u"-----------------  开始爬取url:%s  ------------------------" % url)
            time.sleep(random.randint(1, 3))
            resp = self._get(url=url, headers=random.choice(headers))
            if not resp:
                continue
            if u"没有结果，请换个搜索词或试试筛选吧!" in resp.text:
                url1 = url.split('zu/p')
                index = int(url1[-1])
                try:
                    for i in range(index, 59):
                        self.r.srem(self.REDIS_KEY, url1[0] + 'zu/p{}'.format(str(i)))
                        # print(url1[0] + 'zu/p{}'.format(str(i)))
                except:
                    continue
                continue
            items = self._paras_list_page_item(resp)
            self._paras_detail_page(items)


if __name__ == '__main__':
    task_list = []
    for i in range(1):
        task_list.append(AnJuKe())
    for task in task_list:
        task.start()
    for task in task_list:
        task.join()
