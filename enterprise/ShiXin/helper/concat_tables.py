import os

import numpy as np
import pandas as pd
from pandas import DataFrame


class TableHandle:
    def __init__(self, old_table, new_table, concat_columns: list):
        if os.path.isfile(old_table) and os.path.isfile(new_table):
            self.old_table = old_table
            self.new_table = new_table
            self.concat_columns = concat_columns
        else:
            raise FileNotFoundError("文件不存在!")

    def concat_table(self):
        old_data = pd.read_excel(self.old_table)
        new_data = pd.read_excel(self.new_table)[["严重违法失信企业名称", "证件信息(统一社会信用代码)", "生效日期"]]
        data = pd.concat([old_data, DataFrame(np.array(new_data), columns=self.concat_columns)], ignore_index=True)
        data.to_excel("./temp.xlsx")
        data = DataFrame(data)
        print(data[self.concat_columns])


table = TableHandle("./total.xlsx", "../失信名单客户登记表.xlsx", ["严重违法失信企业名称", "证件信息(统一社会信用代码)", "生效日期"])
table.concat_table()
