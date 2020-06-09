from common.my_requests import Requests
import pytest
import conf.config
from tools.read_excel import ReadExcel
from tools.return_json import ReturnJson
# from tools.return_json import ReturnJson

class TestEhr(object):

    # 参数化 例子
    # @pytest.mark.parametrize("url,expected",
    # [("http://ehrt.g5air.com:8001/api/class/view_org_dept_position","董事会秘书"),
    # ("http://ehrt.g5air.com:8001/api/class/sal_adjust","rows")])
    # @pytest.mark.parametrize("url,expect_result",ReturnJson().my_tuples("url","expect_result"))
    # def test_ehr(self,url,expect_result):
    #     a = Requests().get_request(url)
    #     print(a.text)
    #     assert expect_result in a.text

    @pytest.mark.parametrize("dic", ReadExcel(conf.config.CASE_EXCEL).dict_data())
    def test_ehr_excel(self, dic):
        """通过excel读取用例
        :param dic:
        :return:
        """
        id = dic.get("id")
        case_name = dic.get("case_name")
        interface_name = dic.get("interface_name")
        request_url = dic.get("request_url")
        request_func = dic.get("request_func")
        request_type = dic.get("request_type")
        request_data = dic.get("request_data")
        except_result = dic.get("except_result")
        result = dic.get("result")
        code = dic.get("code")
        if request_type == "get":
            r = Requests().get_request(request_url)
            assert except_result in r.text
        elif request_type == "post":
            print("hello world")

        print(dic.get("id"))

    # @pytest.mark.parametrize("dic", ReturnJson().return_json())
    # def test_ehr_json(self, dic):
    #     """通过json读取用例
    #     :param dic:
    #     :return:
    #     """
    #     a = Requests().get_request(dic.get("request_url"))
    #     assert dic.get("except_result") in a.text
    #     # print('\n测试数据为\n{}'.format(dic.get("except_result")))


if __name__ == '__main__':
    pytest.main(["-s","test_ehr.py"])