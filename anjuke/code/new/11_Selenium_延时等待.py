"""

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browser = webdriver.Chrome()

# 方法2. 设置隐式等待
# browser.implicitly_wait(10)


print(time.time())

browser.get('https://www.taobao.com/')

# 方法1. 等待一定时间
# time.sleep(10)

# input_box = browser.find_element_by_id('q')
# search_btn = browser.find_element_by_css_selector('.btn-search')

# 方法3. 使用显示等待
wait = WebDriverWait(browser, 10)

input_box = wait.until(EC.presence_of_element_located((By.ID, 'q')))
search_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))

print(input_box, search_btn)

print(time.time())
