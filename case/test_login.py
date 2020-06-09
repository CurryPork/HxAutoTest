# 测试接口类
import unittest
from parameterized import parameterized,param
from common.session import ApiLogin
from tools.read_json import ReadJson
from tools.return_json import ReturnJson


# my_tuples()
# rj = ReadJson("login_more.json").read_json().values()
# print(rj)


class TestLogin(unittest.TestCase):
    # @parameterized.expand([param(rj["url"], rj["username"],rj["password"])]) 写死传输值
    @parameterized.expand(ReturnJson.my_tuple())
    def test_login(self, url, username, password):
        s = ApiLogin().api_post_login(url, username, password)
        print(s.json())
        self.assertEqual("tanxi",s.json()["name"])


if __name__ == '__main__':
    unittest.main()





























# import unittest
# from common.api_login import ApiLogin
# from parameterized import parameterized
# from tools.read_json import ReadJson
#
#
# def get_data():
#     data = ReadJson("login.json").read_json()
#     list = []
#     list.append((data.get("url"),
#                  data.get("username"),
#                  data.get("password"),
#                  data.get("code"),
#                  data.get("expect_result")))
#
#     return list
#
#
# class TestLogin(unittest.TestCase):
#     @parameterized.expand(get_data())
#     def test_login(self, url, username, password, code, expect_result):
#         s = ApiLogin().api_post_login(url, username, password)
#         print("查看响应结果:{}".format(s.json()))
#         self.assertEqual(expect_result, s.json()["name"])
#         # self.assertEqual(code, s.json()["code"])
#
#
# if __name__ == '__main__':
#     unittest.main()