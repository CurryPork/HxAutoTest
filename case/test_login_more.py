import unittest
from common.my_session import ApiLogin
from parameterized import parameterized
from tools.read_json_more import ReadJson


def get_data():
    datas = ReadJson("login_more.json").read_json()
    list = []
    for data in datas.values():
        list.append((data.get("url"),data.get("username"),
                     data.get("password"),
                     data.get("code"),
                     data.get("expect_result")))

    return list


class TestLogin(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_login(self, url, username, password, code, expect_result):
        s = ApiLogin().api_post_login(url, username, password)
        print("查看响应结果:{}".format(s.json()))
        self.assertEqual(expect_result, s.json()["name"])
        # self.assertEqual(code, s.json()["code"])


if __name__ == '__main__':
    unittest.main()