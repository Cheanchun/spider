import queue
import random
import re
import sys
import time

import redis
import requests
from lxml import etree

r = redis.Redis(host="47.105.54.129", port=6388, db=0, password="admin")

REDIS_KEY = "proxy"
MAX_SCORE = 100
MIN_SCORE = 0


def ip_pool():
    for i in range(6):
        proxy_url = "http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy?spiderId=bcf4b1d29b374d10a6a1d14fd08e516f&returnType=1&count=1"
        resp = requests.get(url=proxy_url)
        ip_list = [i for i in resp.text.split("\r\n") if i]
        # print(ip_list)
        for i in ip_list:
            r.lpush("ips", i)
            ips.append(i)
            time.sleep(3)
    # print(ips)


'''

'''

cookies = [{
    'sessid': '19FCF1EE-7F25-F8AB-DAB1-A09605CE28C4', 'new_session': '1',
    'lps': 'http%3A%2F%2Fchengdu.anjuke.com%2Fsale%2Fwuhou%2F%7C',
    'aQQ_ajkguid': '94DB6C3F-C884-FD0E-306D-55F97A8218EC', 'ctid': '15', 'twe': '2',
    '58tj_uuid': '210fc2e2-f395-4616-b8c2-7ad382b7713b', 'init_refer': '', 'new_uv': '1', '_gat': '1',
    '_ga': 'GA1.2.1769617714.1550815291', '_gid': 'GA1.2.344453553.1550815291'},
    {'lps': 'http%3A%2F%2Fchengdu.anjuke.com%2Fsale%2Fwuhou%2F%7C', 'new_session': '0',
     'sessid': 'A2546E45-FC2C-C538-990D-A85A24750660', '__xsptplusUT_8': '1',
     'aQQ_ajkguid': '149C812A-32A7-7CAD-6A7D-B376A17FA866', 'ctid': '15', 'twe': '2',
     '58tj_uuid': '06949400-fc6a-4879-a4bb-687ad388d78a', 'init_refer': '', 'new_uv': '1',
     '__xsptplus8': '8.1.1550899935.1550899935.1%234%7C%7C%7C%7C%7C%23%23YJ6oP0bWUS6UpXyVRK1XfBow34DMVsyW%23',
     'als': '0', '_gat': '1', '_ga': 'GA1.2.781398080.1550899936', '_gid': 'GA1.2.753501075.1550899936'},
    {'sessid': '6911B3A3-F478-2208-46BA-5CF970ED8685', 'new_session': '1',
     'lps': 'http%3A%2F%2Fchengdu.anjuke.com%2Fsale%2Fwuhou%2F%7C', '__xsptplusUT_8': '1',
     'aQQ_ajkguid': 'D2A35EEE-E4DC-F1C4-7BA7-5CF85191AB63', 'ctid': '15', 'twe': '2',
     '58tj_uuid': '3fa07a91-a8f8-4107-9c6f-a758399f11f6', 'init_refer': '', 'new_uv': '1',
     '__xsptplus8': '8.1.1550905686.1550905686.1%234%7C%7C%7C%7C%7C%23%23rFKaTTMwllSp-BoJkqW__K8D5ziP2uj7%23',
     '_gat': '1', '_ga': 'GA1.2.1874007311.1550905687', '_gid': 'GA1.2.493945315.1550905687', 'als': '0'},
]
session = requests.Session()
timestamp = time.time()

areas = ["tianfuxinqu", "wuhou", "gaoxin", "qingyang", "jinjiang", "jinniu", "chenghua", "wenjiang", "longquanyi",
         "shuangliu",
         "dujiangyan", "piduqu", "xindu", "qingbaijiangqu", "xinjinxian", "jintangxian", "pengzhoushi",
         "chongzhoushi", "dayixian", "qionglaishi", "cdpujiangxian", "jianyangsh", "pengshan", "renshou"]
area = "tianfuxinqu"
base_url = "https://chengdu.anjuke.com/community/" + area + "/p1/"
url = "https://chengdu.anjuke.com/community/?from=navigation"
num = r.lpop("anjuke_index")
urls = queue.Queue()
ips = queue.Queue()
headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Safari/537.36",
}


def demo():
    '''
    https://chengdu.anjuke.com/community/?from=navigation
    https://chengdu.anjuke.com/community/gaoxinxiqu/
    '''
    url = "https://chengdu.anjuke.com/community/gaoxinxiqu/"
    proxies = r.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
    for ip in proxies:
        ips.append(ip)

    try:
        session.proxies = {"https": ips.pop()}
    except:
        proxies = r.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        for ip in proxies:
            ips.append(ip)

    resp = session.get(url=url)
    while resp and resp.status_code != 200:
        time.sleep(0.5)
        session.proxies = {"https": ips.pop()}
        resp = session.get(url=url, headers=headers, cookies=random.choice(cookies),
                           allow_redirects=False)
    # print(resp.text)
    # resp = open("./page.txt", mode="r", encoding="utf-8").read()
    # print(resp)
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
        if not ips.empty():
            session.proxies = {"https": ips.get(block=False)}
        else:
            sys.exit()
        resp_local = session.get(url=url)
        with open("./info.txt", mode="w+", encoding="utf-8") as fp:
            fp.write(resp_local.text)
        while resp_local.status_code != 200:
            session.proxies = {"https": ips.get(block=False)}
            time.sleep(0.5)
            resp_local = session.get(url=url)
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
        # class CrawlerThread(threading.Thread):
        #     def __init__(self, name):
        #         super(CrawlerThread, self).__init__()
        #         self.name = name
        #
        #     def run(self):
        #         print("{}开始执行".format(self.name))
        #         self.crawl()
        #         print("{}结束执行".format(self.name))
        #
        #     def crawl(self):
        #         while not urls.empty():
        #             try:
        #                 url = urls.get(block=False)
        #                 print("crawl url:{}".format(url))
        #                 print("{}号线程开始爬去页面".format(self.name, url))
        #
        #                 headers = {
        #                     "User_Agent": ua.random,
        #                 }
        #
        #                 # respones = session.get(url=url, headers=headers, cookies=random.choice(cookies),
        #                 #                        allow_redirects=False)
        #                 print("请求")
        #                 try:
        #                     session.proxies = {"https": ips.get(block=False)}
        #                 except:
        #                     proies = get_ip()
        #                     for ip in proies:
        #                         ips.put(ip)
        #                 respones = session.get(url=url, headers=headers, cookies=random.choice(cookies),
        #                                        allow_redirects=False)
        #                 try:
        #
        #                     while respones.status_code != 200:
        #                         print(respones.status_code, url, self.name)
        #                         try:
        #                             session.proxies = {"https": ips.get(block=False)}
        #                         except:
        #                             proies = get_ip()
        #                             for ip in proies:
        #                                 ips.put(ip)
        #                         respones = session.get(url=url, headers=headers, cookies=random.choice(cookies),
        #                                                allow_redirects=False)
        #                 except:
        #                     pass
        #                 print(respones.status_code, url)
        #                 html = respones.content.decode("utf-8")
        #                 pages.put(html)
        #             except queue.Empty:
        #                 pass
        #
        #
        # class ParserThread(threading.Thread):
        #
        #     def __init__(self, name):
        #         super(ParserThread, self).__init__()
        #         self.name = name
        #         self.db = pymysql.connect(host="47.105.54.129", user="root", port=3306, password="scc123321",
        #                                   database="house_info")
        #         self.cursor = self.db.cursor()
        #
        #     def run(self):
        #         print('{}开始执行'.format(self.name))
        #         self.parse()
        #         print('{}结束执行'.format(self.name))
        #
        #     def parse(self):
        #
        #         while not parser_thread_exit_flag:
        #             try:
        #                 page = etree.HTML(pages.get(block=False))
        #                 print(page)
        #                 items = page.xpath("//ul[@id='houselist-mod-new']/li")
        #                 print(items)
        #             except queue.Empty:
        #                 print("pages队列为空!")
        #                 time.sleep(5)
        #                 continue
        #             for item in items:
        #                 house = {}
        #                 house['title'] = item.xpath(".//a//text()")[0].strip()  # title
        #                 details = item.xpath(".//div[@class='details-item']/span//text()")  # details
        #                 house["price"] = item.xpath(".//span[@class='price-det']/strong/text()")[0]
        #                 house['rooms'] = details[0].strip()
        #                 house['size'] = details[1].strip()[:-2]
        #                 house['high'] = details[2].strip()
        #                 house['biuld_year'] = details[3].strip()[:-3]
        #                 house['unknow'] = details[4].strip()
        #                 house['addr'] = "".join([i.strip() for i in details[6]])
        #                 house['url'] = item.xpath('.//a/@href')[0]
        #                 print(house)
        #                 sql = "insert into {} (title,price,rooms,size,high,biuld_year,addr,url) values ('%s','%s','%s','%s','%s','%s','%s','%s')".format(
        #                     "CD_" + area.upper())
        #                 # with lock:
        #                 try:
        #                     self.cursor.execute(
        #                         sql % (house["title"], house["price"], house["rooms"], house['size'], house['high'],
        #                                house["biuld_year"], house['addr'], house['url']))
        #
        #                 except:
        #                     print("创建新地区的数据表")
        #                     creat_table = '''CREATE TABLE `CD_%s` (
        #                                   `title` varchar(255) DEFAULT NULL,
        #                                   `price` varchar(255) DEFAULT '',
        #                                   `rooms` varchar(255) DEFAULT '',
        #                                   `size` varchar(255) DEFAULT '',
        #                                   `high` varchar(255) DEFAULT '',
        #                                   `biuld_year` varchar(255) DEFAULT '',
        #                                   `addr` varchar(255) DEFAULT NULL,
        #                                   `date` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT '添加时间',
        #                                   `url` varchar(255) DEFAULT NULL COMMENT '详情url'
        #                                     ) ENGINE=InnoDB DEFAULT CHARSET=utf8 '''
        #                     self.cursor.execute(creat_table % (area.upper()))
        #                     self.cursor.execute(
        #                         sql % (house["title"], house["price"], house["rooms"], house['size'], house['high'],
        #                                house["biuld_year"], house['addr'], house['url']))
        #
        #                 self.db.commit()
        #
        #         # except queue.Empty as e:
        #         #     print(e)
        #
        #
        # if __name__ == '__main__':
        #     proies = get_ip()
        #     for ip in proies:
        #         ips.put(ip)
        #     for i in range(1, 51):
        #         urls.put(base_url.format(i))
        #
        #     pages = queue.Queue()
        #
        #     lock = threading.Lock()
        #     # 解析线程可以结束的条件
        #     parser_thread_exit_flag = False
        #
        #     # 准备爬取线程组
        #     crawler_threads = []
        #     for i in range(5):
        #         thread = CrawlerThread('{}号爬取线程'.format(i + 1))
        #         crawler_threads.append(thread)
        #
        #     # 启动爬取线程组
        #     for thread in crawler_threads:
        #         thread.start()
        #
        #     # 准备解析线程组
        #     parser_threads = []
        #     for i in range(4):
        #         thread = ParserThread('{}号解析线程'.format(i + 1))
        #         parser_threads.append(thread)
        #     while pages.empty():
        #         pass
        #     # 启动解析线程组
        #     for thread in parser_threads:
        #         thread.start()
        #
        #     # 确定程序终止条件
        #
        #     # 1. 等待urls取完
        #     while not urls.empty():
        #         pass
        #
        #     # 2. 等待爬取线程组结束
        #     for thread in crawler_threads:
        #         thread.join()
        #
        #     # 3. 等待pages取完
        #     while not pages.empty():
        #         pass
        #     parser_thread_exit_flag = True
        #
        #     # 等待解析线程组结束
        #     for thread in parser_threads:
        #         thread.join()
        #     # cursor.close()
        # print('爬虫程序全部执行完成')


if __name__ == '__main__':
    ips = []
    demo()
