#coding:utf-8

from intelligent_parse import IntelligentParse
#https://money.eastmoney.com/a/202003121415065275.html
#http://caifuhao.eastmoney.com/news/20200311184844060020830
#http://finance.eastmoney.com/a/202003131417221585.html
#http://stock.eastmoney.com/a/202003121416012179.html
#http://finance.eastmoney.com/a/202003121415416475.html

intelligent_parse = IntelligentParse(url="http://finance.eastmoney.com/a/202003121415416475.html")
intelligent_parse.intelligent_main()