# coding=utf-8

import requests

default_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
}


class CommSession(object):
    def __init__(self, headers=None, verify=True):
        self._session = requests.session()
        if not headers:
            self._session.headers = default_headers
        self._session.verify = verify

    def session(self, index_url=None, cookies=None):
        if cookies:
            self._session.cookies = cookies
        elif not cookies and index_url:
            self._session.get(index_url)
        return self._session
