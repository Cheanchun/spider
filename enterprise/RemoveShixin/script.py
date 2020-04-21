# 将信息批量导入excel表格
from datetime import datetime

import numpy as np
import os
import pandas as pd
import redis
from pandas import DataFrame

from helper.config import BaseConfig


class TableHandle:
    def __init__(self, old_table, new_table, concat_columns=["单位名称", "注册码", "统一社会信用代码", "生效日期"]):
        if os.path.isfile(old_table) and os.path.isfile(new_table):
            self.old_table = old_table
            self.new_table = new_table
            self.concat_columns = concat_columns
        else:
            raise FileNotFoundError("FileNotFoundError:文件不存在!")

    def concat_table(self):
        old_data = pd.read_excel(self.old_table)
        new_data = pd.read_excel(self.new_table)[["严重违法失信企业名称", "注册码", "统一社会信用代码", "生效日期"]]
        data = pd.concat([old_data, pd.DataFrame(np.array(new_data), columns=self.concat_columns)], ignore_index=True)
        data = data.drop_duplicates(self.concat_columns)  # 去重

        self.data = data

    def save_to_excel(self):
        self.data.to_excel(self.old_table)
        data = DataFrame(self.data)
        print(data[self.concat_columns])


def drop_duplicates_data(path):
    data = pd.read_excel(path)
    data = data.drop_duplicates().reindex()  # 去重 重新排序
    print(data)
    data[["注册码", "统一社会信用代码"]] = data[["注册码", "统一社会信用代码", ]].astype('str')
    print(data)
    data.to_excel(path, )


def concat_table():
    path = "./datas/"
    dates = os.listdir(path)
    # print(dates)
    for date in dates:
        if os.path.isdir(path + date):
            old_table_path = f"{path}批量导入失信名单模板.xlsx"
            new_table_path = f"{path}{date}/失信名单移出登记表.xlsx"
            tabel = TableHandle(old_table=old_table_path, new_table=new_table_path)
            tabel.concat_table()
            tabel.save_to_excel()


def change_redis_zset_data(min=0, max=0, desc=True, amount=0, zset_name="order_company", db=0, password=None):
    '''
    # 设置有序集合的分数
    :param min: 最小分数
    :param max: 最大分数
    :param desc: 是否倒序
    :param amount: 原有分数上的增量
    :param zset_name: 有序集合名称
    :return: None
    '''
    r = redis.Redis(host=BaseConfig.HOST, port=BaseConfig.PORT, db=db, password=password)

    counts = r.zcount(zset_name, min=min, max=max)  # 统计分数起始个数
    print(counts)
    for i in range(counts):
        key = r.zrange(zset_name, start=0, end=0, desc=desc, withscores=True,
                       score_cast_func=int)
        key = key[0][0].decode("utf-8")  # start 和 end 不是分数参数,是集合元素索引的值,
        # start 和 end 不是分数参数,是集合元素索引的值, 返回值是索引区间的元素,为列表
        print(key)
        r.zincrby("order_company", value=key, amount=amount)
        # amount 在元素原有分数上进行增减  key 需要是字符串,redis查询出来的结果为字节流,需要转码才能以value的值传入才能匹配唯一性,否则会重新写入一个新值


if __name__ == '__main__':
    # concat_table()
    date = datetime.today().date()
    print(date)
    date = "2019-03-22"
    path = f"./datas/{date}/失信名单移出登记表.xlsx"
    # print(pd.read_excel(io="./datas/2019-03-29/失信名单移出登记表.xlsx"))
    drop_duplicates_data(path=path)
    # change_redis_zset_data(min=0, max=0, desc=False, amount=1, zset_name="order_company", db=BaseConfig.DB_INDEX,
    #                        password=BaseConfig.PASSWORD)
