from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # 等待

url = "https://www.baidu.com"
# url = "https://ie.icoa.cn/"
display = Display(visible=0, size=(1280, 800))  # 创建虚拟展示界面
display.start()  # 开始
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options)
driver.get(url=url)
WebDriverWait(driver, 10)
driver.save_screenshot("./baidu1.png")
print(driver.page_source)

