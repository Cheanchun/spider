from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()

try:
    browser.get('https://www.baidu.com')

    # 使用搜索输入框搜索
    input_box = browser.find_element_by_id('kw')
    input_box.send_keys('亚运会电子竞技')
    input_box.send_keys(Keys.ENTER)

    # 设置最多等待10秒，超过10秒产生异常
    wait = WebDriverWait(browser, 10)

    # 等待，直到找到ID为'content_left'的Web元素，或者超过10秒产生异常
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))

    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
