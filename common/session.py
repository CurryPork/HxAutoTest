# coding="utf8"
import requests
from conf.config import ReadConfig


class Session(object):
    def __init__(self):
        self.loginHost = ReadConfig().get_loginfo("LOGIN_INFO", "loginHost")
        self.username = ReadConfig().get_loginfo("LOGIN_INFO", "username")
        self.password = ReadConfig().get_loginfo("LOGIN_INFO", "password")

    def get_session(self):
        header = {"Content-Type": "application/json"}
        data = {"username": self.username, "password": self.password}
        s = requests.post(self.loginHost, headers=header, json=data)
        my_token = "Token " + s.json().get("token")
        print(my_token)
        return my_token


if __name__ == '__main__':
    a = Session()
    a.get_session()
