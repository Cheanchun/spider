# -*- coding=utf-8 -*-
"""
@Auth:CheanCC
@Date:2020
@Desc:私募机构管理人统计信息
@Todo
"""
import json
import sys

sys.path.append("../")
sys.path.append("../../")
sys.path.append("../../../")
reload(sys)

from api_parser.custom_parse_base import CustomDataParse


class ManagerInfo(CustomDataParse):


    def parse_data(self, url_id, url, redirect_url, content):
        datas = content.get('data', {}).get('data', {}).get('dataList', [])
        final_data = []
        for data in datas:
            temp = {}
            temp['title'] = data.get('title', '')
            temp['content'] = data.get('docContent', '')
            temp['date'] = data.get('docRelTime', '')
            # json.dumps(clean_data, ensure_ascii=False)
            final_data.append(temp)
        return final_data

