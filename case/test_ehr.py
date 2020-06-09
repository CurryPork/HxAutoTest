from common.my_requests import Requests
import pytest
from tools.return_json import ReturnJson
from tools.read_excel import ExcelUtil
filepath = "../data/test_ehr.xlsx"
class TestEhr(object):
    # 参数化
    # @pytest.mark.parametrize("url,expected",
    # [("http://ehrt.g5air.com:8001/api/class/view_org_dept_position","董事会秘书"),
    # ("http://ehrt.g5air.com:8001/api/class/sal_adjust","rows")])
    @pytest.mark.parametrize("url,expect_result",ReturnJson().my_tuples("url","expect_result"))
    def test_ehr(self,url,expect_result):
        a = Requests().get_request(url)
        print(a.text)
        assert expect_result in a.text
    print(ExcelUtil(filepath).dict_data())
    @pytest.mark.parametrize("ID,模块,用例名称,接口名称,请求URL,请求方法,请求参数类型,请求参数,预期结果,测试结果", ExcelUtil(filepath).dict_data())
    def test_ehr_excel(self, 请求URL, 预期结果):
        a = Requests().get_request(请求URL)
        print(a.text)
        assert 预期结果 in a.text

if __name__ == '__main__':
    pytest.main(["-s","test_ehr.py"])