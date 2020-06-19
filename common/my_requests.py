import requests
import pytest
from common.my_session import MySession

class Requests(object):
    def __init__(self):
        """
        默认获取session
        """
        self.authorization = MySession().get_session()

        pass

    def get_request(self, url, headers):
        header = {"authorization": self.authorization, "Content-Type": "application/json"}  # 拼接header
        if not url.startswith("http://"):
            url = "http://{}".format(url)
            print(url)
        try:
            s = requests.get(url, headers=header)
        except requests.RequestException as e:
            print("RequestException url:{}".format(url))
            print("报错信息为:{}".format(e))
            return ()
        return s
    def post_request(self,url ,headers,json_data):
        header = {"authorization": self.authorization, "Content-Type": "application/json"}
        if not url.startswith("http://"):
            url = "http://{}".format(url)
            print(url)
        try:
            s = requests.post(url, headers=header, json=json_data)
        except requests.RequestException as e:
            print("RequestException url:{}".format(url))
            print("报错信息为:{}".format(e))
            return ()
        return s

    def get_request_cookie(self, url, cookies):
        header = {"authorization": self.authorization, "Content-Type": "application/json"}  # 拼接header
        print(header)
        s = requests.get(url,headers=header)
        return s


if __name__ == '__main__':
    url = "http://.com:8001/api/class/view_org_dept_position"
    a = Requests()
    b = a.get_request(url)
    print(b.text)
