# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo  价格密文加密  -> 需要先替换 \n  base
"""
import hashlib
import json
import time
import uuid
from copy import deepcopy
from xml.dom.minidom import parseString

import pyamf
import pymongo
import requests
from lxml import etree
from pyamf import remoting
from pyamf.flex import messaging

cnn = pymongo.MongoClient(host='47.105.54.129', port=27017)
db = cnn.shixin
db.authenticate('chean', 'scc57295729')
col = db.house_satatus_gaoxin
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


def base(string: str) -> str:
    oldstr = ''
    newstr = []
    base = ''
    base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                   'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
    # 把原始字符串转换为二进制，用bin转换后是0b开头的，所以把b替换了，首位补0补齐8位
    for i in string:
        oldstr += '{:08}'.format(int(str(bin(ord(i))).replace('0b', '')))
    # 把转换好的二进制按照6位一组分好，最后一组不足6位的后面补0
    for j in range(0, len(oldstr), 6):
        newstr.append('{:<06}'.format(oldstr[j:j + 6]))
    # 在base_list中找到对应的字符，拼接
    for l in range(len(newstr)):
        base += base64_list[int(newstr[l], 2)]
    # 判断base字符结尾补几个‘=’
    if len(string) % 3 == 1:
        base += '=='
    elif len(string) % 3 == 2:
        base += '='
    return base


def getRequestData(paramStr, DSID='CD014AC1-D81F-A263-8F0B-F97E03B30147', UNO='', HNO=''):
    msg.headers = {
        "DSEndpoint": 'my-amf',
        "DSId": str(uuid.uuid4()).upper()
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
    response = requests.post(url, data, headers=headers)
    return response.content


def getContent(response, pre_data=1, list_data={}):
    parse_info = remoting.decode(response)
    try:
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
            items = parse_info.bodies[0][1].body.body.HOUSEITEMLIST
            for item in items:
                final_data = {}
                final_data["isMortgage"] = item.get('isMortgage')
                final_data["isSealed"] = item.get('isSealed')
                final_data["roomNo"] = item.get('roomNo')
                final_data["isSealUp"] = item.get('isSealUp')
                final_data["usage"] = item.get('usage')
                final_data["typeHouse"] = item.get('typeHouse')
                final_data["isDebted"] = item.get('isDebted')
                final_data["listWaterPrice"] = item.get('listWaterPrice')
                final_data["maxArea"] = item.get('maxArea')
                final_data["tableid"] = item.get('tableid')
                final_data["floorNo"] = item.get('floorNo')
                final_data["minArea"] = item.get('minArea')
                final_data["status"] = item.get('status')
                final_data["totalArea"] = item.get('totalArea')
                final_data.update(list_data)
                final_data.pop('paramsStr')
                save_data(final_data)
            return parse_info
    except Exception as e:
        print(e)
        return []


def save_data(data):
    temp = deepcopy(data)
    temp.pop('listWaterPrice')
    data_str = json.dumps(temp, ensure_ascii=False).encode('u8')
    m = hashlib.md5()
    m.update(data_str)
    _md5 = m.hexdigest()
    data['_md5'] = _md5
    col.update({"_md5": _md5}, data, True)


def get_list_page(page=1, __VIEWSTATE=''):
    index_url = 'https://zw.cdzj.chengdu.gov.cn/SCXX/Default.aspx?action=ucSCXXShowNew2'
    et = 'ID_ucSCXXShowNew2$UcPager1$btnPage1' if page == 0 else 'ID_ucSCXXShowNew2$UcPager1$btnNewNext'
    post_data = {
        "__EVENTTARGET": et,
        "__EVENTARGUMENT": '',
        "__VIEWSTATE": __VIEWSTATE,
        "__VIEWSTATEGENERATOR": "F35F1EA5",
        "ID_ucSCXXShowNew2$txtpId": "",
        "ID_ucSCXXShowNew2$txtpName": "",
        "ID_ucSCXXShowNew2$ddlRegion": "高新区",
        "ID_ucSCXXShowNew2$txtTime1": "",
        "ID_ucSCXXShowNew2$txtTime2": "",
        "ID_ucSCXXShowNew2$UcPager1$txtPage": str(page),
    }
    header = {
        "Host": "zw.cdzj.chengdu.gov.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://zw.cdzj.chengdu.gov.cn/SCXX/Default.aspx?action=ucSCXXShowNew2",
        "Connection": "keep-alive",

    }
    resp = requests.post(index_url, headers=header, data=post_data)
    return resp


def parse_list(resp):
    list_data = []
    html = etree.HTML(resp.text)
    view_site = html.xpath('string(//input[@id="__VIEWSTATE"]/@value)')
    trs = html.xpath("//table[@id='ID_ucSCXXShowNew2_gridView']//tr[position()>1]")
    for tr in trs:
        data = {}
        keys = ['presell_no', 'project_name', 'area', 'project_addr', 'use', 'developer',
                'presell_size', 'presell_date', 'agency', 'supervise_bank', 'remark']
        for index, key in enumerate(keys):
            data[key] = ''.join(tr.xpath('string(./td[{}])'.format(index + 1))).strip()
        data['paramsStr'] = tr.xpath('string(./td[12]/a/@href)').split('param=')[-1]
        list_data.append(data)
    return list_data, view_site


if __name__ == '__main__':
    vs = ''
    for page in range(0, 118):  # 1770
        resp = get_list_page(page, vs)
        list_datas, vs = parse_list(resp)
        for list_data in list_datas:
            time.sleep(20)
            referer, p = ''.join('https://zw.cdzj.chengdu.gov.cn/DE-SMServerFx/FundateClient.swf?t=1&param={}'.format(
                list_data.get('paramsStr'))), list_data.get('paramsStr')
            pre_data = getContent(getResponse(getRequestData(p)))
            for item in pre_data:
                list_data['house_num'] = item.get('dong')
                for key, value in item.items():
                    if isinstance(value, dict):
                        list_data['unit'] = key
                        uno = value.get('uno')
                        hno = value.get('hno')
                        find_data = getContent(getResponse(getRequestData(p, UNO=uno, HNO=hno)), pre_data=0,
                                               list_data=list_data)


"""
----RSA 解密价格  listWaterPrice
package c
{
   import com.hurlant.crypto.rsa.RSAKey;
   import mx.utils.Base64Decoder;
   import flash.utils.ByteArray;
   
   public class R extends Object
   {
      
      private static var rsa:RSAKey = null;
       
      public function R()
      {
         super();
      }
      
      public static function decode(encodedB64:String) : String
      {
         var N:String = null;
         var E:String = null;
         var D:String = null;
         var P:String = null;
         var Q:String = null;
         var DMP1:String = null;
         var DMQ1:String = null;
         var IQMP:String = null;
         if(rsa == null)
         {
            N = "9c2e6c195b482f28453f2bdf36d8016fac9c7dfbbd9493c9abbee2eaef080b39a56e8d3aab6f7d50827041bd09624a658706c949668320a28c2cdf4310dccbfb7021002b6079854bf25a52fe99087a5d898236116d1db9f93c75237d6b56c6172859bce759ffce500c4f30c780c9b3dd5dfff42dafa367638b956c09a26335c1";
            E = "10001";
            D = "6cc28f18a14e85385ff07bd6b75478bb91d270910c16194c894326b63fbab4467283a7e9c154a4499a6c1dfb4c3b9c5f53465089c2cf71bc802d0754a6bb7b78087c3a232ed165768d2898a900183a788d8a85eea130a079ece9b7d07839918ae46830f73108e27e85590f9ba69395d9d455f4b71012c327518250ad60b5d0f9";
            P = "d0fdd6eea2f6f3a8b25d66fb133d50413598b86a9a5f205cc97e02593a38d5c49602f7ab2495f46343aa8c694f8ae5067ad1965a0902e1497ab725841559ebbb";
            Q = "bf4fa989b201f1d6a970012cae0cfb478231c98753732acfdb500b82b87879a3199315f7f435b8739c7a351e7dce61fcc8811384fb1522b418602a2f56a706b3";
            DMP1 = "28d7f3116037f3169d0534030d9785ffb881c848cd329a188828603d1febcb9b47d5fca12ddd408dc5c3a6fd4dd64f3c1cf4a8f59f9d387a2bc96f438908b1d1";
            DMQ1 = "a7bafd66a7360345746aa9ecf5709642dcc82febc0e3814e99f6f5109811b07baa2986224def67979d429c1deea92aca0934f9db2694224809f30e2950ecc1f7";
            IQMP = "8e37f816f3b08e1078fb267bb16171cc3ea93d8be87f9fdd9b7b2b1779430e9ac8fb71f326550f7df79c5ba85136546f034b5cbe39784f209b328f262797c50d";
            rsa = RSAKey.parsePrivateKey(N,E,D,P,Q,DMP1,DMQ1,IQMP);
         }
         var base64de:Base64Decoder = new Base64Decoder();
         base64de.decode(encodedB64);
         var src:ByteArray = base64de.toByteArray();
         var dst2:ByteArray = new ByteArray();
         rsa.decrypt(src,dst2,src.length);
         return dst2.toString();
      }
   }
}


"""


"""
--- base64 编码
package mx.utils
{
   import flash.utils.ByteArray;
   import mx.resources.IResourceManager;
   import mx.resources.ResourceManager;
   
   [ResourceBundle("utils")]
   public class Base64Decoder extends Object
   {
      
      private static const ESCAPE_CHAR_CODE:Number = 61;
      
      private static const inverse:Array = [64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,62,64,64,64,63,52,53,54,55,56,57,58,59,60,61,64,64,64,64,64,64,64,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,64,64,64,64,64,64,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64];
       
      private var count:int = 0;
      
      private var data:ByteArray;
      
      private var filled:int = 0;
      
      private var work:Array;
      
      private var resourceManager:IResourceManager;
      
      public function Base64Decoder()
      {
         this.work = [0,0,0,0];
         this.resourceManager = ResourceManager.getInstance();
         super();
         this.data = new ByteArray();
      }
      
      public function decode(encoded:String) : void
      {
         var c:* = NaN;
         for(var i:uint = 0; i < encoded.length; i++)
         {
            c = encoded.charCodeAt(i);
            if(c == ESCAPE_CHAR_CODE)
            {
               this.work[this.count++] = -1;
               addr80:
               if(this.count == 4)
               {
                  this.count = 0;
                  this.data.writeByte(this.work[0] << 2 | (this.work[1] & 255) >> 4);
                  this.filled++;
                  if(this.work[2] == -1)
                  {
                     break;
                  }
                  this.data.writeByte(this.work[1] << 4 | (this.work[2] & 255) >> 2);
                  this.filled++;
                  if(this.work[3] == -1)
                  {
                     break;
                  }
                  this.data.writeByte(this.work[2] << 6 | this.work[3]);
                  this.filled++;
               }
            }
            else if(inverse[c] != 64)
            {
               this.work[this.count++] = inverse[c];
               §§goto(addr80);
            }
         }
      }
      
      public function drain() : ByteArray
      {
         var result:ByteArray = new ByteArray();
         var oldPosition:uint = this.data.position;
         this.data.position = 0;
         result.writeBytes(this.data,0,this.data.length);
         this.data.position = oldPosition;
         result.position = 0;
         this.filled = 0;
         return result;
      }
      
      public function flush() : ByteArray
      {
         var message:String = null;
         if(this.count > 0)
         {
            message = this.resourceManager.getString("utils","partialBlockDropped",[this.count]);
            throw new Error(message);
         }
         return this.drain();
      }
      
      public function reset() : void
      {
         this.data = new ByteArray();
         this.count = 0;
         this.filled = 0;
      }
      
      public function toByteArray() : ByteArray
      {
         var result:ByteArray = this.flush();
         this.reset();
         return result;
      }
   }
}



"""