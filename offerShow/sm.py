# coding=utf-8
import os

import requests

base_url = 'https://sm.ms/api/v2'


def get_token():
    user = '32571056@qq.com'
    password = 'scc57295729'
    os.path.join(base_url, '/token')
    resp = requests.post(os.path.join(base_url, '/token'), data={'username': user, 'password': password})
    print(resp.json())


def get_profile(token='wy8a0DJMxmzQNFspd2zmyseefnrJykn1'):
    headers = {
        'Content-Type': 'multipart/form-data',
        'Authorization': token
    }
    resp = requests.post(base_url + '/profile', headers=headers)
    print(resp.text)


def get_history():
    url = base_url + '/history'
    headers = {'format': 'json'
               }
    print(url)
    res = requests.get(url, headers=headers, verify=False)
    print(res.text)


get_history()
