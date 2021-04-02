#coding:utf-8

from intelligent_parse import IntelligentParse

_urls = ['industry.cfi.cn', 'finance.chinanews.com', 'news.winshang.com', 'time-weekly.com', 'changjiangtimes.com',
             'fj.xinhuanet.com', 'iyiou.com', 'jinbw.com', 'xa.winshang.com', 'ceweekly.cn', 'finance.qianlong.com',
             'p5w.net', 'cneo.com', 'jjckb.xinhuanet.com', 'chinanews.com', '21jingji.com', 'ifnews.com', 'chinatimes',
             'fortune.chinanews']


urls = [
    "http://www.safe.gov.cn/safe/2005/0923/5686.html",
"http://www.safe.gov.cn/safe/2005/0906/5339.html",
"http://www.safe.gov.cn/safe/2005/0825/5465.html",
"http://www.safe.gov.cn/safe/2005/0816/5622.html",
"http://www.safe.gov.cn/safe/2005/0808/5685.html",
"http://www.safe.gov.cn/safe/2005/0802/5684.html",
"http://www.safe.gov.cn/safe/2005/0721/5682.html",
"http://www.safe.gov.cn/safe/2005/0721/5683.html",
"http://www.safe.gov.cn/safe/2005/0620/5330.html",
"http://www.safe.gov.cn/safe/2005/0519/5523.html",
"http://www.safe.gov.cn/safe/2005/0517/5566.html",
"http://www.safe.gov.cn/safe/2005/0408/5621.html",
"http://www.safe.gov.cn/safe/2005/0406/5522.html",
"http://www.safe.gov.cn/safe/2005/0401/5620.html",
"http://www.safe.gov.cn/safe/2005/0331/5521.html",
"http://www.safe.gov.cn/safe/2005/0303/5520.html",
"http://www.safe.gov.cn/safe/2005/0201/5519.html",
"http://www.safe.gov.cn/safe/2005/0131/5464.html",
"http://www.safe.gov.cn/safe/2005/0127/5518.html",
"http://www.safe.gov.cn/safe/2005/0127/5463.html",
"http://www.safe.gov.cn/safe/2005/0126/5619.html",
"http://www.safe.gov.cn/safe/2004/1217/5618.html",
"http://www.safe.gov.cn/safe/2004/1209/5462.html",
"http://www.safe.gov.cn/safe/2004/1116/5461.html",
"http://www.safe.gov.cn/safe/2004/1027/5652.html",
"http://www.safe.gov.cn/safe/2004/1027/5517.html",
"http://www.safe.gov.cn/safe/2004/1018/5460.html",
"http://www.safe.gov.cn/safe/2004/1013/5338.html",
"http://www.safe.gov.cn/safe/2004/0920/5337.html",
"http://www.safe.gov.cn/safe/2004/0902/5407.html",
"http://www.safe.gov.cn/safe/2004/0810/5437.html",
"http://www.safe.gov.cn/safe/2004/0810/5406.html",
"http://www.safe.gov.cn/safe/2004/0809/8853.html",
"http://www.safe.gov.cn/safe/2004/0715/5565.html",
"http://www.safe.gov.cn/safe/2004/0705/8764.html",
"http://www.safe.gov.cn/safe/2004/0630/5650.html",
"http://www.safe.gov.cn/safe/2004/0630/5651.html",
"http://www.safe.gov.cn/safe/2004/0629/8763.html",
"http://www.safe.gov.cn/safe/2004/0621/5617.html",
"http://www.safe.gov.cn/safe/2004/0615/5681.html",
"http://www.safe.gov.cn/safe/2004/0527/5616.html",
"http://www.safe.gov.cn/safe/2004/0517/5459.html",
"http://www.safe.gov.cn/safe/2004/0516/5649.html",
"http://www.safe.gov.cn/safe/2004/0420/5615.html",
"http://www.safe.gov.cn/safe/2004/0414/5680.html",
"http://www.safe.gov.cn/safe/2004/0408/8851.html",
"http://www.safe.gov.cn/safe/2004/0325/5679.html",
"http://www.safe.gov.cn/safe/2004/0325/8850.html",
"http://www.safe.gov.cn/safe/2004/0322/5445.html",
"http://www.safe.gov.cn/safe/2004/0308/5516.html",
"http://www.safe.gov.cn/safe/2004/0301/8849.html",
"http://www.safe.gov.cn/safe/2004/0218/5515.html",
"http://www.safe.gov.cn/safe/2003/1125/5317.html",
"http://www.safe.gov.cn/safe/2003/1117/5514.html",
"http://www.safe.gov.cn/safe/2003/1017/5678.html",
"http://www.safe.gov.cn/safe/2003/1016/5405.html",
"http://www.safe.gov.cn/safe/2003/1015/5513.html",
"http://www.safe.gov.cn/safe/2003/1008/8848.html",
"http://www.safe.gov.cn/safe/2003/0924/5564.html",
"http://www.safe.gov.cn/safe/2003/0922/6833.html",
"http://www.safe.gov.cn/safe/2003/0912/5563.html",
"http://www.safe.gov.cn/safe/2003/0909/5677.html",
"http://www.safe.gov.cn/safe/2003/0908/5404.html",
"http://www.safe.gov.cn/safe/2003/0901/8847.html",
"http://www.safe.gov.cn/safe/2003/0828/5444.html",
"http://www.safe.gov.cn/safe/2003/0708/5512.html",
"http://www.safe.gov.cn/safe/2003/0701/5403.html",
"http://www.safe.gov.cn/safe/2003/0626/5511.html",
"http://www.safe.gov.cn/safe/2003/0604/5562.html",
"http://www.safe.gov.cn/safe/2003/0428/5676.html",
"http://www.safe.gov.cn/safe/2003/0422/8760.html",
"http://www.safe.gov.cn/safe/2003/0412/5510.html",
"http://www.safe.gov.cn/safe/2003/0403/5458.html",
"http://www.safe.gov.cn/safe/2003/0329/5561.html",
"http://www.safe.gov.cn/safe/2003/0319/5509.html",
"http://www.safe.gov.cn/safe/2003/0306/5508.html",
"http://www.safe.gov.cn/safe/2003/0303/8844.html",
"http://www.safe.gov.cn/safe/2003/0226/8843.html",
"http://www.safe.gov.cn/safe/2003/0221/5648.html",
"http://www.safe.gov.cn/safe/2003/0218/5507.html",
"http://www.safe.gov.cn/safe/2003/0208/8842.html",
"http://www.safe.gov.cn/safe/2003/0120/5506.html",
"http://www.safe.gov.cn/safe/2003/0108/5614.html",
"http://www.safe.gov.cn/safe/2003/0106/5613.html",
"http://www.safe.gov.cn/safe/2002/1231/5647.html",
"http://www.safe.gov.cn/safe/2002/1230/5505.html",
"http://www.safe.gov.cn/safe/2002/1212/5504.html",
"http://www.safe.gov.cn/safe/2002/1206/5612.html",
"http://www.safe.gov.cn/safe/2002/1129/5675.html",
"http://www.safe.gov.cn/safe/2002/1128/5560.html",
"http://www.safe.gov.cn/safe/2002/1127/5503.html",
"http://www.safe.gov.cn/safe/2002/1119/5559.html",
"http://www.safe.gov.cn/safe/2002/1118/5502.html",
"http://www.safe.gov.cn/safe/2002/1112/5501.html",
"http://www.safe.gov.cn/safe/2002/1024/5500.html",
"http://www.safe.gov.cn/safe/2002/0927/5402.html",
"http://www.safe.gov.cn/safe/2002/0924/8841.html",
"http://www.safe.gov.cn/safe/2002/0909/5558.html",
"http://www.safe.gov.cn/safe/2002/0827/5336.html",
"http://www.safe.gov.cn/safe/2002/0820/5557.html",
"http://www.safe.gov.cn/safe/2002/0816/5334.html",
"http://www.safe.gov.cn/safe/2002/0816/5335.html",
"http://www.safe.gov.cn/safe/2002/0708/5611.html",
"http://www.safe.gov.cn/safe/2002/0704/5499.html",
"http://www.safe.gov.cn/safe/2002/0617/5498.html",
"http://www.safe.gov.cn/safe/2002/0430/5497.html",
"http://www.safe.gov.cn/safe/2002/0422/5610.html",
"http://www.safe.gov.cn/safe/2002/0315/5496.html",
"http://www.safe.gov.cn/safe/2002/0307/5315.html",
"http://www.safe.gov.cn/safe/2002/0226/5674.html",
"http://www.safe.gov.cn/safe/2002/0226/8840.html",
"http://www.safe.gov.cn/safe/2002/0220/8839.html",
"http://www.safe.gov.cn/safe/2002/0201/5333.html",
"http://www.safe.gov.cn/safe/2002/0124/5673.html",
"http://www.safe.gov.cn/safe/2001/1225/5495.html",
"http://www.safe.gov.cn/safe/2001/1024/5457.html",
"http://www.safe.gov.cn/safe/2018/0117/8181.html",
"http://www.safe.gov.cn/safe/2001/0903/5556.html",
"http://www.safe.gov.cn/safe/2001/0808/5609.html",
"http://www.safe.gov.cn/safe/2001/0720/5608.html",
"http://www.safe.gov.cn/safe/2001/0711/5555.html",
"http://www.safe.gov.cn/safe/2001/0711/5607.html",
"http://www.safe.gov.cn/safe/2001/0403/5456.html",
"http://www.safe.gov.cn/safe/2001/0223/5553.html",
"http://www.safe.gov.cn/safe/2001/0223/5554.html",
"http://www.safe.gov.cn/safe/2001/0222/5552.html",
"http://www.safe.gov.cn/safe/2001/0101/5455.html",
"http://www.safe.gov.cn/safe/2000/0822/5454.html",
"http://www.safe.gov.cn/safe/2000/0817/8838.html",
"http://www.safe.gov.cn/safe/2000/0815/5606.html",
"http://www.safe.gov.cn/safe/2000/0810/5605.html",
"http://www.safe.gov.cn/safe/2000/0717/5494.html",
"http://www.safe.gov.cn/safe/2000/0519/5453.html",
"http://www.safe.gov.cn/safe/2000/0413/5604.html",
"http://www.safe.gov.cn/safe/2000/0223/5603.html",
"http://www.safe.gov.cn/safe/2000/0111/5602.html",
"http://www.safe.gov.cn/safe/1999/1222/5493.html",
"http://www.safe.gov.cn/safe/1999/1213/5551.html",
"http://www.safe.gov.cn/safe/1999/1103/5452.html",
"http://www.safe.gov.cn/safe/1999/1018/5451.html",
"http://www.safe.gov.cn/safe/1999/0909/5332.html",
"http://www.safe.gov.cn/safe/1999/0730/5492.html",
"http://www.safe.gov.cn/safe/1999/0518/5331.html",
"http://www.safe.gov.cn/safe/1999/0420/5491.html",
"http://www.safe.gov.cn/safe/1999/0222/5744.html",
"http://www.safe.gov.cn/safe/1999/0107/5450.html",
"http://www.safe.gov.cn/safe/1998/1229/5743.html",
"http://www.safe.gov.cn/safe/1998/1216/5742.html",
"http://www.safe.gov.cn/safe/1998/0926/5601.html",
"http://www.safe.gov.cn/safe/1998/0915/5449.html",
"http://www.safe.gov.cn/safe/1998/0831/5600.html",
"http://www.safe.gov.cn/safe/1998/0828/5741.html",
"http://www.safe.gov.cn/safe/1998/0820/5599.html",
"http://www.safe.gov.cn/safe/1998/0719/5740.html",
"http://www.safe.gov.cn/safe/1998/0708/5598.html",
"http://www.safe.gov.cn/safe/1998/0513/5314.html",
    # "http://www.safe.gov.cn/safe/2020/0312/15681.html"
    # "http://finance.cnwest.com/cjzx/a/2020/03/13/18569185.html"
    # "http://finance.cnwest.com/cjzx/a/2020/03/13/18569185.html"
    # "https://www.ndrc.gov.cn/xxgk/zcfb/fzggwl/201911/t20191105_1198077.html"
    # "https://www.ndrc.gov.cn/xxgk/zcfb/fzggwl/201909/t20190902_960878.html"
# 'https://money.eastmoney.com/a/202003121415065275.html'
# 'http://caifuhao.eastmoney.com/news/20200311184844060020830'
# 'http://finance.eastmoney.com/a/202003131417221585.html'
# 'http://stock.eastmoney.com/a/202003121416012179.html'
# 'http://finance.eastmoney.com/a/202003121415416475.html'
  # "http://www.chinanews.com/gj/2020/02-29/9109031.shtml"
# "http://www.chinanews.com/cj/2020/02-28/9107860.shtml"
    #有问题
# "http://www.chinanews.com/sh/2020/02-29/9109012.shtml"
# 'http://finance.chinanews.com/cj/2020/02-29/9109235.shtml'
# 'http://finance.chinanews.com/cj/2020/02-29/9109090.shtml'
# 'http://finance.chinanews.com/cj/2020/02-28/9107580.shtml'
# 'http://news.winshang.com/html/066/9903.html'
# 'http://news.winshang.com/html/066/9836.html'
# 'http://www.time-weekly.com/html/20191231/265344_1.html'
# 'http://www.fj.xinhuanet.com/shidian/2020-02/29/c_1125641965.htm'
# 'http://www.fj.xinhuanet.com/yuanchuang/2020-02/22/c_1125611373.htm'
# 'https://www.iyiou.com/p/124274.html'
# 'https://www.iyiou.com/intelligence/insight124293.html'
# 'http://news.winshang.com/html/066/9858.html'
# 'http://news.winshang.com/html/066/9861.html'
# 'http://finance.qianlong.com/2020/0229/3768127.shtml'
# 'http://www.p5w.net/kuaixun/202002/t20200228_2383099.htm'
# 'http://www.p5w.net/kuaixun/201801/t20180110_2060565.htm'
# 'http://weyt.p5w.net/article/2382925'
# 'http://www.jjckb.cn/2020-02/28/c_138827816.htm'
#     "https://blog.csdn.net/qq_33589510/article/details/104057498?depth_1-utm_source=distribute.pc_feed.none-task&request_id=&utm_source=distribute.pc_feed.none-task"
        ]
for url in urls:
    print(url)
    intelligent_parse = IntelligentParse(url=url)
    content = intelligent_parse.intelligent_main()
    print(content)