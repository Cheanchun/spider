"""

"""

import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
# browser.get('https://www.douban.com/')
browser.get('https://movie.douban.com/top250')
# browser.get('https://www.python.org/')

browser.back()

time.sleep(1)

browser.forward()

# browser.close()

browser.get('https://www.baidu.com/')
browser.execute_script('window.open()')
print(browser.window_handles)

# browser.switch_to_window(browser.window_handles[1])
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com/')

time.sleep(1)

browser.switch_to.window(browser.window_handles[0])
browser.get('https://movie.douban.com/top250')

