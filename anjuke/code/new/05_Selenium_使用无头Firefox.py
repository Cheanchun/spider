"""
需求：
    使用 Selenium + 无界面Firefox 访问百度首页，搜索关键字，输出渲染后源码，保存网页快照。
"""

# 导入webdriver
from selenium import webdriver # 使用PhantomJS需要选择selenium的较早一点的版本，建议选择selenium 2.47.3

# 引入keys包，目的：使用键盘操作
from selenium.webdriver.common.keys import Keys

import time


# 通过Firefox的无头浏览器组件创建浏览器对象。
# 其中浏览器组件的位置，可以通过可执行文件路径参数指定，也可以通过环境变量指定。
fireFoxOptions = webdriver.FirefoxOptions()
# fireFoxOptions.set_headless()
fireFoxOptions.headless = True
# brower = webdriver.Firefox(firefox_options=fireFoxOptions)

# driver = webdriver.Firefox(executable_path="/Users/hero/Downloads/geckodriver/geckodriver", firefox_options=fireFoxOptions)
driver = webdriver.Firefox(firefox_options=fireFoxOptions)
# 通常，产生出的浏览器对象命名为browser或者driver


# 获取百度首页
driver.get('https://www.baidu.com/')

# get方法会一直等到页面被完全加载，然后才会继续程序；但使用time.sleep()等待加载总是一种好习惯
time.sleep(2)

# 生成网页快照
driver.save_screenshot("baidu.png")

# 模拟使用百度搜索输入框
driver.find_element_by_id("kw").send_keys("神器")


# 加入延时，应对动态加载问题
# time.sleep(0.5)
# time.sleep(2.5)
time.sleep(5)

# 点击搜索按钮
driver.find_element_by_id("su").click()

# 设置延迟，等待页面加载
time.sleep(3)

# 生成网页快照
driver.save_screenshot("神器.png")

# 输出渲染后页面的源代码
print(driver.page_source)

# 获取当前页面Cookie
print(driver.get_cookies())

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
time.sleep(3)
# time.sleep(8)

# 生成真正的新页面快照
driver.save_screenshot("skr_correct.png")


# 获取当前url
print(driver.current_url)

# 关闭当前页面，如果只有一个页面，会关闭浏览器
# driver.close()

# 关闭浏览器
driver.quit()
