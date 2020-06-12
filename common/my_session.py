# coding="utf8"
import requests
from conf.config import ReadConfig


class MySession(object):
    def __init__(self):
        self.loginHost = ReadConfig().get_info("LOGIN_INFO", "loginHost")
        self.username = ReadConfig().get_info("LOGIN_INFO", "username")
        self.password = ReadConfig().get_info("LOGIN_INFO", "password")

    def get_session(self):
        header = {"Content-Type": "application/json"}
        data = {"username": self.username, "password": self.password}
        s = requests.post(self.loginHost, headers=header, json=data)
        my_token ="Token " + s.json().get("token")
        # print("\n获得token:{}".format(my_token))
        return my_token

    def get_cookie(self):
        header = {"Content-Type": "application/json"}
        data = {"username": self.username, "password": self.password}
        s = requests.post(self.loginHost, headers=header, json=data)
        print(s.content)
        my_cookie = s.json().get("Cookie")
        # print("\n获得token:{}".format(my_token))
        return my_cookie

if __name__ == '__main__':
    a = MySession()
    print(a.get_cookie())
