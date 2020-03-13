import time
from selenium import webdriver

class Douban():
    def __init__(self):
        self.url = "https://www.douban.com/"
        # self.driver = webdriver.PhantomJS('/Users/hero/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
        self.driver = webdriver.Chrome()

    def log_in(self):
        self.driver.get(self.url)
        time.sleep(3) #睡3秒，等待页面加载
        self.driver.save_screenshot("before_login.jpg")

        #输入账号
        self.driver.find_element_by_xpath('//*[@id="form_email"]').send_keys("herodolphin@163.com")

        #输入密码
        self.driver.find_element_by_xpath('//*[@id="form_password"]').send_keys("itsource@520")

        #点击登陆
        self.driver.find_element_by_class_name("bn-submit").click()
        time.sleep(2)

        self.driver.save_screenshot("after_login.jpg")
        #输出登陆之后的cookies
        print(self.driver.get_cookies())

    def __del__(self):
        '''调用内建的稀构方法，在程序退出的时候自动调用
        类似的还可以在文件打开的时候调用close，数据库链接的断开
        '''
        self.driver.quit()

if __name__ == "__main__":
    douban = Douban() #实例化
    douban.log_in() #之后调用登陆方法
