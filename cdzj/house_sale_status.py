# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""

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
    "Cookie": "JSESSIONID=B1F1FD3227AA632421F9B01C44AC3D75; FntCookie=TraditionalOrSimplized=0; ASP.NET_SessionId=pygkmqjupi54xr55hehrhm55",
    "Referer": "https://zw.cdzj.chengdu.gov.cn/DE-SMServerFx/FundateClient.swf?t=1&param=dfKr9U7lple67abd5wFvyI52vkx2j%2FvdwKNC2r1C2Tk4%2BpBjAwp%2BqT%2BNJmFaGXgbtQyK5%2FGlb%2FRJcJCg2ZIyJoIlxDrrlrur%2BsPFzKImAbhQoEmW9DnHnWsm0HvtCY4O3xhF0a%2BN5a%2F28vYK8DU%2FA%2FZbcL%2B3PE8C26punMzcYnc%3D",
    "Content-type": "application/x-amf",
    # "Content-length": "519",

}

msg = messaging.RemotingMessage()


def getRequestData():
    msg.headers = {
        "DSEndpoint": 'my-amf',
        "DSId": "299864DE-9F1C-D3BD-9693-6347498D3CEF"
    }
    msg.destination = "SMService"
    msg.operation = "ExecRPC"
    msg.timeToLive = 0
    msg.timestamp = 0
    msg.source = None
    msg.messageId = '45BFC871-AC7A-7099-A7C7-42995FE950C0'
    msg.body = [
                   "HouseTableServiceImpl",
                   "getHouses",
                   {
                       "UNO": 1,
                       "HNO": 8,
                       "paramStr": "dfKr9U7lple67abd5wFvyI52vkx2j/vdwKNC2r1C2Tk4+pBjAwp+qT+NJmFaGXgbtQyK5/Glb/RJcJCg2ZIyJoIlxDrrlrur+sPFzKImAbhQoEmW9DnHnWsm0HvtCY4O3xhF0a+N5a/28vYK8DU/A/ZbcL+3PE8C26punMzcYnc=",
                   }
                   ,

               ],

    req = remoting.Request('null', body=[msg])
    env = remoting.Envelope(amfVersion=pyamf.AMF3)
    env.bodies = [('/2', req)]
    data = bytes(remoting.encode(env).read())
    # 返回一个请求的数据格式
    return data


def getResponse(data):
    # 这个url一定是amf结尾的哦
    url = 'https://zw.cdzj.chengdu.gov.cn/DE-SMServerFx/messagebroker/amf'
    response = requests.post(url, data, headers=headers)
    return response.content


def getContent(response):
    parse_info = remoting.decode(response)

    # total_num = parse_info.bodies[0][1].body.body[3]
    # info = parse_info.bodies[0][1].body.body[0]
    return parse_info


print(getContent(getResponse(getRequestData())))
