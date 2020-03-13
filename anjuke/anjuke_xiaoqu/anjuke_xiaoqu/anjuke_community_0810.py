# coding=utf-8
import datetime
import random
import sys
import time

import fake_useragent
import pymongo
import re
import redis
import requests
from lxml import etree

MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017

conn = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
db = conn.shixin
db.authenticate("chean", "scc57295729")
temp = db.xiaoqu
r = redis.StrictRedis(host='127.0.0.1', port=6388, password="admin")
REDIS_KEY = "anjuke_xiaoqu"
main_url = ['https://beijing.anjuke.com/community/p%s/', 'https://tianjin.anjuke.com/community/p%s/',
            'https://dalian.anjuke.com/community/p%s/', 'https://sjz.anjuke.com/community/p%s/',
            'https://heb.anjuke.com/community/p%s/', 'https://sy.anjuke.com/community/p%s/',
            'https://ty.anjuke.com/community/p%s/', 'https://cc.anjuke.com/community/p%s/',
            'https://weihai.anjuke.com/community/p%s/', 'https://weifang.anjuke.com/community/p%s/',
            'https://huhehaote.anjuke.com/community/p%s/', 'https://baotou.anjuke.com/community/p%s/',
            'https://qinhuangdao.anjuke.com/community/p%s/', 'https://yt.anjuke.com/community/p%s/',
            'https://baoding.anjuke.com/community/p%s/', 'https://shanghai.anjuke.com/community/p%s/',
            'https://hangzhou.anjuke.com/community/p%s/', 'https://suzhou.anjuke.com/community/p%s/',
            'https://nanjing.anjuke.com/community/p%s/', 'https://wuxi.anjuke.com/community/p%s/',
            'https://jinan.anjuke.com/community/p%s/', 'https://qd.anjuke.com/community/p%s/',
            'https://ks.anjuke.com/community/p%s/', 'https://nb.anjuke.com/community/p%s/',
            'https://nc.anjuke.com/community/p%s/', 'https://fz.anjuke.com/community/p%s/',
            'https://hf.anjuke.com/community/p%s/', 'https://xuzhou.anjuke.com/community/p%s/',
            'https://zibo.anjuke.com/community/p%s/', 'https://nantong.anjuke.com/community/p%s/',
            'https://cz.anjuke.com/community/p%s/', 'https://huzhou.anjuke.com/community/p%s/',
            'https://shenzhen.anjuke.com/community/p%s/', 'https://guangzhou.anjuke.com/community/p%s/',
            'https://foshan.anjuke.com/community/p%s/', 'https://cs.anjuke.com/community/p%s/',
            'https://sanya.anjuke.com/community/p%s/', 'https://huizhou.anjuke.com/community/p%s/',
            'https://dg.anjuke.com/community/p%s/', 'https://haikou.anjuke.com/community/p%s/',
            'https://zh.anjuke.com/community/p%s/', 'https://zs.anjuke.com/community/p%s/',
            'https://xm.anjuke.com/community/p%s/', 'https://nanning.anjuke.com/community/p%s/',
            'https://quanzhou.anjuke.com/community/p%s/', 'https://liuzhou.anjuke.com/community/p%s/',
            'https://chengdu.anjuke.com/community/p%s/', 'https://chongqing.anjuke.com/community/p%s/',
            'https://wuhan.anjuke.com/community/p%s/', 'https://zhengzhou.anjuke.com/community/p%s/',
            'https://xa.anjuke.com/community/p%s/', 'https://km.anjuke.com/community/p%s/',
            'https://gy.anjuke.com/community/p%s/', 'https://lanzhou.anjuke.com/community/p%s/',
            'https://luoyang.anjuke.com/community/p%s/']
start_url = ['https://beijing.anjuke.com/community/?from=navigation',
             'https://tianjin.anjuke.com/community/?from=navigation',
             'https://dalian.anjuke.com/community/?from=navigation',
             'https://sjz.anjuke.com/community/?from=navigation',
             'https://heb.anjuke.com/community/?from=navigation', 'https://sy.anjuke.com/community/?from=navigation',
             'https://ty.anjuke.com/community/?from=navigation', 'https://cc.anjuke.com/community/?from=navigation',
             'https://weihai.anjuke.com/community/?from=navigation',
             'https://weifang.anjuke.com/community/?from=navigation',
             'https://huhehaote.anjuke.com/community/?from=navigation',
             'https://baotou.anjuke.com/community/?from=navigation',
             'https://qinhuangdao.anjuke.com/community/?from=navigation',
             'https://yt.anjuke.com/community/?from=navigation',
             'https://baoding.anjuke.com/community/?from=navigation',
             'https://shanghai.anjuke.com/community/?from=navigation',
             'https://hangzhou.anjuke.com/community/?from=navigation',
             'https://suzhou.anjuke.com/community/?from=navigation',
             'https://nanjing.anjuke.com/community/?from=navigation',
             'https://wuxi.anjuke.com/community/?from=navigation',
             'https://jinan.anjuke.com/community/?from=navigation', 'https://qd.anjuke.com/community/?from=navigation',
             'https://ks.anjuke.com/community/?from=navigation', 'https://nb.anjuke.com/community/?from=navigation',
             'https://nc.anjuke.com/community/?from=navigation', 'https://fz.anjuke.com/community/?from=navigation',
             'https://hf.anjuke.com/community/?from=navigation', 'https://xuzhou.anjuke.com/community/?from=navigation',
             'https://zibo.anjuke.com/community/?from=navigation',
             'https://nantong.anjuke.com/community/?from=navigation',
             'https://cz.anjuke.com/community/?from=navigation', 'https://huzhou.anjuke.com/community/?from=navigation',
             'https://shenzhen.anjuke.com/community/?from=navigation',
             'https://guangzhou.anjuke.com/community/?from=navigation',
             'https://foshan.anjuke.com/community/?from=navigation', 'https://cs.anjuke.com/community/?from=navigation',
             'https://sanya.anjuke.com/community/?from=navigation',
             'https://huizhou.anjuke.com/community/?from=navigation',
             'https://dg.anjuke.com/community/?from=navigation', 'https://haikou.anjuke.com/community/?from=navigation',
             'https://zh.anjuke.com/community/?from=navigation', 'https://zs.anjuke.com/community/?from=navigation',
             'https://xm.anjuke.com/community/?from=navigation',
             'https://nanning.anjuke.com/community/?from=navigation',
             'https://quanzhou.anjuke.com/community/?from=navigation',
             'https://liuzhou.anjuke.com/community/?from=navigation',
             'https://chengdu.anjuke.com/community/?from=navigation',
             'https://chongqing.anjuke.com/community/?from=navigation',
             'https://wuhan.anjuke.com/community/?from=navigation',
             'https://zhengzhou.anjuke.com/community/?from=navigation',
             'https://xa.anjuke.com/community/?from=navigation', 'https://km.anjuke.com/community/?from=navigation',
             'https://gy.anjuke.com/community/?from=navigation',
             'https://lanzhou.anjuke.com/community/?from=navigation',
             'https://luoyang.anjuke.com/community/?from=navigation']


class AnJuKeCommunity():

    def __init__(self):
        self.proxies = []
        self.proxy = {}
        pass

    def get_proxy(self):
        if not self.proxies:
            self.delay()
            resp = requests.get(
                "http://http.tiqu.alicdns.com/getip3?num=0&type=2&pro=0&city=0&yys=0&port=1&pack=58416&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4").json()
            if isinstance(resp, dict) and resp.get("code") != 0:
                # self.logger.info("ProxyError:{}".format(resp.get("msg")))
                print "ProxyError:"
                print resp.get("msg")
                sys.exit()
            self.proxies = [{"https": "https://" + str(proxy.get("ip")) + ":" + str(proxy.get("port"))} for proxy in
                            resp.get("data")]
        print "ips:", len(self.proxies)
        return random.choice(self.proxies)

    @staticmethod
    def delay():
        time.sleep(random.randint(3, 5))

    def _save_urls_to_redis(self):
        """

        :return:
        """
        if not r.exists(REDIS_KEY):
            print("url写入中...")
            for i in start_url:
                r.sadd(REDIS_KEY, i)
            print("---------------url写入完成----------------------")

    def _ban_validate(self, resp):
        """

        :return:
        """
        if u"访问验证-安居客" in resp:
            return True
        else:
            return False

    def _check_next_page(self, content):
        """

        :param resp:
        :return:
        """
        pattern = u'<a href="(.+)" class="aNxt">'
        res = re.findall(pattern, content)
        if res:
            return res[0]
        else:
            return False

    def _page_downloader(self, url, headers, allow_redirects=False, cookies={}):
        """

        :param url:
        :param headers:
        :param cookies:
        :return:
        """
        global cnt
        cnt += 1
        print cnt
        self.delay()
        self.proxy = self.get_proxy()
        print u"使用代理", self.proxy
        page = requests.get(url=url, headers=headers, cookies=cookies, allow_redirects=allow_redirects,
                            proxies=self.proxy, timeout=10)
        while page.status_code == 302 or self._ban_validate(page.text):
            self.proxies.remove(self.proxy)
            print "bans,change ip"
            self.proxy = self.get_proxy()
            page = requests.get(url=url, headers=headers, cookies=cookies, allow_redirects=allow_redirects,
                                proxies=self.proxy, timeout=10)
        return page

    def _list_page_paras(self, resp):
        """

        :param resp:
        :return:
        """
        html = etree.HTML(resp)
        return html.xpath("//div[@class='li-info']/h3/a/@href")

    def _save_data(self, data):
        """

        :param data:
        :return:
        """

        flag = temp.find_one({"src": data["src"]})
        if flag:
            res = temp.update_one(
                {'src': data["src"]},
                {'$set': data
                 }
            )  # todo
            print("[*]data update to MONGODB:{}".format(res))
        else:
            res = temp.insert(data)
            print("[√]data save to MONGODB:{}".format(res))
        # print data

    def _detail_paras(self, resp):
        """

        :param resp:
        :return:
        """
        data = {}
        detail_html = etree.HTML(resp)
        data["community_name"] = detail_html.xpath("//div[@class='comm-title']/h1/text()")[0].strip()
        result = re.search('"comm_midprice":"(.+)","area_midprice"', resp)
        if result:
            data["community_price"] = result.group(1) + u"元/m²"
        else:
            data["community_price"] = ""
        community_house_number = detail_html.xpath("//div[@id='basic-infos-box']//dd[@class='other-dd'][2]/text()")[0]
        data["community_house_number"] = "" if community_house_number == u"暂无数据" else community_house_number
        lat = re.search(pattern='lat : "(.+)",', string=resp)
        lng = re.search(pattern='lng : "(.+)"', string=resp)
        if lat and lng:
            data["lng"] = lng.group(1)  # 经度
            data["lat"] = lat.group(1)  # 纬度
        else:
            data["lng"] = ""
            data["lat"] = ""
        data["community_rent"] = ""
        data["from"] = "安居客"
        return data

    def main(self):
        start_time = datetime.datetime.now()
        ua = fake_useragent.UserAgent()
        headers = {"User-Agent": ua.random}
        self._save_urls_to_redis()
        while r.exists(REDIS_KEY):
            url = r.spop(REDIS_KEY).decode('utf-8')
            while url:
                try:
                    resp = self._page_downloader(url=url, headers=headers)
                except Exception as e:
                    print e
                    self.proxy = self.get_proxy()
                    continue
                urls = self._list_page_paras(resp.text)
                print url
                for detail_url in urls:
                    try:
                        detail_resp = self._page_downloader(url=detail_url, headers=headers)
                    except Exception as e:
                        print e
                        self.proxy = self.get_proxy()
                        continue
                    final_data = self._detail_paras(detail_resp.text)
                    final_data["src"] = detail_url
                    self._save_data(final_data)
                url = self._check_next_page(resp.text)
            print "done,next url"
            if (datetime.datetime.now() - start_time).seconds > 3600:
                print "timeout"
                sys.exit()


if __name__ == '__main__':
    cnt = 0
    t = AnJuKeCommunity()
    t.main()
