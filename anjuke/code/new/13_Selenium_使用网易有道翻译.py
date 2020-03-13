"""

"""

from selenium import webdriver
import time

class Fanyiyoudao():
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/'
        # self.driver = webdriver.PhantomJS('/Users/hero/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
        self.driver = webdriver.Chrome()

    def translate(self, keyword):
        self.driver.get(self.url)
        time.sleep(3)

        self.driver.find_element_by_id('inputOriginal').send_keys(keyword)
        time.sleep(2)

        return {keyword: self.driver.find_element_by_id('transTarget').text}
    def __del__(self):
        self.driver.close()
        # self.driver.quit()


if __name__ == '__main__':
    fanyi_youdao = Fanyiyoudao()
    # keyword = 'Winter is coming'
    print(fanyi_youdao.translate('Winter is coming'))
    # print("{}: {}".format(keyword, fanyi_youdao.translate(keyword)))

    # keyword =
    print(fanyi_youdao.translate('凛冬将至'))
