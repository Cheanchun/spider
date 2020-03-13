"""

"""


from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()

browser.get('https://www.zhihu.com/explore')

logo = browser.find_element_by_id('zh-top-link-logo')

print(logo)

# 获取属性
print(logo.get_attribute('class'))

# 获取文本
print(logo.text)

# 获取ID
print(logo.id)

# 获取位置
print(logo.location)

# 获取标签名
print(logo.tag_name)

# 获取size
print(logo.size)
