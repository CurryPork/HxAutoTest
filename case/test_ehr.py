from common.my_requests import Requests
import pytest
from tools.return_json import ReturnJson
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

if __name__ == '__main__':
    pytest.main(["-s","test_ehr.py"])