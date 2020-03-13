"""
rn = 'de481cbc87141b5d6fca922ec7b85bd7', MD5, 128-bit

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from lxml import etree
import time


class Taobao():
    """
    淘宝商品数据爬取类
    """
    def __init__(self):
        self.url = 'https://www.taobao.com/'
        # 这里使用Chrome浏览器，正式爬取的时候，可以设置无界面选项，提高效率。
        self.browser = webdriver.Chrome()
        self.maxPageNum = 10
        # 设定最大等待时间
        # self.wait = WebDriverWait(10)
        self.wait = WebDriverWait(self.browser, 10)

    def searchProducts(self, product_name):
        """
        搜索商品，解析商品数据
        :param product_name:
        :return: 返回商品字典数据的迭代器
        """
        # 加载url对应页面
        self.browser.get(self.url)

        # 模拟使用搜索框搜索商品信息
        input_box = self.browser.find_element_by_id('q')
        input_box.send_keys(product_name)
        input_box.send_keys(Keys.ENTER)

        # 返回迭代器
        for product in self.getProducts(1):
            yield product

    def getProducts(self, page_num):
        """
        获取页面的商品数据
        :param page_num:
        :return: 返回商品数据的迭代器
        """
        # 解析当前页面内容
        print("page " + str(page_num) + ": ")
        # self.wait.until(EC.text_to_be_present_in_element((By.XPATH, '//li[@class="item active"]/span/text()'), str(page_num)))
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        for product in self.parsePage(self.browser.page_source):
            yield product

        # 跳转到下一页页面
        if page_num < self.maxPageNum:
            try:
                next_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@class="item next"]')))
                next_btn.click()
                time.sleep(1)
                for product in self.getProducts(page_num + 1):
                    yield product
            except TimeoutException:
                self.browser.refresh()
                # self.getProducts(page_num)
                for product in self.getProducts(page_num):
                    yield product

    def parsePage(self, page_source):
        """
        解析商品页面，获得产品列表
        :param page_source:
        :return:
        """
        # 解析得到DOM树结构
        html_tree = etree.HTML(page_source)

        # 解析出每个商品条目
        # html_tree.xpath('//div[@class="items"]')
        # html_tree.xpath('//div[@class="m-itemlist"]//div[@class="items"]/div[@class="item J_MouserOnverReq"]')
        # for item in html_tree.xpath('//div[@class="item J_MouserOnverReq"]'):
        for item in html_tree.xpath('//div[@class="m-itemlist"]//div[@class="items"]//div[contains(@class,"item")]'):
            # 解析商品信息
            # title = item.xpath('.//div[contains(@class, "title")]/a/span/text()').extract_first()
            # title = item.xpath('.//div[contains(@class, "title")]/a/text()').extract_first()
            # title = item.xpath('.//div[contains(@class, "title")]/a/text()')[0]
            title = ''.join(item.xpath('.//div[contains(@class, "title")]/a//text()')).strip()
            # print('='*80)
            # print(title)
            # print(item)
            # 解析商品价格
            price = item.xpath('.//strong/text()')[0]

            # 返回商品数据的迭代器
            yield {
                'title': title,
                'price': price
            }

    def __del__(self):
        self.browser.close()


def run_main():
    taobao = Taobao()
    # taobao.loadWeb('iPad')
    products = taobao.searchProducts('iPad')
    for product in products:
        print(product)


if __name__ == '__main__':
    run_main()
