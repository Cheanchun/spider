"""
需求：
    使用动作链ActionChains实现控件拖拽操作。
"""


from selenium import webdriver
from selenium.webdriver import ActionChains # 动作链

browser = webdriver.Chrome()

browser.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 首先移动到结果框iframeResult中
# browser.switch_to_frame('iframeResult')
browser.switch_to.frame('iframeResult')


source = browser.find_element_by_id('draggable')
target = browser.find_element_by_id('droppable')

actions = ActionChains(browser)

actions.drag_and_drop(source, target)

actions.perform()
