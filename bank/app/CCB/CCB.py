# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:
@Todo
"""
import random
import time
import traceback
from urllib.parse import urljoin

import requests

from bank.utils.utils import CommSession, content2tree

HEADERS = {
    "User-Agent": "ICBCiPhoneBSNew F-WAPB 3.0.1.3 fullversion:3.0.1.3 newversion:5.1.0.4.0 iPhone10,3 12.2 CE95C2AC-3C65-4FAA-9634-9A59CFE4E2D5 4G Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 BSComponentVersion:5.1",
}
URLS = [
    "https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_13_MB?SYS_CODE=0760&MP_CODE=02&SEC_VERSION=4.1.61&APP_NAME=com.ccb.ccbDemo&SKEY=&GLOBAL_SKEY=&ccbParam=YLPra4XXIDakUzYVvjeQlug%2F9RURJFjKEdnPbUvXhv9Krr%2B4lA1M39EGNu5xm2JobKQilisXcO%2FJYLrY01Jghiuf%2BfN5Qc8S9wYh0sFaLLrPu9u6p%2BlxYooHJRT11fXaZtF8LE%2Bp%2FNCBOyf668kqxVJbcpnibhtE1LGKY%2FJvwnKJqFftk7wTMbAGOk5avbniMUuw8rUhYJsxRS%2BuRyhh3wQdGQ0Dxxqo0CVYohWdRmZ3H9%2BIg58zpMrr3LAkMK7RTGaYJ2HaJ2X2Ka9E5ng61P74zVQx5Y4vvjTGuF5H8nd4HNrP%2BxS3AvMOO3k9nJHrKY4ulhW1ynUXx1X7gEAm4RWtIwQe5%2BhwdL8s0V29qm8C2Gl1KM60C7vP4O9zkJviZmvOgkGm7%2FJ32R%2Ft6RZqcJN7vZJ3lHn9FzsmZYQ2prFXA3n8qCOGah%2BCCSImL0qh4ZLAxNeera7Q3rdXkDZKZYhTvOQwM344l%2BBArmBmnyeC25xMUmbHfAUEA9ByaGcCNTDGPkz%2FV8oIjzfTmfLOXITrSYmsgkdcV0IOCFZeTuHFfOonPBSiE7YGxGiKq2p0VThKdM86BHBShwdtTME6YjWvBW1R0bwUOCU3FyidVnVTlNlyebSG%2Fbv9hMIPW0ukM2TXn9SwC97mHUNLLa4%2BVn5GXAYDT%2FX60gbbS8Alnlln0xiHRBn38EF5755D%2FAywkTm4v89mGFmRqwGdGajoeucOmvN5X4C%2BVx%2BLqOmt2w1wNyLTC0v3bRgjFd%2B2JhXep2mjL5CP86obAGd3FmtwoqLMbYM40DdsPRHKMqX5gZ1psrGN2gGxtiNXQEFnSitZvAWC7%2B%2BQaBxaLCItqr8F35uBp9qPAB47%2FNPIC%2FlibYMXwlDeVlRPXS16%2BP4qrXBlf4N9grZdGU8Ai8lRsq7tgQ%3D%3D",
    "https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_13_MB?SYS_CODE=0760&MP_CODE=02&SEC_VERSION=4.1.61&APP_NAME=com.ccb.ccbDemo&SKEY=&GLOBAL_SKEY=&ccbParam=YLPra4XXIDakUzYVvjeQlug%2F9RURJFjKEdnPbUvXhv9Krr%2B4lA1M39EGNu5xm2JobKQilisXcO%2FJYLrY01Jghiuf%2BfN5Qc8S9wYh0sFaLLrPu9u6p%2BlxYooHJRT11fXaZtF8LE%2Bp%2FNCBOyf668kqxVJbcpnibhtE1LGKY%2FJvwnKJqFftk7wTMbAGOk5avbniMUuw8rUhYJsxRS%2BuRyhh32wsWci5VFkfEHejJZjAYsiKJcVcjQX3nvkjYODLsLvzrNMnphBtuXH4kjdAEpBqNsXgVfdhZDetsnsOM4IdovWL0oO3dsAcH8eGgCYjz%2BIy73ic7WQiyQH0aM%2FM%2Fz2WHJ2KRLADyEQ8xaXtqQR1ZboGL8Z%2FTV%2FMGgugjhi6DE%2FlmllU2Qf%2BUUPlF%2BDonWZ1jWy%2BdbeGSanVCBjGBiJ5H4OtA0fHd6TS4BywHP7ffEqtSquJ8222VK8bdZphznC7BNcdCmV9tT63Wb3bTSZD8xVTK9B%2FEkPWVZq8PadpADF0bAFZ4l78TYo9HGceE0IVvxbHmhMmWlgchwXSGpmzHCe8W8MRghfJmssHJUDK6cSjKe3htJ7YC0upqYgUb3lBZY4Y%2FS9utiVclGSxvfXKS0LiVVOQ9RcfrqEWYiDdcqxNlNCVsHvdJufbFl%2BlxyMO3IdFNALJgbbE5AtTbioR8Z76E8MuguJt9Nd8yCIUd2wPfCPuhzChuocjvxaTxfiNh9Yo4t1ObLwTJKxwdXDrQAP6c2KNYZY5kRzGcdz1%2FE%2BoFy05iZ1h5Gf4uqkWMwAj4sqdv1Uor02ZtEse6h31Mxu7RP1pl0zit4W2V1FFil%2F0i6uTmCvOR1ZgFA%2BZ4zimE0LDYYEf4CmgHVbIpk7AZ3RXJrq9%2BZFai9XBZOS%2FdFABLgngYsFCrbD3nwSZN9xQLA%3D%3D",
    "https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_13_MB?SYS_CODE=0760&MP_CODE=02&SEC_VERSION=4.1.61&APP_NAME=com.ccb.ccbDemo&SKEY=&GLOBAL_SKEY=&ccbParam=YLPra4XXIDakUzYVvjeQlug%2F9RURJFjKEdnPbUvXhv9Krr%2B4lA1M39EGNu5xm2JobKQilisXcO%2FJYLrY01Jghiuf%2BfN5Qc8S9wYh0sFaLLrPu9u6p%2BlxYooHJRT11fXaZtF8LE%2Bp%2FNCBOyf668kqxVJbcpnibhtE1LGKY%2FJvwnKJqFftk7wTMbAGOk5avbniMUuw8rUhYJsxRS%2BuRyhh37CSeWsg6najFhxE4LoR0dLn9iCEiKNeQzK%2FtWL3EwJhEyC0JFIpxTe39fTl5EE8MEB55o%2BQx1RXTdy9meexG4WQLy%2BeKkeLHlWXN8UJcWHUPPdNmrV%2FdcRw01f%2BHGyZW9Cjs%2BU14cFw0zHVOL4q2r0jCnJc4yCGyN86V7O13Kizg%2BQnoolcFJnZAH8GnQE9HImsO%2FtOkJkgs5Zwwi%2FUhR%2B8BcOoeKcC6%2FRsDdB2j7sbRXK1EWXr3c%2FCKHchgn84H0u0gXV8CSY4w%2BIpyjNhXcekUlYeYfv39io3ioKPlUCoqUvwZv8lKeOt2KvNXyFpfSAxfbJcWa6w8YgDIBwAdSH%2FqOZc%2Ft8CXTDuwxLDdUIUa%2BBtxmp6YUx%2FR626mxrbOSI0OuLoQWLayG6L3KiZZ47RA25jhBR7N5Fb67NpgAYe5%2BPVO2EIbV2oyn6OKTq3%2F6Y09jJt5IhTTKDZVYWdXVh5TMu%2BnTWD2uWsZrUl64sXaCX6MnK%2FDMLNkO%2FysPbmhqaLc7AeWFTsHDXxfSLf9Cet9GFCWR1bPBciaLa1gafnxWEOLP5RbPnyveA%2FCtWrtgyGv5W6q36paCemKsMQ9I%2F6j8EgKEVP%2BhyRdKRl54M9CgF6asS4mYeXRQWeR0oJe%2FSz2e5IL9r0Vw50jpoyzWN007oytcepeww1xDSLfjinqFcuHqXDuARFmPRffigBkg%3D%3D",
    "https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_13_MB?SYS_CODE=0760&MP_CODE=02&SEC_VERSION=4.1.61&APP_NAME=com.ccb.ccbDemo&SKEY=&GLOBAL_SKEY=&ccbParam=YLPra4XXIDakUzYVvjeQlug%2F9RURJFjKEdnPbUvXhv9Krr%2B4lA1M39EGNu5xm2JobKQilisXcO%2FJYLrY01Jghiuf%2BfN5Qc8S9wYh0sFaLLrPu9u6p%2BlxYooHJRT11fXaZtF8LE%2Bp%2FNCBOyf668kqxVJbcpnibhtE1LGKY%2FJvwnKJqFftk7wTMbAGOk5avbniMUuw8rUhYJsxRS%2BuRyhh3%2BtK0VY7mZzpDFUlkH5XpClaLc5Ox%2BfOMti31J1xSjr5SCEUxZS6QjDP6XHG6ODbykeWwyCJIhqa1MEl6CWUMSu%2FrYidl4iHuw4Pr5oljJpedeme4O8IXnBEYZHogBJumTF0gfVjb%2F6dc1m8XAoDY0oRg2mw6oOhR%2Fztvk3C1PVOqTcF55SPskBDElf7VhJ1jXPcll39gNRGgGfiQapQHsM8S5Z%2B2G6I6YoSmDJn0Oxb8CAVCLNsqfq7%2F8JEUIzyxceeCakfG3uiEkmoaZahHN0q10RYqsM8OYU86G5%2BozsSwVA%2BrfZzjqERrqHV%2B7Wrfo4Ojv7iMnCVIPiAWuQDBrpQXrqfvjoOpxrGGkmPw4uRQ23%2Bw3NU5OGdkrvMdk8acySD%2Bwkltisqsver8MycFbaSmpjc8kP72yvFvX7tL097qxgnT4nPNPK%2F0OI2BQOh4up7%2FaE3f0Ul%2FaMtMw1SiYRIBzbQ%2BZK83B1Z%2FyVyXxGgpXofla9kbCs1UNnDJ2wHo2ekqJgSxQL5ZskaXpR1IjpprbiZ69MMIXUxHVcPcUBP7XqLko4Vk1lda44VwcUdFnOyaq8%2FXbr4tPSUPHVMiv5xyKvSHTZy4zFULamvoJje7J1UICy8ttNehknBvSo5uuJ1kyowj7uojCgEz6ycv5xwA2r8dJr0mEaYSJoa0kFFUmQb8fcoZfA9hNytwUrQFg%3D%3D",
    "https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_13_MB?SYS_CODE=0760&MP_CODE=02&SEC_VERSION=4.1.61&APP_NAME=com.ccb.ccbDemo&SKEY=&GLOBAL_SKEY=&ccbParam=YLPra4XXIDakUzYVvjeQlug%2F9RURJFjKEdnPbUvXhv9Krr%2B4lA1M39EGNu5xm2JobKQilisXcO%2FJYLrY01Jghiuf%2BfN5Qc8S9wYh0sFaLLrPu9u6p%2BlxYooHJRT11fXaZtF8LE%2Bp%2FNCBOyf668kqxVJbcpnibhtE1LGKY%2FJvwnKJqFftk7wTMbAGOk5avbniMUuw8rUhYJsxRS%2BuRyhh322kS4qpHQXq1LEGs1tKYbL5s48Jk2WAl75kWeH%2Bmlzo6gLA599WrnCMnNOkvihaSUwUlrzdVSEKRejHF1cv0Sbg%2Fs%2FXo%2Fb7Qjew6o7j7UOblSovmyUUeauepCRddj5w1Bpm8gvPHP0iVb3jquoDoL0T50Mcw3yk1NlU6uJQIMLP5EZ7FQwtbXn1mPkZ44CPnkGr8frn2TXOLuSUli8e5S75GYLbvHROu0V9MrguzSrF9IAHy%2BZPnX6jlMEGrCSFbhPHBypZwyAeoSLA8Jra247AoTvmdqP8jICa%2FiuBpTysCG04wEIuZr6aTy0AiL4sK4i5IStYw%2B8M9KhPeQQ68KoaYrwLMOJP2dpxI5iBldaTtioBhslzrX4PHJ2w7iq%2F6gBlclf5OHpHtafN7wsZnMAcxXmdD4oB%2BdIdEV9zYPkRPc7gX%2FymHkiwwGQ0BFxHY0wutQo65h91cDu8t5zGu0AedDSG%2FLo%2B9gzoTBC3Q3XCjm0O%2FoIDcmkc7cPpcKeHHgKW0NbIhqDjX197Q4XJgemaI5lByCiDFfgXIykiE22T03UirsZZ2qCntQJwu%2BX1UMpXtPTGKXIKRZ%2BUnMXIUd8BFoje3Q7zriFN6rx7cFmykgvBIyS5K5Md3mdVV9dz1jpnr0jHuhctjRoNWZbC2PG%2FpukgFo75kO6bLchhN7ciMqf8WbuSedz6lwulwiRcLQ%3D%3D",
    "https://ibsbjstar.ccb.com.cn/CCBIS/B2CMainPlat_13_MB?SYS_CODE=0760&MP_CODE=02&SEC_VERSION=4.1.61&APP_NAME=com.ccb.ccbDemo&SKEY=&GLOBAL_SKEY=&ccbParam=YLPra4XXIDakUzYVvjeQlug%2F9RURJFjKEdnPbUvXhv9Krr%2B4lA1M39EGNu5xm2JobKQilisXcO%2FJYLrY01Jghiuf%2BfN5Qc8S9wYh0sFaLLrPu9u6p%2BlxYooHJRT11fXaZtF8LE%2Bp%2FNCBOyf668kqxVJbcpnibhtE1LGKY%2FJvwnKJqFftk7wTMbAGOk5avbniMUuw8rUhYJsxRS%2BuRyhh39YgG1J8wkxrsNHyofs4lh07SreJMpxYww4Pw7v1wN5w2F2PFpq%2F2xrM%2BjAa0WbPgcc%2F%2FHNSCCODRiH6SCq2z6TF8TxmBGnL2pY%2FOzQqTaC7rNdYocvpCAbsyrkN6SPaNJEQ1PrqOZ4CmM5sMO9wmmVnagCZyCzNYm9G0m4zZYiUKcMY7neFLrKnlhwqJzZP5tMTOqiHdbN6ObH5wvUf8ik4Y8jhJS5GWSWWYea97jJ9bAhvqT3Rci%2BhqagzD8cbBJHbGYSandRzrs44Y2wt887OQs5wQaswFa8OCmY33BtvLY7C53l49BgGTDFPgbbEXxTt6ygM%2Fo96gHDaYliqem4W2kv8tzXb7RRmM%2FH5UmOWDzq4NFg7h4pJSRtlo287pRYTrbxt5f%2FenITk6J2DJHOSK6mgjvPZpBX3rj%2FzNVqsp0OlXyRWas%2FLcirLTbhZW5H11qw1Yo8LcT%2B3l%2Bo7ZAUNpcCCmVEL2bEvrFZYPtEUldU0VkWIv5x%2FdCoP0p1kH1qa3UEJaDxmeCxX5FrkO%2FgiuuXgYUa2AmGI7Joqfy66K90qAOygj38vQdU%2FTGsmFJvpjJOZEtUlRWaJtmUymyS%2FVHErvwlR2QwQW%2BUnxaskzoZ%2BkvwNTQYaw4J36s1dzFugvEFzNjCcs2GZvYmCVtlKFxs8ynD8LzVNTNHrZi9L8m4Fmn5q5dbIcrsD41zMAw%3D%3D",
]


class CCB(object):
    def __init__(self):
        self.index = 'http://finance.ccb.com/cn/'
        self.session = self.instance_session()

    def instance_session(self):
        return CommSession(verify=False, headers=HEADERS).session()

    def _get(self, url, timeout=30, method='get', data=None, retry=3):
        """
        网页下载
        :param url:
        :return:resp
        :rtype: requests.Response
        """
        for _ in range(retry):
            try:
                time.sleep(random.randint(3, 5))
                if method == 'get':
                    resp = self.session.get(url=url, timeout=timeout, params=data)
                elif method == 'post':
                    resp = self.session.post(url=url, data=data, allow_redirects=True, timeout=timeout)
                else:
                    raise ValueError('request method not support')
            except requests.exceptions:
                continue
            if resp.status_code // 100 == 2:
                return resp
        raise traceback.format_exc()

    def get_file_url(self, url: str):
        """

        :param url:
        :return:
        """
        if url and url.endswith('html'):
            try:
                html = content2tree(self._get(url))
            except requests.exceptions as ex:
                print(ex)
                return url
            res = html.xpath('//div[@class=\'content f14\']/p/a/@href')
            return urljoin(self.index, res[0]) if res else ''
        elif url.endswith('.pdf'):
            return url
        else:
            return url

    def purchase_amount(self, data):
        info = data.get('Txn_Num_GRP', [])
        for item in info:
            if item.get('PerTxn_Num_LwrLmt_Val'):
                return item.get('PerTxn_Num_LwrLmt_Val')
        return ''

    def data_format(self, data):
        final_data = {}
        final_data['product_status'] = '在售'
        final_data['issue_bank'] = '建设银行'
        final_data['lowest_yield'] = data.get('Exp_AnulRtRet', '')
        final_data['highest_yield'] = final_data['lowest_yield']
        final_data['sales_target'] = ''
        final_data['product_name'] = data.get('ChmtPd_Nm')
        final_data['sales_target'] = ''
        final_data['url'] = ''
        final_data['file_url'] = self.get_file_url(data.get('Web_Acs_Rsc_URL', ''))
        final_data['sales_start_date'] = data.get('Ivs_StDt', '')
        final_data['sales_end_date'] = data.get('Ivs_CODt', '')
        final_data['currency'] = u'人民币' if data.get('CcyCd') == '156' else '其他'
        final_data['product_type'] = ''
        final_data['product_term'] = data.get('Ivs_Trm', '')
        final_data['product_nature'] = ''
        final_data['value_date'] = ''
        final_data['min_purchase_amount'] = self.purchase_amount(data)
        self.save_data(final_data)

    def save_data(self, data):
        print(data)
        if data.get('file_url'):
            resp = self._get(data.get('file_url'))
            with open('./data/{}.pdf'.format(data['product_name']), mode='wb') as wp:
                wp.write(resp.content)

    def main(self):
        for url in URLS:
            resp = self._get(url)
            for data in resp.json().get('PROD_INFO_GRP', []):
                self.data_format(data)


if __name__ == '__main__':
    c = CCB()
    c.main()
