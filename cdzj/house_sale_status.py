# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import uuid
from xml.dom.minidom import parseString

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


def getRequestData(paramStr, DSID='CD014AC1-D81F-A263-8F0B-F97E03B30147', UNO='', HNO=''):
    msg.headers = {
        "DSEndpoint": 'my-amf',
        "DSId": DSID
    }
    msg.destination = "SMService"
    msg.operation = "ExecRPC"
    msg.timeToLive = '0'
    msg.timestamp = '0'
    msg.source = None
    msg.clientID = None
    msg.messageId = str(uuid.uuid4()).upper()
    info_type = 'getHouses' if UNO and HNO else 'getHnoAndUnos'
    msg.body = [
        "HouseTableServiceImpl",
        info_type,  # getHnoAndUnos -> 获取hno uno   getHouses -> 获取房屋列表
        {
            "UNO": UNO,
            "HNO": HNO,
            "paramStr": paramStr,
        }
    ]

    req = remoting.Request('null', body=[msg])
    env = remoting.Envelope(amfVersion=pyamf.AMF3)
    env.bodies = [('/2', req)]
    data = bytes(remoting.encode(env).read())
    # 返回一个请求的数据格式
    return data


def getResponse(data):
    # 这个url一定是amf结尾的哦
    url = 'https://zw.cdzj.chengdu.gov.cn/DE-SMServerFx/messagebroker/amf'
    response = requests.post(url, data, headers=headers, verify=False)
    return response.content


def getContent(response, pre_data=1):
    parse_info = remoting.decode(response)
    if pre_data:
        xml_data = parse_info.bodies[0][1].body.body.HOUSETABLETREE

        all_info = parseString(xml_data).childNodes[0].childNodes
        infos = []
        for item in all_info:
            d_info = {}
            d_info['dong'] = item._attrs['label']._value
            uint = item.childNodes
            for u_item in uint:
                d_info[u_item._attrs['label']._value] = {'uno': u_item._attrs['uno']._value,
                                                         'hno': u_item._attrs['hno']._value}
                # info[item._attrs['label']._value] = []
            infos.append(d_info)

        return infos
    else:
        return parse_info


if __name__ == '__main__':
    p = 'PBww38FqaYbB2WYT0z6La+galfqBFlGnutm9AeyIJHm0gQCi48fZHdbyr5iZ/sYq/xrPH55s5qYda8Dq0RecjUj2uNDtvp5ucK6yHogmxQq8qJapoXNEOlCrWQUxAJoojUI0yJ7QmJ9xjeRtEDiaTRASz48/5btYlz0hSGKkCGA='
    pre_data = getContent(getResponse(getRequestData(p)))
    for item in pre_data:
        for key, value in item.items():
            if isinstance(value, dict):
                uno = value.get('uno')
                hno = value.get('hno')
                find_data = getContent(getResponse(getRequestData(p, UNO=uno, HNO=hno)), pre_data=0)
                with open('-'.join([str(uuid.uuid4())  + item.get('dong') + key]) + '.txt', mode='w+', encoding='u8') as fp:
                    fp.write(str(find_data))
                print(pre_data)
