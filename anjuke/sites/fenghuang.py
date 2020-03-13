import requests
from lxml import etree


# url = "http://finance.ifeng.com/listpage/110/1/list.shtml"
# res = requests.get(url)
# print(res.text)
# html = etree.HTML(res.text)
# print(html.xpath("//div[@class='list03']/ul[1]/li/span[@class='txt01']/a/@href"))

url_c = "http://finance.ifeng.com/a/20190408/17044443_0.shtml"
res = requests.get(url_c)
# print(res.text)
html = etree.HTML(res.text)
print(html.xpath("//meta/@content")[0].split("=")[1])
url_cc = html.xpath("//meta/@content")[0].split("=")[1]
res = requests.get(url_cc)
print(res.text)

