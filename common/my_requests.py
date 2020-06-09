import requests
import pytest
from common.my_session import MySession

class Requests(object):
    def __init__(self):
        self.authorization = MySession().get_session()

    def get_request(self, url):
        headers = {"authorization":self.authorization,"Content-Type": "application/json"}
        s = requests.get(url,headers=headers)
        return s


if __name__ == '__main__':
    url = "http://ehrt.g5air.com:8001/api/class/view_org_dept_position"
    a = Requests()
    b = a.get_request(url)
    print(b.text)
