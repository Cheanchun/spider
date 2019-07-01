"""
需求:
    使用多线程完成爬取豆瓣电影top250的各条目,保存到json文件中
"""

import json
import queue
import threading

import requests
from lxml import etree


def parse_page(url):
    response = requests.get(url)

    # 得到解析出的树结构
    html_tree = etree.HTML(response.content)

    movie_items = html_tree.xpath('//div[@class="item"]')
    movies = []
    for movie_item in movie_items:
        title = movie_item.xpath('.//span[@class="title"]/text()')[0]
        rating_num = movie_item.xpath('.//span[@class="rating_num"]/text()')[0]
        reviewer_num = movie_item.xpath('.//div[@class="star"]/span[last()]/text()')[0][:-3]
        quote = movie_item.xpath('.//span[@class="inq"]/text()')[0]
        poster_url = movie_item.xpath('.//img/@src')[0]

        movie = {
            'title': title,
            'rating_num': rating_num,
            'reviewer_num': reviewer_num,
            'quote': quote,
            'poster_url': poster_url
        }

        movies.append(movie)

    with open('movies.json', 'a+', encoding='utf-8') as fp:
        json.dump(movies, fp, ensure_ascii=False)


class CrawlerThread(threading.Thread):
    """
    网页爬取线程类
    """

    def __init__(self, name):
        super(CrawlerThread, self).__init__()
        self.name = name

    def run(self):
        print('{}开始执行'.format(self.name))
        self.crawl()
        print('{}结束执行'.format(self.name))

    def crawl(self):
        # 检查是否有待爬取的url
        while not urls.empty():
            try:
                url = urls.get(block=False)

                print('{}号线程开始爬取页面{}'.format(self.name, url))
                response = requests.get(url)
                print('{}号线程完成爬取页面{}'.format(self.name, url))

                html = response.content.decode('utf-8')

                pages.put(html)
            except queue.Empty:
                pass


class ParserThread(threading.Thread):
    """
    页面解析线程类
    """

    def __init__(self, name):
        super(ParserThread, self).__init__()
        self.name = name

    def run(self):
        print('{}开始执行'.format(self.name))
        self.parse()
        print('{}结束执行'.format(self.name))

    def parse(self):
        """
        解析页面
        :return:
        """
        """
        结束条件:
            1. urls为空
            2. 爬取线程组必须全部结束
            3. pages为空
        谁来判断？
        主线程判断
        """
        while not parser_thread_exit_flag:
            try:
                html = pages.get(block=False)

                # 得到解析出的树结构
                html_tree = etree.HTML(html.encode('utf-8'))

                movie_items = html_tree.xpath('//div[@class="item"]')

                # movies = []

                for movie_item in movie_items:
                    title = movie_item.xpath('.//span[@class="title"]/text()')[0]
                    rating_num = movie_item.xpath('.//span[@class="rating_num"]/text()')[0]
                    reviewer_num = movie_item.xpath('.//div[@class="star"]/span[last()]/text()')[0][:-3]
                    quote = movie_item.xpath('.//span[@class="inq"]/text()')[0]
                    poster_url = movie_item.xpath('.//img/@src')[0]

                    movie = {
                        'title': title,
                        'rating_num': rating_num,
                        'reviewer_num': reviewer_num,
                        'quote': quote,
                        'poster_url': poster_url
                    }

                    # 试图获取锁,进行文件写
                    with g_json_lock:
                        fp.write(json.dumps(movie, ensure_ascii=False) + '\n')
                    # movies.append(movie)

                # print(movies)
            except queue.Empty:
                pass


# 文件锁
g_json_lock = threading.Lock()

if __name__ == '__main__':
    # 解析线程可以结束的条件
    parser_thread_exit_flag = False

    # jsonline文件
    with open('movies250.jl', 'w', encoding='utf-8') as fp:
        # 确定待爬取的地址池urls
        urls = queue.Queue()
        for i in range(10):
            url = "https://movie.douban.com/top250?start={}&filter=".format(i * 25)
            urls.put(url)

        # 准备已爬取的页面池pages
        pages = queue.Queue()

        # 准备爬取线程组
        crawler_threads = []
        for i in range(3):
            thread = CrawlerThread('{}号爬取线程'.format(i + 1))
            crawler_threads.append(thread)

        # 启动爬取线程组
        for thread in crawler_threads:
            thread.start()

        # 准备解析线程组
        parser_threads = []
        for i in range(2):
            thread = ParserThread('{}号解析线程'.format(i + 1))
            parser_threads.append(thread)

        # 启动解析线程组
        for thread in parser_threads:
            thread.start()

        # 确定程序终止条件

        # 1. 等待urls取完
        while not urls.empty():
            pass

        # 2. 等待爬取线程组结束
        for thread in crawler_threads:
            thread.join()

        # 3. 等待pages取完
        while not pages.empty():
            pass
        """
        解析线程结束条件:
            1. urls为空
            2. 爬取线程组必须全部结束
            3. pages为空
        谁来判断？
        主线程判断
        """
        parser_thread_exit_flag = True

        # 等待解析线程组结束
        for thread in parser_threads:
            thread.join()

    print('爬虫程序全部执行完成')
