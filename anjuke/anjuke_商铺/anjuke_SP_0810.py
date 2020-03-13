# encoding: utf-8
import random
import sys
import time

import fake_useragent
import re
import redis
import requests
# from api_develop.develop_job_base import DevelopJobBase
from lxml import etree

ua = fake_useragent.UserAgent()
area_start_url = ['https://anshan.sp.anjuke.com/zu/p1', 'https://anyang.sp.anjuke.com/zu/p1',
                  'https://anqing.sp.anjuke.com/zu/p1', 'https://ankang.sp.anjuke.com/zu/p1',
                  'https://anshun.sp.anjuke.com/zu/p1', 'https://aba.sp.anjuke.com/zu/p1',
                  'https://akesu.sp.anjuke.com/zu/p1', 'https://ali.sp.anjuke.com/zu/p1',
                  'https://alaer.sp.anjuke.com/zu/p1', 'https://alashanmeng.sp.anjuke.com/zu/p1',
                  'https://aomen.sp.anjuke.com/zu/p1', 'https://anda.sp.anjuke.com/zu/p1',
                  'https://anqiu.sp.anjuke.com/zu/p1', 'https://anning.sp.anjuke.com/zu/p1',
                  'https://anguo.sp.anjuke.com/zu/p1', 'https://aershan.sp.anjuke.com/zu/p1',
                  'https://atushi.sp.anjuke.com/zu/p1', 'https://anlu.sp.anjuke.com/zu/p1',
                  'https://beijing.sp.anjuke.com/zu/p1', 'https://baoding.sp.anjuke.com/zu/p1',
                  'https://baotou.sp.anjuke.com/zu/p1', 'https://binzhou.sp.anjuke.com/zu/p1',
                  'https://baoji.sp.anjuke.com/zu/p1', 'https://bengbu.sp.anjuke.com/zu/p1',
                  'https://benxi.sp.anjuke.com/zu/p1', 'https://beihai.sp.anjuke.com/zu/p1',
                  'https://bayinguoleng.sp.anjuke.com/zu/p1', 'https://bazhong.sp.anjuke.com/zu/p1',
                  'https://bayannaoer.sp.anjuke.com/zu/p1', 'https://bozhou.sp.anjuke.com/zu/p1',
                  'https://baiyin.sp.anjuke.com/zu/p1', 'https://baicheng.sp.anjuke.com/zu/p1',
                  'https://baise.sp.anjuke.com/zu/p1', 'https://baishan.sp.anjuke.com/zu/p1',
                  'https://boertala.sp.anjuke.com/zu/p1', 'https://bijie.sp.anjuke.com/zu/p1',
                  'https://baoshan.sp.anjuke.com/zu/p1', 'https://bazh.sp.anjuke.com/zu/p1',
                  'https://beian.sp.anjuke.com/zu/p1', 'https://beipiao.sp.anjuke.com/zu/p1',
                  'https://botou.sp.anjuke.com/zu/p1', 'https://bole.sp.anjuke.com/zu/p1',
                  'https://beiliu.sp.anjuke.com/zu/p1', 'https://chengdu.sp.anjuke.com/zu/p1',
                  'https://chongqing.sp.anjuke.com/zu/p1', 'https://cs.sp.anjuke.com/zu/p1',
                  'https://cz.sp.anjuke.com/zu/p1', 'https://cc.sp.anjuke.com/zu/p1',
                  'https://cangzhou.sp.anjuke.com/zu/p1', 'https://changji.sp.anjuke.com/zu/p1',
                  'https://chifeng.sp.anjuke.com/zu/p1', 'https://changde.sp.anjuke.com/zu/p1',
                  'https://chenzhou.sp.anjuke.com/zu/p1', 'https://chengde.sp.anjuke.com/zu/p1',
                  'https://changzhi.sp.anjuke.com/zu/p1', 'https://chizhou.sp.anjuke.com/zu/p1',
                  'https://chuzhou.sp.anjuke.com/zu/p1', 'https://chaoyang.sp.anjuke.com/zu/p1',
                  'https://chaozhou.sp.anjuke.com/zu/p1', 'https://chuxiong.sp.anjuke.com/zu/p1',
                  'https://chaohu.sp.anjuke.com/zu/p1', 'https://changdu.sp.anjuke.com/zu/p1',
                  'https://changge.sp.anjuke.com/zu/p1', 'https://chongzuo.sp.anjuke.com/zu/p1',
                  'https://changshushi.sp.anjuke.com/zu/p1', 'https://changyi.sp.anjuke.com/zu/p1',
                  'https://changning.sp.anjuke.com/zu/p1', 'https://chibi.sp.anjuke.com/zu/p1',
                  'https://cengxi.sp.anjuke.com/zu/p1', 'https://chishui.sp.anjuke.com/zu/p1',
                  'https://cixi.sp.anjuke.com/zu/p1', 'https://chongzhou.sp.anjuke.com/zu/p1',
                  'https://dalian.sp.anjuke.com/zu/p1', 'https://dg.sp.anjuke.com/zu/p1',
                  'https://deyang.sp.anjuke.com/zu/p1', 'https://dali.sp.anjuke.com/zu/p1',
                  'https://dezhou.sp.anjuke.com/zu/p1', 'https://dongying.sp.anjuke.com/zu/p1',
                  'https://daqing.sp.anjuke.com/zu/p1', 'https://dandong.sp.anjuke.com/zu/p1',
                  'https://datong.sp.anjuke.com/zu/p1', 'https://dazhou.sp.anjuke.com/zu/p1',
                  'https://dafeng.sp.anjuke.com/zu/p1', 'https://dehong.sp.anjuke.com/zu/p1',
                  'https://dingzhou.sp.anjuke.com/zu/p1', 'https://diqing.sp.anjuke.com/zu/p1',
                  'https://dingxi.sp.anjuke.com/zu/p1', 'https://dxanling.sp.anjuke.com/zu/p1',
                  'https://dongtai.sp.anjuke.com/zu/p1', 'https://dengzhou.sp.anjuke.com/zu/p1',
                  'https://dehui.sp.anjuke.com/zu/p1', 'https://dangyang.sp.anjuke.com/zu/p1',
                  'https://dongfang.sp.anjuke.com/zu/p1', 'https://danzhou.sp.anjuke.com/zu/p1',
                  'https://dunhuashi.sp.anjuke.com/zu/p1', 'https://danyang.sp.anjuke.com/zu/p1',
                  'https://dashiqiao.sp.anjuke.com/zu/p1', 'https://dengta.sp.anjuke.com/zu/p1',
                  'https://dunhuang.sp.anjuke.com/zu/p1', 'https://delingha.sp.anjuke.com/zu/p1',
                  'https://daye.sp.anjuke.com/zu/p1', 'https://duyun.sp.anjuke.com/zu/p1',
                  'https://dongxing.sp.anjuke.com/zu/p1', 'https://dongyang.sp.anjuke.com/zu/p1',
                  'https://dexing.sp.anjuke.com/zu/p1', 'https://danjiangkou.sp.anjuke.com/zu/p1',
                  'https://dujiangyan.sp.anjuke.com/zu/p1', 'https://donggang.sp.anjuke.com/zu/p1',
                  'https://dengfeng.sp.anjuke.com/zu/p1', 'https://eerduosi.sp.anjuke.com/zu/p1',
                  'https://enshi.sp.anjuke.com/zu/p1', 'https://ezhou.sp.anjuke.com/zu/p1',
                  'https://enping.sp.anjuke.com/zu/p1', 'https://emeishan.sp.anjuke.com/zu/p1',
                  'https://foshan.sp.anjuke.com/zu/p1', 'https://fz.sp.anjuke.com/zu/p1',
                  'https://fuyang.sp.anjuke.com/zu/p1', 'https://fushun.sp.anjuke.com/zu/p1',
                  'https://fuxin.sp.anjuke.com/zu/p1', 'https://fuzhoushi.sp.anjuke.com/zu/p1',
                  'https://fangchenggang.sp.anjuke.com/zu/p1', 'https://feichengshi.sp.anjuke.com/zu/p1',
                  'https://fengchengshi.sp.anjuke.com/zu/p1', 'https://fengzhen.sp.anjuke.com/zu/p1',
                  'https://fenyang.sp.anjuke.com/zu/p1', 'https://fukang.sp.anjuke.com/zu/p1',
                  'https://fuquan.sp.anjuke.com/zu/p1', 'https://fuqing.sp.anjuke.com/zu/p1',
                  'https://fuan.sp.anjuke.com/zu/p1', 'https://fengcheng.sp.anjuke.com/zu/p1',
                  'https://fuding.sp.anjuke.com/zu/p1', 'https://guangzhou.sp.anjuke.com/zu/p1',
                  'https://gy.sp.anjuke.com/zu/p1', 'https://guilin.sp.anjuke.com/zu/p1',
                  'https://ganzhou.sp.anjuke.com/zu/p1', 'https://guangan.sp.anjuke.com/zu/p1',
                  'https://guigang.sp.anjuke.com/zu/p1', 'https://guangyuan.sp.anjuke.com/zu/p1',
                  'https://ganzi.sp.anjuke.com/zu/p1', 'https://gannan.sp.anjuke.com/zu/p1',
                  'https://guantao.sp.anjuke.com/zu/p1', 'https://guoluo.sp.anjuke.com/zu/p1',
                  'https://guyuan.sp.anjuke.com/zu/p1', 'https://gongzhulingshi.sp.anjuke.com/zu/p1',
                  'https://gaoyou.sp.anjuke.com/zu/p1', 'https://gaomishi.sp.anjuke.com/zu/p1',
                  'https://guangshui.sp.anjuke.com/zu/p1', 'https://gaizhou.sp.anjuke.com/zu/p1',
                  'https://geermu.sp.anjuke.com/zu/p1', 'https://guanghan.sp.anjuke.com/zu/p1',
                  'https://gejiu.sp.anjuke.com/zu/p1', 'https://guiping.sp.anjuke.com/zu/p1',
                  'https://guixi.sp.anjuke.com/zu/p1', 'https://gaoanshi.sp.anjuke.com/zu/p1',
                  'https://gaozhou.sp.anjuke.com/zu/p1', 'https://gaoyaoshi.sp.anjuke.com/zu/p1',
                  'https://gujiao.sp.anjuke.com/zu/p1', 'https://gaobeidian.sp.anjuke.com/zu/p1',
                  'https://hangzhou.sp.anjuke.com/zu/p1', 'https://hf.sp.anjuke.com/zu/p1',
                  'https://heb.sp.anjuke.com/zu/p1', 'https://haikou.sp.anjuke.com/zu/p1',
                  'https://huizhou.sp.anjuke.com/zu/p1', 'https://handan.sp.anjuke.com/zu/p1',
                  'https://huhehaote.sp.anjuke.com/zu/p1', 'https://huanggang.sp.anjuke.com/zu/p1',
                  'https://huainan.sp.anjuke.com/zu/p1', 'https://huangshan.sp.anjuke.com/zu/p1',
                  'https://hebi.sp.anjuke.com/zu/p1', 'https://hengyang.sp.anjuke.com/zu/p1',
                  'https://huzhou.sp.anjuke.com/zu/p1', 'https://hengshui.sp.anjuke.com/zu/p1',
                  'https://hanzhong.sp.anjuke.com/zu/p1', 'https://huaian.sp.anjuke.com/zu/p1',
                  'https://huangshi.sp.anjuke.com/zu/p1', 'https://heze.sp.anjuke.com/zu/p1',
                  'https://huaihua.sp.anjuke.com/zu/p1', 'https://huaibei.sp.anjuke.com/zu/p1',
                  'https://huludao.sp.anjuke.com/zu/p1', 'https://heyuan.sp.anjuke.com/zu/p1',
                  'https://honghe.sp.anjuke.com/zu/p1', 'https://hami.sp.anjuke.com/zu/p1',
                  'https://hegang.sp.anjuke.com/zu/p1', 'https://hulunbeier.sp.anjuke.com/zu/p1',
                  'https://haibei.sp.anjuke.com/zu/p1', 'https://haidong.sp.anjuke.com/zu/p1',
                  'https://hainan.sp.anjuke.com/zu/p1', 'https://hechi.sp.anjuke.com/zu/p1',
                  'https://heihe.sp.anjuke.com/zu/p1', 'https://hexian.sp.anjuke.com/zu/p1',
                  'https://hezhou.sp.anjuke.com/zu/p1', 'https://hailaer.sp.anjuke.com/zu/p1',
                  'https://huoqiu.sp.anjuke.com/zu/p1', 'https://hetian.sp.anjuke.com/zu/p1',
                  'https://huangnan.sp.anjuke.com/zu/p1', 'https://hexi.sp.anjuke.com/zu/p1',
                  'https://huadian.sp.anjuke.com/zu/p1', 'https://heshan.sp.anjuke.com/zu/p1',
                  'https://hailin.sp.anjuke.com/zu/p1', 'https://haicheng.sp.anjuke.com/zu/p1',
                  'https://hunchun.sp.anjuke.com/zu/p1', 'https://huanghua.sp.anjuke.com/zu/p1',
                  'https://hejian.sp.anjuke.com/zu/p1', 'https://hancheng.sp.anjuke.com/zu/p1',
                  'https://huaying.sp.anjuke.com/zu/p1', 'https://houma.sp.anjuke.com/zu/p1',
                  'https://hanchuan.sp.anjuke.com/zu/p1', 'https://huaying2.sp.anjuke.com/zu/p1',
                  'https://heshanshi.sp.anjuke.com/zu/p1', 'https://huixian.sp.anjuke.com/zu/p1',
                  'https://huazhou.sp.anjuke.com/zu/p1', 'https://huozhou.sp.anjuke.com/zu/p1',
                  'https://honghu.sp.anjuke.com/zu/p1', 'https://hongjiang.sp.anjuke.com/zu/p1',
                  'https://helong.sp.anjuke.com/zu/p1', 'https://haimen.sp.anjuke.com/zu/p1',
                  'https://haining.sp.anjuke.com/zu/p1', 'https://haiyang.sp.anjuke.com/zu/p1',
                  'https://jinan.sp.anjuke.com/zu/p1', 'https://jx.sp.anjuke.com/zu/p1',
                  'https://jilin.sp.anjuke.com/zu/p1', 'https://jiangmen.sp.anjuke.com/zu/p1',
                  'https://jingmen.sp.anjuke.com/zu/p1', 'https://jinzhou.sp.anjuke.com/zu/p1',
                  'https://jingdezhen.sp.anjuke.com/zu/p1', 'https://jian.sp.anjuke.com/zu/p1',
                  'https://jining.sp.anjuke.com/zu/p1', 'https://jinhua.sp.anjuke.com/zu/p1',
                  'https://jieyang.sp.anjuke.com/zu/p1', 'https://jinzhong.sp.anjuke.com/zu/p1',
                  'https://jiujiang.sp.anjuke.com/zu/p1', 'https://jiaozuo.sp.anjuke.com/zu/p1',
                  'https://jincheng.sp.anjuke.com/zu/p1', 'https://jingzhou.sp.anjuke.com/zu/p1',
                  'https://jiamusi.sp.anjuke.com/zu/p1', 'https://jiuquan.sp.anjuke.com/zu/p1',
                  'https://jixi.sp.anjuke.com/zu/p1', 'https://jiyuan.sp.anjuke.com/zu/p1',
                  'https://jinchang.sp.anjuke.com/zu/p1', 'https://jiayuguan.sp.anjuke.com/zu/p1',
                  'https://jiangyin.sp.anjuke.com/zu/p1', 'https://jingjiang.sp.anjuke.com/zu/p1',
                  'https://jianyangshi.sp.anjuke.com/zu/p1', 'https://jintan.sp.anjuke.com/zu/p1',
                  'https://jinshi.sp.anjuke.com/zu/p1', 'https://jieshou.sp.anjuke.com/zu/p1',
                  'https://jishou.sp.anjuke.com/zu/p1', 'https://jinghong.sp.anjuke.com/zu/p1',
                  'https://jinjiangshi.sp.anjuke.com/zu/p1', 'https://jianou.sp.anjuke.com/zu/p1',
                  'https://jiangshan.sp.anjuke.com/zu/p1', 'https://jinggangshan.sp.anjuke.com/zu/p1',
                  'https://jiaohe.sp.anjuke.com/zu/p1', 'https://jiaozhoux.sp.anjuke.com/zu/p1',
                  'https://jurong.sp.anjuke.com/zu/p1', 'https://jiande.sp.anjuke.com/zu/p1',
                  'https://jizhoushi.sp.anjuke.com/zu/p1', 'https://jiangyoushi.sp.anjuke.com/zu/p1',
                  'https://km.sp.anjuke.com/zu/p1', 'https://ks.sp.anjuke.com/zu/p1',
                  'https://kaifeng.sp.anjuke.com/zu/p1', 'https://kashi.sp.anjuke.com/zu/p1',
                  'https://kelamayi.sp.anjuke.com/zu/p1', 'https://kenli.sp.anjuke.com/zu/p1',
                  'https://lezilesu.sp.anjuke.com/zu/p1', 'https://kuerle.sp.anjuke.com/zu/p1',
                  'https://kuitun.sp.anjuke.com/zu/p1', 'https://kaili.sp.anjuke.com/zu/p1',
                  'https://kaiping.sp.anjuke.com/zu/p1', 'https://kaiyuan.sp.anjuke.com/zu/p1',
                  'https://kaiyuan2.sp.anjuke.com/zu/p1', 'https://lanzhou.sp.anjuke.com/zu/p1',
                  'https://langfang.sp.anjuke.com/zu/p1', 'https://luoyang.sp.anjuke.com/zu/p1',
                  'https://liuzhou.sp.anjuke.com/zu/p1', 'https://laiwu.sp.anjuke.com/zu/p1',
                  'https://luan.sp.anjuke.com/zu/p1', 'https://luzhou.sp.anjuke.com/zu/p1',
                  'https://lijiang.sp.anjuke.com/zu/p1', 'https://linyi.sp.anjuke.com/zu/p1',
                  'https://liaocheng.sp.anjuke.com/zu/p1', 'https://lianyungang.sp.anjuke.com/zu/p1',
                  'https://lishui.sp.anjuke.com/zu/p1', 'https://loudi.sp.anjuke.com/zu/p1',
                  'https://leshan.sp.anjuke.com/zu/p1', 'https://liaoyang.sp.anjuke.com/zu/p1',
                  'https://lasa.sp.anjuke.com/zu/p1', 'https://linfen.sp.anjuke.com/zu/p1',
                  'https://longyan.sp.anjuke.com/zu/p1', 'https://luohe.sp.anjuke.com/zu/p1',
                  'https://liangshan.sp.anjuke.com/zu/p1', 'https://liupanshui.sp.anjuke.com/zu/p1',
                  'https://liaoyuan.sp.anjuke.com/zu/p1', 'https://laibin.sp.anjuke.com/zu/p1',
                  'https://lingcang.sp.anjuke.com/zu/p1', 'https://linxia.sp.anjuke.com/zu/p1',
                  'https://linyishi.sp.anjuke.com/zu/p1', 'https://linzhi.sp.anjuke.com/zu/p1',
                  'https://longnan.sp.anjuke.com/zu/p1', 'https://lvliang.sp.anjuke.com/zu/p1',
                  'https://linhaishi.sp.anjuke.com/zu/p1', 'https://longhaishi.sp.anjuke.com/zu/p1',
                  'https://lilingshi.sp.anjuke.com/zu/p1', 'https://linqing.sp.anjuke.com/zu/p1',
                  'https://longkou.sp.anjuke.com/zu/p1', 'https://laiyang.sp.anjuke.com/zu/p1',
                  'https://leiyang.sp.anjuke.com/zu/p1', 'https://liyang.sp.anjuke.com/zu/p1',
                  'https://longjing.sp.anjuke.com/zu/p1', 'https://linjiang.sp.anjuke.com/zu/p1',
                  'https://lingyuan.sp.anjuke.com/zu/p1', 'https://linzhoushi.sp.anjuke.com/zu/p1',
                  'https://lingbao.sp.anjuke.com/zu/p1', 'https://lucheng.sp.anjuke.com/zu/p1',
                  'https://lichuan.sp.anjuke.com/zu/p1', 'https://lengshuijiang.sp.anjuke.com/zu/p1',
                  'https://lianyuan.sp.anjuke.com/zu/p1', 'https://langzhong.sp.anjuke.com/zu/p1',
                  'https://luxishi.sp.anjuke.com/zu/p1', 'https://lanxi.sp.anjuke.com/zu/p1',
                  'https://lechang.sp.anjuke.com/zu/p1', 'https://lianjiangshi.sp.anjuke.com/zu/p1',
                  'https://leizhou.sp.anjuke.com/zu/p1', 'https://lufengshi.sp.anjuke.com/zu/p1',
                  'https://lianzhou.sp.anjuke.com/zu/p1', 'https://luoding.sp.anjuke.com/zu/p1',
                  'https://linxiang.sp.anjuke.com/zu/p1', 'https://longquan.sp.anjuke.com/zu/p1',
                  'https://leping.sp.anjuke.com/zu/p1', 'https://laoling.sp.anjuke.com/zu/p1',
                  'https://laizhoushi.sp.anjuke.com/zu/p1', 'https://liuyang.sp.anjuke.com/zu/p1',
                  'https://laohekou.sp.anjuke.com/zu/p1', 'https://laixi.sp.anjuke.com/zu/p1',
                  'https://mianyang.sp.anjuke.com/zu/p1', 'https://maoming.sp.anjuke.com/zu/p1',
                  'https://maanshan.sp.anjuke.com/zu/p1', 'https://mudanjiang.sp.anjuke.com/zu/p1',
                  'https://meishan.sp.anjuke.com/zu/p1', 'https://meizhou.sp.anjuke.com/zu/p1',
                  'https://minggang.sp.anjuke.com/zu/p1', 'https://mishan.sp.anjuke.com/zu/p1',
                  'https://meihekou.sp.anjuke.com/zu/p1', 'https://manzhouli.sp.anjuke.com/zu/p1',
                  'https://mengzhou.sp.anjuke.com/zu/p1', 'https://macheng.sp.anjuke.com/zu/p1',
                  'https://mianzhu.sp.anjuke.com/zu/p1', 'https://mingguang.sp.anjuke.com/zu/p1',
                  'https://miluo.sp.anjuke.com/zu/p1', 'https://nanjing.sp.anjuke.com/zu/p1',
                  'https://nb.sp.anjuke.com/zu/p1', 'https://nc.sp.anjuke.com/zu/p1',
                  'https://nanning.sp.anjuke.com/zu/p1', 'https://nantong.sp.anjuke.com/zu/p1',
                  'https://nanchong.sp.anjuke.com/zu/p1', 'https://nanyang.sp.anjuke.com/zu/p1',
                  'https://ningde.sp.anjuke.com/zu/p1', 'https://neijiang.sp.anjuke.com/zu/p1',
                  'https://nanping.sp.anjuke.com/zu/p1', 'https://naqu.sp.anjuke.com/zu/p1',
                  'https://nujiang.sp.anjuke.com/zu/p1', 'https://nananshi.sp.anjuke.com/zu/p1',
                  'https://ninganshi.sp.anjuke.com/zu/p1', 'https://ningguo.sp.anjuke.com/zu/p1',
                  'https://nankang.sp.anjuke.com/zu/p1', 'https://nanxiong.sp.anjuke.com/zu/p1',
                  'https://nehe.sp.anjuke.com/zu/p1', 'https://nangong.sp.anjuke.com/zu/p1',
                  'https://panzhihua.sp.anjuke.com/zu/p1', 'https://pingdingsha.sp.anjuke.com/zu/p1',
                  'https://panjin.sp.anjuke.com/zu/p1', 'https://pingxiang.sp.anjuke.com/zu/p1',
                  'https://puyang.sp.anjuke.com/zu/p1', 'https://putian.sp.anjuke.com/zu/p1',
                  'https://puer.sp.anjuke.com/zu/p1', 'https://pingliang.sp.anjuke.com/zu/p1',
                  'https://puning.sp.anjuke.com/zu/p1', 'https://pulandian.sp.anjuke.com/zu/p1',
                  'https://pingxiangshi.sp.anjuke.com/zu/p1', 'https://pizhou.sp.anjuke.com/zu/p1',
                  'https://penglaishi.sp.anjuke.com/zu/p1', 'https://pinghu.sp.anjuke.com/zu/p1',
                  'https://pingdu.sp.anjuke.com/zu/p1', 'https://pengzhou.sp.anjuke.com/zu/p1',
                  'https://qd.sp.anjuke.com/zu/p1', 'https://qinhuangdao.sp.anjuke.com/zu/p1',
                  'https://quanzhou.sp.anjuke.com/zu/p1', 'https://qujing.sp.anjuke.com/zu/p1',
                  'https://qiqihaer.sp.anjuke.com/zu/p1', 'https://quzhou.sp.anjuke.com/zu/p1',
                  'https://qingyuan.sp.anjuke.com/zu/p1', 'https://qinzhou.sp.anjuke.com/zu/p1',
                  'https://qingyang.sp.anjuke.com/zu/p1', 'https://qiandongnan.sp.anjuke.com/zu/p1',
                  'https://qianjiang.sp.anjuke.com/zu/p1', 'https://qingxu.sp.anjuke.com/zu/p1',
                  'https://qiannan.sp.anjuke.com/zu/p1', 'https://qitaihe.sp.anjuke.com/zu/p1',
                  'https://qianxinan.sp.anjuke.com/zu/p1', 'https://qiananshi.sp.anjuke.com/zu/p1',
                  'https://qingzhoushi.sp.anjuke.com/zu/p1', 'https://qingzhen.sp.anjuke.com/zu/p1',
                  'https://qionghai.sp.anjuke.com/zu/p1', 'https://qingtongxia.sp.anjuke.com/zu/p1',
                  'https://qinyangshi.sp.anjuke.com/zu/p1', 'https://qufu.sp.anjuke.com/zu/p1',
                  'https://qionglai.sp.anjuke.com/zu/p1', 'https://qidong.sp.anjuke.com/zu/p1',
                  'https://rizhao.sp.anjuke.com/zu/p1', 'https://rikeze.sp.anjuke.com/zu/p1',
                  'https://ruian.sp.anjuke.com/zu/p1', 'https://ruzhoushi.sp.anjuke.com/zu/p1',
                  'https://renqiushi.sp.anjuke.com/zu/p1', 'https://ruijin.sp.anjuke.com/zu/p1',
                  'https://rushan.sp.anjuke.com/zu/p1', 'https://renhuai.sp.anjuke.com/zu/p1',
                  'https://ruichang.sp.anjuke.com/zu/p1', 'https://ruili.sp.anjuke.com/zu/p1',
                  'https://rugao.sp.anjuke.com/zu/p1', 'https://rongchengshi.sp.anjuke.com/zu/p1',
                  'https://shanghai.sp.anjuke.com/zu/p1', 'https://shenzhen.sp.anjuke.com/zu/p1',
                  'https://suzhou.sp.anjuke.com/zu/p1', 'https://sjz.sp.anjuke.com/zu/p1',
                  'https://sy.sp.anjuke.com/zu/p1', 'https://sanya.sp.anjuke.com/zu/p1',
                  'https://shaoxing.sp.anjuke.com/zu/p1', 'https://shantou.sp.anjuke.com/zu/p1',
                  'https://shiyan.sp.anjuke.com/zu/p1', 'https://sanmenxia.sp.anjuke.com/zu/p1',
                  'https://sanming.sp.anjuke.com/zu/p1', 'https://shaoguan.sp.anjuke.com/zu/p1',
                  'https://shangqiu.sp.anjuke.com/zu/p1', 'https://suqian.sp.anjuke.com/zu/p1',
                  'https://suihua.sp.anjuke.com/zu/p1', 'https://shaoyang.sp.anjuke.com/zu/p1',
                  'https://suining.sp.anjuke.com/zu/p1', 'https://shangrao.sp.anjuke.com/zu/p1',
                  'https://siping.sp.anjuke.com/zu/p1', 'https://shihezi.sp.anjuke.com/zu/p1',
                  'https://shunde.sp.anjuke.com/zu/p1', 'https://suzhoushi.sp.anjuke.com/zu/p1',
                  'https://songyuan.sp.anjuke.com/zu/p1', 'https://shuyang.sp.anjuke.com/zu/p1',
                  'https://shizuishan.sp.anjuke.com/zu/p1', 'https://suizhou.sp.anjuke.com/zu/p1',
                  'https://shuozhou.sp.anjuke.com/zu/p1', 'https://shanwei.sp.anjuke.com/zu/p1',
                  'https://sansha.sp.anjuke.com/zu/p1', 'https://shangluo.sp.anjuke.com/zu/p1',
                  'https://shannan.sp.anjuke.com/zu/p1', 'https://shennongjia.sp.anjuke.com/zu/p1',
                  'https://shuangyashan.sp.anjuke.com/zu/p1', 'https://shishi.sp.anjuke.com/zu/p1',
                  'https://sanheshi.sp.anjuke.com/zu/p1', 'https://shangzhi.sp.anjuke.com/zu/p1',
                  'https://shouguang.sp.anjuke.com/zu/p1', 'https://shengzhou.sp.anjuke.com/zu/p1',
                  'https://suifenhe.sp.anjuke.com/zu/p1', 'https://shifang.sp.anjuke.com/zu/p1',
                  'https://sihui.sp.anjuke.com/zu/p1', 'https://shaowu.sp.anjuke.com/zu/p1',
                  'https://songzi.sp.anjuke.com/zu/p1', 'https://shishou.sp.anjuke.com/zu/p1',
                  'https://shaoshan.sp.anjuke.com/zu/p1', 'https://shenzhou.sp.anjuke.com/zu/p1',
                  'https://shahe.sp.anjuke.com/zu/p1', 'https://tianjin.sp.anjuke.com/zu/p1',
                  'https://ty.sp.anjuke.com/zu/p1', 'https://taizhou.sp.anjuke.com/zu/p1',
                  'https://tangshan.sp.anjuke.com/zu/p1', 'https://taian.sp.anjuke.com/zu/p1',
                  'https://taiz.sp.anjuke.com/zu/p1', 'https://tieling.sp.anjuke.com/zu/p1',
                  'https://tongliao.sp.anjuke.com/zu/p1', 'https://tongling.sp.anjuke.com/zu/p1',
                  'https://tianshui.sp.anjuke.com/zu/p1', 'https://tonghua.sp.anjuke.com/zu/p1',
                  'https://taishan.sp.anjuke.com/zu/p1', 'https://tongchuan.sp.anjuke.com/zu/p1',
                  'https://tulufan.sp.anjuke.com/zu/p1', 'https://tianmen.sp.anjuke.com/zu/p1',
                  'https://tumushuke.sp.anjuke.com/zu/p1', 'https://tongcheng.sp.anjuke.com/zu/p1',
                  'https://tongren.sp.anjuke.com/zu/p1', 'https://taiwan.sp.anjuke.com/zu/p1',
                  'https://taicang.sp.anjuke.com/zu/p1', 'https://taixing.sp.anjuke.com/zu/p1',
                  'https://tengzhoushi.sp.anjuke.com/zu/p1', 'https://taonan.sp.anjuke.com/zu/p1',
                  'https://tieli.sp.anjuke.com/zu/p1', 'https://tongxiang.sp.anjuke.com/zu/p1',
                  'https://tianchang.sp.anjuke.com/zu/p1', 'https://wuhan.sp.anjuke.com/zu/p1',
                  'https://wuxi.sp.anjuke.com/zu/p1', 'https://weihai.sp.anjuke.com/zu/p1',
                  'https://weifang.sp.anjuke.com/zu/p1', 'https://wulumuqi.sp.anjuke.com/zu/p1',
                  'https://wenzhou.sp.anjuke.com/zu/p1', 'https://wuhu.sp.anjuke.com/zu/p1',
                  'https://wuzhou.sp.anjuke.com/zu/p1', 'https://weinan.sp.anjuke.com/zu/p1',
                  'https://wuhai.sp.anjuke.com/zu/p1', 'https://wenshan.sp.anjuke.com/zu/p1',
                  'https://wuwei.sp.anjuke.com/zu/p1', 'https://wulanchabu.sp.anjuke.com/zu/p1',
                  'https://wafangdian.sp.anjuke.com/zu/p1', 'https://wujiaqu.sp.anjuke.com/zu/p1',
                  'https://wuyishan.sp.anjuke.com/zu/p1', 'https://wuzhong.sp.anjuke.com/zu/p1',
                  'https://wuzhishan.sp.anjuke.com/zu/p1', 'https://wnelingshi.sp.anjuke.com/zu/p1',
                  'https://wuanshi.sp.anjuke.com/zu/p1', 'https://wugang.sp.anjuke.com/zu/p1',
                  'https://wuchang.sp.anjuke.com/zu/p1', 'https://weihui.sp.anjuke.com/zu/p1',
                  'https://wugangshi.sp.anjuke.com/zu/p1', 'https://wenchang.sp.anjuke.com/zu/p1',
                  'https://wudalianchi.sp.anjuke.com/zu/p1', 'https://wulanhaote.sp.anjuke.com/zu/p1',
                  'https://wuxue.sp.anjuke.com/zu/p1', 'https://wanyuan.sp.anjuke.com/zu/p1',
                  'https://wuchuan.sp.anjuke.com/zu/p1', 'https://wanning.sp.anjuke.com/zu/p1',
                  'https://xa.sp.anjuke.com/zu/p1', 'https://xm.sp.anjuke.com/zu/p1',
                  'https://xuzhou.sp.anjuke.com/zu/p1',
                  'https://xiangtan.sp.anjuke.com/zu/p1', 'https://xiangyang.sp.anjuke.com/zu/p1',
                  'https://xinxiang.sp.anjuke.com/zu/p1', 'https://xinyang.sp.anjuke.com/zu/p1',
                  'https://xianyang.sp.anjuke.com/zu/p1', 'https://xingtai.sp.anjuke.com/zu/p1',
                  'https://xiaogan.sp.anjuke.com/zu/p1', 'https://xining.sp.anjuke.com/zu/p1',
                  'https://xuchang.sp.anjuke.com/zu/p1', 'https://xinzhou.sp.anjuke.com/zu/p1',
                  'https://xuancheng.sp.anjuke.com/zu/p1', 'https://xianning.sp.anjuke.com/zu/p1',
                  'https://xinganmeng.sp.anjuke.com/zu/p1', 'https://xinyu.sp.anjuke.com/zu/p1',
                  'https://bannan.sp.anjuke.com/zu/p1', 'https://xianggang.sp.anjuke.com/zu/p1',
                  'https://xiangxi.sp.anjuke.com/zu/p1', 'https://xiantao.sp.anjuke.com/zu/p1',
                  'https://xilinguole.sp.anjuke.com/zu/p1', 'https://xintaishi.sp.anjuke.com/zu/p1',
                  'https://xinle.sp.anjuke.com/zu/p1', 'https://xiangxiang.sp.anjuke.com/zu/p1',
                  'https://xilinhaote.sp.anjuke.com/zu/p1', 'https://xinji.sp.anjuke.com/zu/p1',
                  'https://xinmin.sp.anjuke.com/zu/p1', 'https://xinghua.sp.anjuke.com/zu/p1',
                  'https://xingping.sp.anjuke.com/zu/p1', 'https://xingyi.sp.anjuke.com/zu/p1',
                  'https://xuanwei.sp.anjuke.com/zu/p1', 'https://xingning.sp.anjuke.com/zu/p1',
                  'https://xiangcheng.sp.anjuke.com/zu/p1', 'https://xinyi.sp.anjuke.com/zu/p1',
                  'https://xiaoyi.sp.anjuke.com/zu/p1', 'https://xingcheng.sp.anjuke.com/zu/p1',
                  'https://xinyishi.sp.anjuke.com/zu/p1', 'https://xingyang.sp.anjuke.com/zu/p1',
                  'https://xinzheng.sp.anjuke.com/zu/p1', 'https://xinmi.sp.anjuke.com/zu/p1',
                  'https://yt.sp.anjuke.com/zu/p1', 'https://yangzhou.sp.anjuke.com/zu/p1',
                  'https://yichang.sp.anjuke.com/zu/p1', 'https://yinchuan.sp.anjuke.com/zu/p1',
                  'https://yangjiang.sp.anjuke.com/zu/p1', 'https://yongzhou.sp.anjuke.com/zu/p1',
                  'https://yulinshi.sp.anjuke.com/zu/p1', 'https://yancheng.sp.anjuke.com/zu/p1',
                  'https://yueyang.sp.anjuke.com/zu/p1', 'https://yuncheng.sp.anjuke.com/zu/p1',
                  'https://yichun.sp.anjuke.com/zu/p1', 'https://yingkou.sp.anjuke.com/zu/p1',
                  'https://yulin.sp.anjuke.com/zu/p1', 'https://yibin.sp.anjuke.com/zu/p1',
                  'https://yiyang.sp.anjuke.com/zu/p1', 'https://yiwu.sp.anjuke.com/zu/p1',
                  'https://yuxi.sp.anjuke.com/zu/p1', 'https://yili.sp.anjuke.com/zu/p1',
                  'https://yangquan.sp.anjuke.com/zu/p1', 'https://yanan.sp.anjuke.com/zu/p1',
                  'https://yingtan.sp.anjuke.com/zu/p1', 'https://yanbian.sp.anjuke.com/zu/p1',
                  'https://yufu.sp.anjuke.com/zu/p1', 'https://yaan.sp.anjuke.com/zu/p1',
                  'https://yangchun.sp.anjuke.com/zu/p1', 'https://yanling.sp.anjuke.com/zu/p1',
                  'https://yichunshi.sp.anjuke.com/zu/p1', 'https://yushu.sp.anjuke.com/zu/p1',
                  'https://yueqing.sp.anjuke.com/zu/p1', 'https://yuzhou.sp.anjuke.com/zu/p1',
                  'https://yongxin.sp.anjuke.com/zu/p1', 'https://yongkangshi.sp.anjuke.com/zu/p1',
                  'https://yushushi.sp.anjuke.com/zu/p1', 'https://yongan.sp.anjuke.com/zu/p1',
                  'https://yidou.sp.anjuke.com/zu/p1', 'https://yizheng.sp.anjuke.com/zu/p1',
                  'https://yanji.sp.anjuke.com/zu/p1', 'https://yangzhong.sp.anjuke.com/zu/p1',
                  'https://yakeshi.sp.anjuke.com/zu/p1', 'https://yining.sp.anjuke.com/zu/p1',
                  'https://yongji.sp.anjuke.com/zu/p1', 'https://yingchengshi.sp.anjuke.com/zu/p1',
                  'https://yizhou.sp.anjuke.com/zu/p1', 'https://yingde.sp.anjuke.com/zu/p1',
                  'https://yumen.sp.anjuke.com/zu/p1', 'https://yucheng.sp.anjuke.com/zu/p1',
                  'https://yuyao.sp.anjuke.com/zu/p1', 'https://yanshishi.sp.anjuke.com/zu/p1',
                  'https://yongcheng.sp.anjuke.com/zu/p1', 'https://yixing.sp.anjuke.com/zu/p1',
                  'https://yicheng.sp.anjuke.com/zu/p1', 'https://yuanjiang.sp.anjuke.com/zu/p1',
                  'https://zhengzhou.sp.anjuke.com/zu/p1', 'https://zh.sp.anjuke.com/zu/p1',
                  'https://zs.sp.anjuke.com/zu/p1', 'https://zhenjiang.sp.anjuke.com/zu/p1',
                  'https://zibo.sp.anjuke.com/zu/p1', 'https://zhangjiakou.sp.anjuke.com/zu/p1',
                  'https://zhuzhou.sp.anjuke.com/zu/p1', 'https://zhangzhou.sp.anjuke.com/zu/p1',
                  'https://zhanjiang.sp.anjuke.com/zu/p1', 'https://zhaoqing.sp.anjuke.com/zu/p1',
                  'https://zaozhuang.sp.anjuke.com/zu/p1', 'https://zhoushan.sp.anjuke.com/zu/p1',
                  'https://zunyi.sp.anjuke.com/zu/p1', 'https://zhumadian.sp.anjuke.com/zu/p1',
                  'https://zigong.sp.anjuke.com/zu/p1', 'https://ziyang.sp.anjuke.com/zu/p1',
                  'https://zhoukou.sp.anjuke.com/zu/p1', 'https://zhangqiu.sp.anjuke.com/zu/p1',
                  'https://zhangjiajie.sp.anjuke.com/zu/p1', 'https://zhucheng.sp.anjuke.com/zu/p1',
                  'https://zhuanghe.sp.anjuke.com/zu/p1', 'https://zhengding.sp.anjuke.com/zu/p1',
                  'https://zhangbei.sp.anjuke.com/zu/p1', 'https://zhangye.sp.anjuke.com/zu/p1',
                  'https://zhaotong.sp.anjuke.com/zu/p1', 'https://weizhong.sp.anjuke.com/zu/p1',
                  'https://zhaoxian.sp.anjuke.com/zu/p1', 'https://zouchengshi.sp.anjuke.com/zu/p1',
                  'https://zunhua.sp.anjuke.com/zu/p1', 'https://zhaodong.sp.anjuke.com/zu/p1',
                  'https://zhangjiagang.sp.anjuke.com/zu/p1', 'https://zhijiang.sp.anjuke.com/zu/p1',
                  'https://zhaoyuanshi.sp.anjuke.com/zu/p1', 'https://zhongxiang.sp.anjuke.com/zu/p1',
                  'https://zixing.sp.anjuke.com/zu/p1', 'https://zhangshu.sp.anjuke.com/zu/p1',
                  'https://zhalandun.sp.anjuke.com/zu/p1', 'https://zhuji.sp.anjuke.com/zu/p1',
                  'https://zhuozhoushi.sp.anjuke.com/zu/p1', 'https://zaoyangshi.sp.anjuke.com/zu/p1',
                  'https://zhangping.sp.anjuke.com/zu/p1', 'https://chengdu.sp.anjuke.com/zu/p1',
                  'https://chengdu.sp.anjuke.com/zu/p1', 'https://chengdu.sp.anjuke.com/zu/p1',
                  'https://nanjing.sp.anjuke.com/zu/p1', 'https://hangzhou.sp.anjuke.com/zu/p1',
                  'https://hangzhou.sp.anjuke.com/zu/p1', 'https://hangzhou.sp.anjuke.com/zu/p1',
                  'https://hangzhou.sp.anjuke.com/zu/p1', 'https://chongqing.sp.anjuke.com/zu/p1',
                  'https://chongqing.sp.anjuke.com/zu/p1', 'https://chongqing.sp.anjuke.com/zu/p1',
                  'https://chongqing.sp.anjuke.com/zu/p1', 'https://chongqing.sp.anjuke.com/zu/p1',
                  'https://chongqing.sp.anjuke.com/zu/p1', 'https://chongqing.sp.anjuke.com/zu/p1',
                  'https://chongqing.sp.anjuke.com/zu/p1', 'https://chongqing.sp.anjuke.com/zu/p1',
                  'https://chongqing.sp.anjuke.com/zu/p1', 'https://chongqing.sp.anjuke.com/zu/p1',
                  'https://dalian.sp.anjuke.com/zu/p1', 'https://jinan.sp.anjuke.com/zu/p1',
                  'https://jinan.sp.anjuke.com/zu/p1', 'https://jinan.sp.anjuke.com/zu/p1',
                  'https://zhengzhou.sp.anjuke.com/zu/p1', 'https://zhengzhou.sp.anjuke.com/zu/p1',
                  'https://cs.sp.anjuke.com/zu/p1', 'https://sjz.sp.anjuke.com/zu/p1',
                  'https://sjz.sp.anjuke.com/zu/p1',
                  'https://sjz.sp.anjuke.com/zu/p1', 'https://qd.sp.anjuke.com/zu/p1', 'https://qd.sp.anjuke.com/zu/p1',
                  'https://xa.sp.anjuke.com/zu/p1', 'https://xa.sp.anjuke.com/zu/p1', 'https://xa.sp.anjuke.com/zu/p1',
                  'https://nb.sp.anjuke.com/zu/p1', 'https://nb.sp.anjuke.com/zu/p1', 'https://hf.sp.anjuke.com/zu/p1',
                  'https://hf.sp.anjuke.com/zu/p1', 'https://hf.sp.anjuke.com/zu/p1', 'https://hf.sp.anjuke.com/zu/p1',
                  'https://fz.sp.anjuke.com/zu/p1', 'https://fz.sp.anjuke.com/zu/p1', 'https://fz.sp.anjuke.com/zu/p1',
                  'https://km.sp.anjuke.com/zu/p1', 'https://km.sp.anjuke.com/zu/p1', 'https://gy.sp.anjuke.com/zu/p1',
                  'https://sy.sp.anjuke.com/zu/p1', 'https://sy.sp.anjuke.com/zu/p1', 'https://nc.sp.anjuke.com/zu/p1',
                  'https://nc.sp.anjuke.com/zu/p1', 'https://cz.sp.anjuke.com/zu/p1', 'https://jx.sp.anjuke.com/zu/p1',
                  'https://yt.sp.anjuke.com/zu/p1', 'https://yt.sp.anjuke.com/zu/p1', 'https://yt.sp.anjuke.com/zu/p1',
                  'https://haikou.sp.anjuke.com/zu/p1', 'https://haikou.sp.anjuke.com/zu/p1',
                  'https://haikou.sp.anjuke.com/zu/p1', 'https://haikou.sp.anjuke.com/zu/p1',
                  'https://haikou.sp.anjuke.com/zu/p1', 'https://haikou.sp.anjuke.com/zu/p1',
                  'https://haikou.sp.anjuke.com/zu/p1', 'https://cc.sp.anjuke.com/zu/p1',
                  'https://sanya.sp.anjuke.com/zu/p1', 'https://sanya.sp.anjuke.com/zu/p1',
                  'https://sanya.sp.anjuke.com/zu/p1', 'https://sanya.sp.anjuke.com/zu/p1',
                  'https://huizhou.sp.anjuke.com/zu/p1', 'https://huizhou.sp.anjuke.com/zu/p1',
                  'https://huizhou.sp.anjuke.com/zu/p1', 'https://jilin.sp.anjuke.com/zu/p1',
                  'https://lanzhou.sp.anjuke.com/zu/p1', 'https://lanzhou.sp.anjuke.com/zu/p1',
                  'https://langfang.sp.anjuke.com/zu/p1', 'https://luoyang.sp.anjuke.com/zu/p1',
                  'https://luoyang.sp.anjuke.com/zu/p1', 'https://luoyang.sp.anjuke.com/zu/p1',
                  'https://luoyang.sp.anjuke.com/zu/p1', 'https://luoyang.sp.anjuke.com/zu/p1',
                  'https://nanning.sp.anjuke.com/zu/p1', 'https://nanning.sp.anjuke.com/zu/p1',
                  'https://nantong.sp.anjuke.com/zu/p1', 'https://nantong.sp.anjuke.com/zu/p1',
                  'https://nantong.sp.anjuke.com/zu/p1', 'https://quanzhou.sp.anjuke.com/zu/p1',
                  'https://quanzhou.sp.anjuke.com/zu/p1', 'https://quanzhou.sp.anjuke.com/zu/p1',
                  'https://quanzhou.sp.anjuke.com/zu/p1', 'https://shaoxing.sp.anjuke.com/zu/p1',
                  'https://taizhou.sp.anjuke.com/zu/p1', 'https://tangshan.sp.anjuke.com/zu/p1',
                  'https://tangshan.sp.anjuke.com/zu/p1', 'https://tangshan.sp.anjuke.com/zu/p1',
                  'https://tangshan.sp.anjuke.com/zu/p1', 'https://tangshan.sp.anjuke.com/zu/p1',
                  'https://weifang.sp.anjuke.com/zu/p1', 'https://weifang.sp.anjuke.com/zu/p1',
                  'https://weifang.sp.anjuke.com/zu/p1', 'https://weifang.sp.anjuke.com/zu/p1',
                  'https://weifang.sp.anjuke.com/zu/p1', 'https://xuzhou.sp.anjuke.com/zu/p1',
                  'https://xuzhou.sp.anjuke.com/zu/p1', 'https://xuzhou.sp.anjuke.com/zu/p1',
                  'https://yangzhou.sp.anjuke.com/zu/p1', 'https://yangzhou.sp.anjuke.com/zu/p1',
                  'https://yangzhou.sp.anjuke.com/zu/p1', 'https://yangzhou.sp.anjuke.com/zu/p1',
                  'https://yichang.sp.anjuke.com/zu/p1', 'https://yichang.sp.anjuke.com/zu/p1',
                  'https://yichang.sp.anjuke.com/zu/p1', 'https://zhenjiang.sp.anjuke.com/zu/p1',
                  'https://zhenjiang.sp.anjuke.com/zu/p1', 'https://binzhou.sp.anjuke.com/zu/p1',
                  'https://dongying.sp.anjuke.com/zu/p1', 'https://taiz.sp.anjuke.com/zu/p1',
                  'https://daqing.sp.anjuke.com/zu/p1', 'https://lianyungang.sp.anjuke.com/zu/p1',
                  'https://huzhou.sp.anjuke.com/zu/p1', 'https://huzhou.sp.anjuke.com/zu/p1',
                  'https://yancheng.sp.anjuke.com/zu/p1', 'https://maanshan.sp.anjuke.com/zu/p1',
                  'https://xuancheng.sp.anjuke.com/zu/p1', 'https://bazhong.sp.anjuke.com/zu/p1']

PROXY_URL = "http://http.tiqu.alicdns.com/getip3?num=20&type=2&pro=0&city=0&yys=0&port=11&pack=28170&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4"


class AnJuKe():

    def __init__(self):
        # super(AnJuKe, self).__init__()
        self._TOPIC_ID = ""  # todo add
        self.REDIS_KEY = 'anjuke_SP_url'
        self.headers = {"User-Agent": ua.random}
        self.r = redis.StrictRedis(host='127.0.0.1', port=6379)

        self.proxies = []
        self.proxy = {}

    def get_proxy(self):
        if not self.proxies:
            resp = requests.get(PROXY_URL).json()
            if isinstance(resp, dict) and resp.get("code") != 0:
                self.logger.info("ProxyError:{}".format(resp.get("msg")))
                print("ProxyError:", resp.get("msg"))
                sys.exit()
            self.proxies = [{"https": "https://" + str(proxy.get("ip")) + ":" + str(proxy.get("port"))} for proxy in
                            resp.get("data")]
        print("current proxy num:", len(self.proxies))
        return random.choice(self.proxies)

    def _save_urls_to_redis(self):
        """
        写入所有待爬取的url
        :return:
        """
        # if not self.user_redis.exists(self.REDIS_KEY):
        if not self.r.exists(self.REDIS_KEY):
            # self.logger.info(u"安居客商铺：url写入中...")
            print(u"安居客商铺：url写入中...")
            for url in area_start_url:
                self.r.sadd(self.REDIS_KEY, url)
            # self.logger.info(u"安居客商铺：url写入完成")
            print(u"安居客商铺：url写入完成")

    def _ban_validate(self, resp):
        """

        :return:
        """
        if u"访问验证-安居客" in resp:
            return True
        else:
            return False

    def _check_next_page(self, content):
        """

        :param resp:
        :return:
        """
        pattern = u'<a href="(.+)" class="aNxt">'
        res = re.findall(pattern, content)
        if res:
            return res[0]
        else:
            return False

    def _get(self, url, headers):
        """
        :param url:
        :param headers:
        :return:
        """
        self.proxy = self.get_proxy()
        print("change ip pre request{}".format(self.proxy))
        h = {}
        if headers:
            for k, v in headers.items():
                h[k] = v
        for k, v in self.headers.items():
            h[k] = v
        try:
            resp = requests.get(url, headers=h, allow_redirects=False, proxies={"https": self.proxy.get("https")},
                                timeout=10)
        except Exception as e:
            print("请求错误", e.args)
            return
        if resp.status_code == 200:
            return resp
        elif resp.status_code == 302:
            self.proxies.remove(self.proxy)
            self.proxy = self.get_proxy()
            return self._get(url, headers)
        else:
            print(u"请求失败:{}".format(url))
            return

    def _paras_list_page_item(self, content):
        """
        :param resp:
        :return:
        """
        # self.logger.info("list page ok")
        if content:
            html = etree.HTML(content)
            return html.xpath("//div[@id='list-content']/div[@class='list-item']")
        else:
            # self.logger.error(u"--------列表页返回错误----------{}".format(resp.text))
            print(u"--------列表页返回错误----------{}".format(content))

    def _save_data(self, url, data):
        """
        数据保存
        :param url:
        :param data:
        :return:
        """
        print(data)
        self.r.sadd("anjuke_SP", str(data))
        # self.save_topic_data(url, data, self._TOPIC_ID)

    def _paras_detail_page(self, items):
        """
        解析详情页  字段:抓取时间.数据来源(安居客/中原地产)/网页url/具体地址/经纬度/租金/租期/面积
        :return:
        """
        for item in items:
            data = {}
            try:
                floor = item.xpath(".//dl/dd/span[2]/text()")[0]
            except Exception as e:
                print(u"安居客商铺：商铺楼层解析错误:%s" % e.args)
                continue
            data["data_from"] = u"安居客"
            page_url = item.xpath("./@link")[0]
            if "1" in floor or u"一" in floor:
                data["url"] = page_url  # 详情url
                print("detail url:{}".format(page_url))
                resp_detail = self._get(url=page_url, headers=self.headers)
                if not resp_detail:
                    continue
                html = etree.HTML(resp_detail.text)
                try:
                    lat = re.search(pattern='lat: "(.+)"', string=resp_detail.text)
                    lng = re.search(pattern='lng: "(.+)"', string=resp_detail.text)
                    if lat and lng:
                        data["lng"] = lng.group(1)  # 经度
                        data["lat"] = lat.group(1)  # 纬度
                    else:
                        data["lng"] = ""
                        data["lat"] = ""
                    data["rent"] = \
                        html.xpath("//div[@id='fy_info']/ul[@class='litem']/li[1]/span[@class='desc']/text()")[
                            0].strip()  # 租金
                    data["desc"] = html.xpath(
                        "//div[@id='fy_info']/ul[@class='litem']/li[3]/span[@class='desc']/text()")[0].strip()  # 租期
                    data["size"] = html.xpath(
                        "//div[@id='fy_info']/ul[@class='ritem']/li[1]/span[@class='desc']/text()")[0].strip()  # 面积
                    data["address"] = html.xpath("//div[@id='fy_info']//span[@class='desc addresscommu']/text()")[0][
                                      1:-1].strip().replace(" ", "")  # 地址
                    self._save_data(url=page_url, data=data)
                    # print(json.dumps(data, skipkeys=True, ensure_ascii=False))
                except Exception as e:
                    print(u"安居客商铺：数据获取失败{}:{}".format(e.args, page_url))
                    continue
            else:
                print("-------------------------floor info:%s-------------------------" % floor)
                if u'其他' in floor or u'商铺/门面/店面' in floor:
                    break  # 楼层信息为其他的情况
                else:
                    continue

    @staticmethod
    def delay():
        """
        用于延时
        :return:
        """
        time.sleep(random.randint(1, 3))

    def start(self):
        self._save_urls_to_redis()
        while self.r.exists(self.REDIS_KEY):
            url = self.r.spop(self.REDIS_KEY).decode('utf-8')

            print("start url:{}".format(url))
            while url:
                resp = self._get(url=url, headers=self.headers)
                items = self._paras_list_page_item(resp.text)
                self._paras_detail_page(items)
                url = self._check_next_page(resp.text)
                print("next page url:{}".format(url))
            print("done,next area url")


if __name__ == '__main__':
    a = AnJuKe()
    a.start()
