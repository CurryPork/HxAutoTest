# coding:utf-8
import xlrd
from conf.config import ReadConfig

class ReadExcel:
    def __init__(self, case_excel, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(case_excel)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行取对应values值
                # s['rowNum'] = i+2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r
# 返回题目
    def dict_item(self, list):
        item = []
        for x in list:
            item.append(x.get("interface_name"))
        # print(item)
        return item

if __name__ == '__main__':
    a = ReadExcel("../data/case_ehr.xlsx")
    b = a.dict_data()
    a.dict_item(b)
