"""
使用隐式等待
"""

from selenium import webdriver


browser = webdriver.Chrome()
# browser = webdriver.Firefox()

# browser.implicitly_wait(10)

# browser.get('https://www.zhihu.com/explore')
#
# input_box = browser.find_element_by_id('q')
#
# print(input_box)



# # 获取百度首页
# browser.get('https://www.baidu.com/')
#
# # get方法会一直等到页面被完全加载，然后才会继续程序；但使用time.sleep()等待加载总是一种好习惯
# # time.sleep(2)
#
#
# # 模拟使用百度搜索输入框
# browser.find_element_by_id("kw").send_keys("神器")
#
#
# # 加入延时，应对动态加载问题（主要是在MacOS下）
# # time.sleep(0.5)
# # time.sleep(2.5)
# # time.sleep(5)
#
# # 点击搜索按钮
# browser.find_element_by_id("su").click()
#
# # 设置延迟，等待页面加载
# # time.sleep(3)

# browser.find_element_by_id("kw").clear()
# browser.find_element_by_id('kw').send_keys('skr')
#
# browser.find_element_by_id("su").click()

import time

browser.implicitly_wait(10)

browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# time.sleep(10)

print(time.time())

# browser.switch_to.frame('iframeResult')

# time.sleep(30)

# source = browser.find_element_by_id('draggable')
# target = browser.find_element_by_id('droppable')

browser.switch_to.frame('google_ads_frame1')

browser.find_element_by_id('google_ads_frame1')

print(time.time())
