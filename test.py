# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import json
from urllib.parse import unquote

import requests

content = """
D?!F?灇??R9纘R鷫鷸<緳0?蚅?鉓-Oo鲟=?怊e挬阢阷澸j{)I}Z?讱?mNx!D?3踧脅鯠z(Q圹}澨dyy稠泌蒙mg罊?袄S~?祏琿ha糵芃fw挛4橼諿磒绿&??E觱恂YA奩uG"??鎲┞;蕹r??ヵ8檡{X?抳?Fd/$0[渿茂雮儹渴撊r逄\`z胗頵丝I8眖iDL?m|G纃6寙$^w?S€?p襲?璛(x嗶e	龎牚湸?`埃;P峼潞讴C影NⅧ譧? TC錗桊
w鞁	墰?鏀?"偗W黕鬏h?拽脆蝔u#mCi餳?'侍?F,?I掷耔%{!$络雘F殬贎熫Ni:q譢n2F卓: 历榰镌昜h嶗3还v:奏藭苀併K	wA傡cp於?ň??爎腛援??AX恠T??2Sz8玷尫K诸?O飚乔坔
s?唢;f櫆eC0?P3^?>継餘刳,&鐄?慚w肐'銑??\FM钅JG晹i奃S9?|編??気Ri笹殨玲鐚閿%=|獐?
"""
h = " 0a 00 14 16 2c 37 68 55 6c 53 2b 4e 72 6a 4a 38 6c 57 4c 79 35 67 56 64 44 4b 44 51 34 4d 7a 51 77 4e 7a 59 78 4f 44 55 34 4f 54 55 30 4d 6a 6b 34 2c 36 00 40 02 50 3f 6c 0b 1d 00 0c 2d 00 01 02 60 b7 92 2a 94 cc f6 50 68 54 7e a1 55 3b 21 74 c4 75 25 f1 fe 1c 18 80 46 16 51 73 5a 9f 5e 80 2b a3 8e e6 27 e9 ac 3d 43 fd 9a 90 f9 dc 7a a6 5d 72 fc ae 48 7e db 43 b0 42 31 3c fb d1 9d 1c ba 63 ec c2 1f 7f 4a 19 58 23 aa 6a 6c 05 4c de 91 0d 52 71 dd 9d 35 c2 42 93 01 cf 66 e4 4a b9 9a 92 0f a4 e4 40 a2 bc 19 e2 2b fb 51 3e 27 25 55 11 14 81 21 a3 54 92 1c 34 d0 72 ad 2d 5d 5c 5b cc b2 98 5a 4f eb 0b d8 b6 cf fd 76 5b a0 24 d1 e1 50 e1 52 7d 13 06 68 a0 e6 bf 80 1c 2d dc c3 cb 4b fc b5 38 43 af b2 26 c2 b3 c4 ba f3 c2 be 9b a4 ed d1 d6 86 16 a5 60 65 7c e9 83 79 79 4a 6e b3 df 4c eb 4d c7 f9 e1 55 e1 40 ac 8d 4b 76 e2 cf ad 71 d4 48 71 7b ac 8f 1f 66 64 15 67 8d 81 72 fb 0d 18 22 5a ea 79 98 80 c9 22 8f ad 26 b5 d1 fd 3e c8 cd 80 ad 05 90 eb 17 0e d0 a5 2e 88 81 73 21 ff 72 dd 4b df 39 30 09 26 67 1f 7f 6e 1e ba 04 c3 e5 cf db 87 0e a1 17 27 98 e2 f0 29 be b0 3f 16 fc a9 55 84 fa 7d 60 ed 51 57 45 86 0d a1 af 9e 8a e6 e2 b0 55 6f 9c c6 d2 a5 0c 4c 55 56 e5 af 67 94 8f 2f 19 28 36 df 46 c9 78 4d 31 d1 9a b9 18 69 ee 61 0c 19 e3 30 9c 49 bd 6e ca 79 c3 42 f4 6f 6e b4 7e ea ad c5 70 39 9c 92 16 d2 0e 43 09 b6 5e d1 d6 3b 00 48 d4 b3 dc 73 a2 12 7e 90 3f 63 42 35 2c d5 60 4c f4 09 20 90 38 4d 72 91 4f 03 56 1f f0 78 fb cf 80 eb 8d fb a8 98 8b d4 c8 01 f2 8c 1f e7 77 cd 4a 46 cf 11 03 29 8b 69 c9 b5 44 ee 2c 2a 6f f5 c1 04 ac 9e 8d a1 27 7b 65 7f a7 81 e7 28 7e e8 93 37 c0 74 23 c1 c3 43 20 97 ec 3f 7f b1 2d 83 2d ec fb 1a 99 cf 83 67 f1 72 72 f5 b8 4d a3 f9 28 a5 45 c0 b7 ab c1 6e 78 56 88 ed ed 60 f1 05 8f c9 24 29 0a 3b 0a 6c b8 5e 59 05 fe 30 32 fa 8d 05 ca 2b 98 ee 4c 70 8e a8 b1 75 c2 d1 44 c4 67 0e 6c 7d 5e bb 36 97 fd 15 d9 84 13 f5 fa f7 56 b4 8e 37 e1 4e 00 a4 b3 ed ca 62 05 49 3d b4 25 4b 39 c7 4d de 4f c4 bc 9d d5 d8 1f ba 86 dc 16 92 7f f3 08 8e 39 f4 dc 54 18 1c bd 54 c4 2a 98 31 40"
# h = "\x0a\x00\x14\x16\x2c\x37\x68\x55\x6c\x53\x2b\x4e\x72\x6a\x4a\x38\x6c\x57\x4c\x79\x35\x67\x56\x64\x44\x4b\x44\x51\x34\x4d\x7a\x51\x77\x4e\x7a\x59\x78\x4f\x44\x55\x34\x4f\x54\x55\x30\x4d\x6a\x6b\x34\x2c\x36\x00\x40\x02\x50\x3f\x6c\x0b\x1d\x00\x0c\x2d\x00\x01\x02\x60\xb7\x92\x2a\x94\xcc\xf6\x50\x68\x54\x7e\xa1\x55\x3b\x21\x74\xc4\x75\x25\xf1\xfe\x1c\x18\x80\x46\x16\x51\x73\x5a\x9f\x5e\x80\x2b\xa3\x8e\xe6\x27\xe9\xac\x3d\x43\xfd\x9a\x90\xf9\xdc\x7a\xa6\x5d\x72\xfc\xae\x48\x7e\xdb\x43\xb0\x42\x31\x3c\xfb\xd1\x9d\x1c\xba\x63\xec\xc2\x1f\x7f\x4a\x19\x58\x23\xaa\x6a\x6c\x05\x4c\xde\x91\x0d\x52\x71\xdd\x9d\x35\xc2\x42\x93\x01\xcf\x66\xe4\x4a\xb9\x9a\x92\x0f\xa4\xe4\x40\xa2\xbc\x19\xe2\x2b\xfb\x51\x3e\x27\x25\x55\x11\x14\x81\x21\xa3\x54\x92\x1c\x34\xd0\x72\xad\x2d\x5d\x5c\x5b\xcc\xb2\x98\x5a\x4f\xeb\x0b\xd8\xb6\xcf\xfd\x76\x5b\xa0\x24\xd1\xe1\x50\xe1\x52\x7d\x13\x06\x68\xa0\xe6\xbf\x80\x1c\x2d\xdc\xc3\xcb\x4b\xfc\xb5\x38\x43\xaf\xb2\x26\xc2\xb3\xc4\xba\xf3\xc2\xbe\x9b\xa4\xed\xd1\xd6\x86\x16\xa5\x60\x65\x7c\xe9\x83\x79\x79\x4a\x6e\xb3\xdf\x4c\xeb\x4d\xc7\xf9\xe1\x55\xe1\x40\xac\x8d\x4b\x76\xe2\xcf\xad\x71\xd4\x48\x71\x7b\xac\x8f\x1f\x66\x64\x15\x67\x8d\x81\x72\xfb\x0d\x18\x22\x5a\xea\x79\x98\x80\xc9\x22\x8f\xad\x26\xb5\xd1\xfd\x3e\xc8\xcd\x80\xad\x05\x90\xeb\x17\x0e\xd0\xa5\x2e\x88\x81\x73\x21\xff\x72\xdd\x4b\xdf\x39\x30\x09\x26\x67\x1f\x7f\x6e\x1e\xba\x04\xc3\xe5\xcf\xdb\x87\x0e\xa1\x17\x27\x98\xe2\xf0\x29\xbe\xb0\x3f\x16\xfc\xa9\x55\x84\xfa\x7d\x60\xed\x51\x57\x45\x86\x0d\xa1\xaf\x9e\x8a\xe6\xe2\xb0\x55\x6f\x9c\xc6\xd2\xa5\x0c\x4c\x55\x56\xe5\xaf\x67\x94\x8f\x2f\x19\x28\x36\xdf\x46\xc9\x78\x4d\x31\xd1\x9a\xb9\x18\x69\xee\x61\x0c\x19\xe3\x30\x9c\x49\xbd\x6e\xca\x79\xc3\x42\xf4\x6f\x6e\xb4\x7e\xea\xad\xc5\x70\x39\x9c\x92\x16\xd2\x0e\x43\x09\xb6\x5e\xd1\xd6\x3b\x00\x48\xd4\xb3\xdc\x73\xa2\x12\x7e\x90\x3f\x63\x42\x35\x2c\xd5\x60\x4c\xf4\x09\x20\x90\x38\x4d\x72\x91\x4f\x03\x56\x1f\xf0\x78\xfb\xcf\x80\xeb\x8d\xfb\xa8\x98\x8b\xd4\xc8\x01\xf2\x8c\x1f\xe7\x77\xcd\x4a\x46\xcf\x11\x03\x29\x8b\x69\xc9\xb5\x44\xee\x2c\x2a\x6f\xf5\xc1\x04\xac\x9e\x8d\xa1\x27\x7b\x65\x7f\xa7\x81\xe7\x28\x7e\xe8\x93\x37\xc0\x74\x23\xc1\xc3\x43\x20\x97\xec\x3f\x7f\xb1\x2d\x83\x2d\xec\xfb\x1a\x99\xcf\x83\x67\xf1\x72\x72\xf5\xb8\x4d\xa3\xf9\x28\xa5\x45\xc0\xb7\xab\xc1\x6e\x78\x56\x88\xed\xed\x60\xf1\x05\x8f\xc9\x24\x29\x0a\x3b\x0a\x6c\xb8\x5e\x59\x05\xfe\x30\x32\xfa\x8d\x05\xca\x2b\x98\xee\x4c\x70\x8e\xa8\xb1\x75\xc2\xd1\x44\xc4\x67\x0e\x6c\x7d\x5e\xbb\x36\x97\xfd\x15\xd9\x84\x13\xf5\xfa\xf7\x56\xb4\x8e\x37\xe1\x4e\x00\xa4\xb3\xed\xca\x62\x05\x49\x3d\xb4\x25\x4b\x39\xc7\x4d\xde\x4f\xc4\xbc\x9d\xd5\xd8\x1f\xba\x86\xdc\x16\x92\x7f\xf3\x08\x8e\x39\xf4\xdc\x54\x18\x1c\xbd\x54\xc4\x2a\x98\x31\x40"
# print(h.replace(' ', ""))

# print(content.encode().decode())
# print(unquote('%E4%BA%A4%E9%80%9A%E9%93%B6%E8%A1%8C'))
# headers = {
#     "Host": "mbank.95559.com.cn:30013",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Accept": "*/*",
#     "User-Agent": "%E4%BA%A4%E9%80%9A%E9%93%B6%E8%A1%8C/4.0.6 CFNetwork/978.0.7 Darwin/18.5.0",
#     "Accept-Language": "zh-cn",
#     "Content-Length": "674",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "keep-alive",
#
# }
# url = 'http://mbank.95559.com.cn:30013/'
# resp = requests.post(url=url, data=h)
# print(resp.status_code)
# print(resp.content)
s = 'YLPra4XXIDakUzYVvjeQlug%2F9RURJFjKEdnPbUvXhv9Krr%2B4lA1M39EGNu5xm2JobKQilisXcO%2FJYLrY01Jghiuf%2BfN5Qc8S9wYh0sFaLLrPu9u6p%2BlxYooHJRT11fXaZtF8LE%2Bp%2FNCBOyf668kqxVJbcpnibhtE1LGKY%2FJvwnKJqFftk7wTMbAGOk5avbniMUuw8rUhYJuhJ2kntKvSaRPXRx9BvXbnMT5dza3cBA4Unjx1iOQcfrmQiPiYYSVC2fIP75pym%2FCqPtm99FhNCD9hGB8j%2BZKQZ4nRwmSxF00bmYexO%2BhsM27jHk8u%2B5%2FNpy2vrwRQvhdxEClsRmZ4qu1IB%2FcTq%2B5RHxB%2BDwjoW1i5v3DFSGthx60NFUKNNgWgdAGtvngECxj4tUn%2BRuA2FxBG1cETMC1JYLpzvrRjd6j%2FFBKxKQri3np4Ine0GyfqbL58%2FcnAL2eZznK48rtkrtwZ%2Fn1NuL7VIojFD307VO2X7nCM1Fh9D6ArxpcfTVql6C8lZ6kBPF763fvNuXeBAlkoEubUK1kJdopbvzvOfQ2%2Bn5P%2FFT9BA%2Bvqr8ZVJjGSSmJmHcTlb9QCtmuFenLgEVRSdIlzd7u7E9Hru2lBtxXIdCH0oynhdooq%2FGDAdJJmHmwiVRfDBb38yY8vRt4Q8VIUm%2BX6%2Fs6tm%2BxPBdX0cTaGqKfQ7egvyuu1iM%2FSz5YK67FADEqdv2bWSPtVN5MWQH%2Fprz6pItwM7eaOrtyObAhoGEPV9GoR7o82dSMYiXNEFZyIgYt5KYhPHLeXqYJhNfbrM7%2FM882qHpPOpAx6ESntBrEcdleD2SkdNfUKGFCkma%2Ftqxelp6lEIumnyfYdfRfgxFFQv95CzJI3dlLQePI6oYOSGhK1poP9apig92vsl%2FzAkwAXqrC2mrm7WZMgrg%3D%3D'
print(
    s.replace('%20', ' ').replace('%2B', '+').replace('%2F', '/').replace('%3F', '?').replace('%26', '&').replace('%3D',
                                                                                                                  '=').replace(
        '%25', '%').replace('%23', '#'))