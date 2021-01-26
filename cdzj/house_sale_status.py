# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import uuid

import pyamf
import requests
from pyamf import remoting
from pyamf.flex import messaging

headers = {
    "Host": "zw.cdzj.chengdu.gov.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "https://zw.cdzj.chengdu.gov.cn",
    "Connection": "keep-alive",
    "Cookie": "JSESSIONID=FF018C929B24DB26636D2E65195BD3DF; FntCookie=TraditionalOrSimplized=0; ASP.NET_SessionId=pygkmqjupi54xr55hehrhm55",
    "Referer": "https://zw.cdzj.chengdu.gov.cn/DE-SMServerFx/FundateClient.swf?t=1&param=dfKr9U7lple67abd5wFvyI52vkx2j%2FvdwKNC2r1C2Tk4%2BpBjAwp%2BqT%2BNJmFaGXgbtQyK5%2FGlb%2FRJcJCg2ZIyJoIlxDrrlrur%2BsPFzKImAbhQoEmW9DnHnWsm0HvtCY4O3xhF0a%2BN5a%2F28vYK8DU%2FA%2FZbcL%2B3PE8C26punMzcYnc%3D",
    "Content-type": "application/x-amf",
    "Content-length": "519",

}


class HqPara:
    def __init__(self):
        self.source = None


msg = messaging.RemotingMessage(messageId=str(uuid.uuid1()).upper(),
                                clientId=str(uuid.uuid1()).upper(),
                                operation='getHqSearchData',
                                destination='reportStatService',
                                timeToLive=0,
                                timestamp=0)


def getRequestData(page_num, total_num):
    # 请求体第一个参数是查询参数, 第二个是页数,第三个是控制每页显示的数量
    msg.body = [HqPara(), str(page_num), str(total_num)]
    msg.headers['DSEndpoint'] = None
    msg.headers['DSId'] = str(uuid.uuid1()).upper()

    req = remoting.Request('null', body=(msg,))
    env = remoting.Envelope(amfVersion=pyamf.AMF3)
    env.bodies = [('/1', req)]
    data = bytes(remoting.encode(env).read())
    # 返回一个请求的数据格式
    return data


def getResponse(data):
    # 这个url一定是amf结尾的哦
    # url = 'http://jgsb.agri.cn/controller?SERVICE_ID=REGISTRY_JCSJ_MRHQ_SHOW_SERVICE&recordperpage=15&newsearch=true&login_result_sign=nologin'
    url = 'https://zw.cdzj.chengdu.gov.cn/DE-SMServerFx/messagebroker/amf'
    response = requests.post(url, data, headers={'Content-Type': 'application/x-amf'})
    return response.content
