from common.my_requests import Requests
import pytest
from conf.config import ReadConfig
from tools.read_excel import ReadExcel
from common.my_session import MySession
from tools.return_json import ReturnJson
from tools.allure_report import allure_report_get
import allure
# from tools.return_json import ReturnJson

@allure.feature("测试EHR接口")
class TestEhr(object):
    readexcel = ReadExcel(ReadConfig().CASE_EXCEL)
    list_case = readexcel.dict_data()
    list_item = ReadExcel(ReadConfig().CASE_EXCEL).dict_item(list_case)

    @pytest.fixture()
    def get_session(self):
        """
        每次只获取一次session
        :return: session值
        """
        self.authorization = MySession().get_session()
        return self.authorization

    @allure.story("读取Excel用例")
    # @allure.title("{title}")
    @pytest.mark.parametrize("dic",list_case ,ids = list_item)
    def test_ehr_excel(self, dic, get_session):
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
        headers = {"authorization": self.authorization, "Content-Type": "application/json"}
        if request_type == "get":
            r = Requests().get_request(request_url,headers=headers)
            # 增加allure返回值等信息
            allure_report_get(headers, request_url, r.json())
            assert r.status_code == 200
            assert except_result in r.text
        elif request_type == "post":
            r = Requests().post_request(request_url, headers=headers, json_data=request_data)
            # 增加allure返回值等信息
            allure_report_get(headers, request_url, r.json())
            assert r.status_code == 200
            assert except_result in r.text

    @allure.story("读取json用例")
    # @pytest.mark.skip
    @pytest.mark.parametrize("dic", ReturnJson().return_json())
    def test_ehr_json(self, dic,get_session):
        """通过json读取用例
        :param dic:
        :return:
        """
        request_url = dic.get("request_url")
        headers = {"authorization": self.authorization, "Content-Type": "application/json"}
        a = Requests().get_request(request_url,headers=headers)
        allure_report_get(headers, request_url, a.json())
        assert dic.get("except_result") in a.text
        # print('\n测试数据为\n{}'.format(dic.get("except_result")))


if __name__ == '__main__':
    # pytest.main(["-s","-n 2","test_ehr.py"])  # 用2个线程跑接口
    # pytest.main(["-s","test_ehr.py"])
    # TestEhr().handle_data()
    print(TestEhr().list_case_name)