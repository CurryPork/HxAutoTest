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
    #
    # def handle_data(self):
    #     list = ReadExcel(ReadConfig().CASE_EXCEL).dict_data()
    #     print(list)
    #     list_case_name = []
    #     for x in list:
    #         # print(x.get("case_name"))
    #         list_case_name.append(x.get("case_name"))
    #     print(list_case_name)
    #     return list_case_name

if __name__ == "__main__":
    # case_excel = "../data/case_ehr.xlsx"
    # sheetName = "Sheet1"
    # return_list = ReadExcel(case_excel).dict_data()
    # print(return_list)
    # ReadExcel(ReadConfig().CASE_EXCEL).handle_data()

