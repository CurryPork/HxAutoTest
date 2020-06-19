from common.my_requests import Requests
import pytest
from conf.config import ReadConfig
from tools.read_excel import ReadExcel
from common.my_session import MySession
from tools.return_json import ReturnJson
from tools.allure_report import allure_report_get
import allure
# from tools.return_json import ReturnJson

@allure.feature("测试FOC接口")
class TestFoc(object):
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