"""

"""

from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.zhihu.com/explore')

# JS脚本：滑动滚动条到底部
script = """
window.scrollTo(0, document.body.scrollHeight)
alert("To Bottom")
"""

# 执行JS脚本
# browser.execute_script(script)

# 保证顺序执行
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
