# coding:utf-8
import xlrd

class ExcelUtil:
    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
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

# @pytest.mark.parametrize('Function,TestCase,Type,Run,URL,Headers,Parameter,SQL1,SQL2,SQL3,AssertType,Expect1,Expect2,Expect3', case_data)
#     def test_login1(self,Function,TestCase,Type,Run,URL,Headers,Parameter,SQL1,SQL2,SQL3,AssertType,Expect1,Expect2,Expect3):
#         r=requests.post(url=URL,headers=eval(Headers),json=eval(Parameter))
#         response=r.json()
#         print(response)
#         assert eval(Expect1)['code']==response['code']
#         assert eval(Expect1)['msg'] == response['msg']





if __name__ == "__main__":
    filepath = "../data/test_ehr.xlsx"
    sheetName = "Sheet1"
    print(ExcelUtil(filepath).dict_data())

