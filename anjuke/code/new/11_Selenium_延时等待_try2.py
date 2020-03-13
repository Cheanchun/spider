# 导入webdriver
from selenium import webdriver # 使用PhantomJS需要选择selenium的较早一点的版本，建议选择selenium 2.47.3

# 引入keys包，目的：使用键盘操作
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time


# 通过PhantomJS浏览器组件创建浏览器对象。
# 其中浏览器组件的位置，可以通过可执行文件路径参数指定，也可以通过环境变量指定。
# driver = webdriver.Chrome(executable_path="/Users/hero/Downloads/chromedriver")
driver = webdriver.PhantomJS()
# driver = webdriver.Chrome() # /usr/local/bin
# 通常，产生出的浏览器对象命名为browser或者driver

# 方法2. 设置隐式等待时间，如果没有找到节点时，将继续等待；如果超出设定时间，则抛出找不到节点的异常。
driver.implicitly_wait(10)


# 获取百度首页
driver.get('https://www.baidu.com/')

# get方法会一直等到页面被完全加载，然后才会继续程序；但使用time.sleep()等待加载总是一种好习惯
# time.sleep(2)

# 生成网页快照
driver.save_screenshot("baidu.png")

# 模拟使用百度搜索输入框
driver.find_element_by_id("kw").send_keys("神器")
# driver.find_element(By.ID, "kw").send_keys("神器")


# 加入延时，应对动态加载问题（主要是在MacOS下）
# time.sleep(0.5)
# time.sleep(2.5)
# time.sleep(5)


print(time.time())

# 方法1. 使用time.sleep()，缺点：不需要等待的情况下也会等待
# time.sleep(0.5)


# 点击搜索按钮
search_btn = driver.find_element_by_id("su")

search_btn.click()

print(time.time())

# 生成网页快照
driver.save_screenshot("神器.png")
