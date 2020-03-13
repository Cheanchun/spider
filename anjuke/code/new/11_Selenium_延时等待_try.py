from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Chrome()

# browser.implicitly_wait(10)

#
browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
input_box = browser.find_element_by_id('q')
input_box.send_keys('iPad')
input_box.send_keys(Keys.ENTER)


browser.find_element_by_id('q')


# browser.get('https://movie.douban.com/top250')
#
# next_btn = browser.find_element_by_css_selector('.next a')
# next_btn.click()
#
# # import time
# #
# # time.sleep(0.2)
#
# print(time.time())
#
# next_btn = browser.find_element_by_css_selector('.next a')
# next_btn.click()
#
# print(time.time())

# browser.get('https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0')
#
# more_btn = browser.find_element_by_css_selector('.more')
# more_btn.click()
#
# more_btn = browser.find_element_by_css_selector('.more')
# print(more_btn)
# more_btn.click()
#
# more_btn = browser.find_element_by_css_selector('.more')
# print(more_btn)



"""

# 通过PhantomJS浏览器组件创建浏览器对象。
# 其中浏览器组件的位置，可以通过可执行文件路径参数指定，也可以通过环境变量指定。
# driver = webdriver.Chrome(executable_path="/Users/hero/Downloads/chromedriver")
driver = webdriver.Chrome() # /usr/local/bin
# 通常，产生出的浏览器对象命名为browser或者driver


# 获取百度首页
driver.get('https://www.baidu.com/')

# 模拟使用百度搜索输入框
driver.find_element_by_id("kw").send_keys("神器")
# driver.find_element(By.ID, "kw").send_keys("神器")


# 加入延时，应对动态加载问题（主要是在MacOS下）
# time.sleep(0.5)
# time.sleep(2.5)
# time.sleep(5)

# 点击搜索按钮
driver.find_element_by_id("su").click()

# 设置延迟，等待页面加载
# time.sleep(3)


# # 生成网页快照
# driver.save_screenshot("神器.png")
#
# # 输出渲染后页面的源代码
# print(driver.page_source)
#
# # 获取当前页面Cookie
# print(driver.get_cookies())

# 使用clear()方法清除搜索输入框内容
driver.find_element_by_id("kw").clear()



# 输入框重新输入内容
driver.find_element_by_id("kw").send_keys("skr")

# 模拟Enter回车键
driver.find_element_by_id("kw").send_keys(Keys.RETURN)
# driver.find_element_by_id("su").send_keys(Keys.RETURN)

# 清除输入框内容
driver.find_element_by_id("kw").clear()

# 生成新的页面快照
driver.save_screenshot("skr.png")


# 设置延迟，等待页面加载
# time.sleep(3)
# time.sleep(8)

# 生成真正的新页面快照
# driver.save_screenshot("skr_correct.png")


# 获取当前url
print(driver.current_url)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()

# 关闭浏览器
# driver.quit()

"""
