from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

input_box = browser.find_element_by_id('q')
input_box.send_keys('iPhone')

time.sleep(1)
input_box.clear()

input_box.send_keys('iPad')

search_btn = browser.find_element_by_class_name('btn-search')
search_btn.click()
