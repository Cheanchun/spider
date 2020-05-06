# coding:utf-8
import json
import random
import time
import traceback

import redis
import requests

from bank.utils.Comm import CommSession

redis_info = {
    "host": "47.105.54.129",
    "port": 6388,
    "password": "admin"

}
user_redis = redis.StrictRedis(**redis_info)


class OfferShow():
    def __init__(self):
        self._TOPIC_ID = ''
        self.session = CommSession(verify=True).session()
        self.access_token = '520pbkdf2_sha256$15000$pAyCwlbfv8bi$ytkzhLIvv5+sYwytrpIpzGDkg26d4HQpxjr6pCl1i1k=offershow'
        self.redis_key = 'hr_opinion_offershow'
        self.TOPIC_ID = ''
        self.query_words = [u'招银', u'招商银行', u'招银网络科技']
        self.user_redis = user_redis

    def _get(self, url, timeout=30, method='get', post_data=None, retry=3):
        """
        网页下载
        :param url:
        :return:resp
        :rtype: requests.Response
        """
        time.sleep(random.randint(2, 4))
        if method == 'get':
            for i in range(retry):
                try:
                    resp = self.session.get(url=url, timeout=timeout)
                    if resp.status_code == 200:
                        return resp
                except requests.Timeout:
                    continue
            raise requests.RequestException('requests error {}'.format(url))
        elif method.lower() == 'post' and post_data is not None:
            for i in range(retry):
                try:
                    resp = self.session.post(url=url, data=post_data, allow_redirects=True, timeout=timeout)
                    if resp.status_code // 100 == 2:
                        return resp
                except requests.Timeout:
                    continue
            raise requests.RequestException('requests error {}'.format(url))
        else:
            raise ValueError('func args error')

    def query_jobs(self, content, _type='1', access_token=None):
        """
        query jobs list
        :param content:query keywords        精确查询   公司名称+地点/岗位   eg:华为+杭州
        :param _type:query type              排序(倒序)  0-可信度 1-时间 2-浏览量
        :param access_token:post token       暂时不确定会不会改变
        :return: jobs_info
        """
        url = 'https://www.ioffershow.com/webapi/jobnewsearch/'
        token = access_token if access_token else self.access_token
        post_data = {'access_token': token, 'content': content, 'type': _type}
        response = self._get(url=url, method='post', post_data=post_data)
        if response.json().get('r') == 1:
            return response.json()
        else:
            raise requests.exceptions.InvalidSchema('not correct type or value return')

    def query_job_detail(self, job_id, access_token=None):
        """
        query job detail by job_id
        :param job_id:job id
        :param access_token:
        :return:
        """
        url = 'https://www.ioffershow.com/webapi/jobdetail/'
        token = access_token if access_token else self.access_token
        post_data = {'access_token': token, 'id': job_id}
        response = self._get(url, method='post', post_data=post_data)
        if response.json().get('r') == 1:
            return response.json().get('info')
        else:
            raise requests.exceptions.InvalidSchema('not correct type or value return')

    def query_job_comments(self, job_id, access_token=None):
        """
        query comments about one job by job id
        :param job_id:job id
        :param access_token:
        :return: job_comments
        """
        url = 'https://www.ioffershow.com/webapi/jobmessagelist/'
        token = access_token if access_token else self.access_token
        post_data = {'access_token': token, 'id': job_id}
        response = self._get(url, method='post', post_data=post_data)
        if response.json().get('r') == 1:
            return response.json().get('info')
        else:
            raise requests.exceptions.InvalidSchema('not correct type or value return')

    @staticmethod
    def _data_format(item, job_info, comments_info, final_data, query_word):
        final_data['field'] = job_info.get('hangye', u'')
        final_data['city'] = job_info.get('city', u'')
        final_data['position'] = job_info.get('position', u'')
        final_data['education'] = job_info.get('xueli', u'')
        final_data['user_id'] = job_info.get('ip', u'')
        final_data['salary'] = job_info.get('salary', u'')
        final_data['remark'] = job_info.get('remark', u'')
        final_data['post_time'] = item.get('time', u'')
        final_data['post_tags'] = [job_info.get('time', u''), ]
        final_data['reliability'] = job_info.get('score', u'')
        final_data['visit_num'] = job_info.get('number', u'')
        final_data['post_content'] = json.dumps(job_info, ensure_ascii=False)
        final_data['query'] = query_word.decode('u8')
        final_data['post_id'] = item.get('id', u'')
        final_data['post_title'] = u''
        final_data['follow'] = u''
        final_data['like'] = u''
        final_data['sentiment'] = u''  # 情感分析指数
        replys = []
        for item in comments_info:  # comment
            temp = {}
            temp['comment_id'] = item.get('id')
            temp['comment_author'] = item.get('ip')
            temp['comment_content'] = item.get('content')
            temp['comment_time'] = item.get('time')
            temp['comment_like'] = u''
            temp['comments'] = []
            replys.append(temp)
        final_data['replys'] = replys
        return final_data

    def save_data(self, data):
        # todo 数据存储
        # self.save_topic_data(url,data,self.TOPIC_ID)
        data = json.dumps(data, ensure_ascii=False)
        fp.write(data.encode('utf-8') + '\n')
        fp.flush()
        print(data)

    def _get_query_words(self):
        if not self.user_redis.exists(self.redis_key):
            for word in self.query_words:
                self.user_redis.sadd(self.redis_key, word)
        return self.user_redis.spop(self.redis_key)

    def main(self):
        """
        :return:
        """
        query = self._get_query_words()
        try:
            res = self.query_jobs(query)
            for item in res.get('info'):
                final_data = {}
                job_info = self.query_job_detail(item.get('id'))
                comments_info = self.query_job_comments(item.get('id'))
                final_data = self._data_format(item, job_info, comments_info, final_data, query)
                self.save_data(final_data)
                final_data.clear()
        except Exception:
            print(traceback.format_exc())


if __name__ == '__main__':
    fp = open('offershow.txt', mode='a+')
    t = OfferShow()
    t.main()
    fp.close()
