import requests


class Requests(object):
    def __init__(self):
        pass

    def get_request(self, url):
        header = {"Content-Type": "application/json"}
        s = requests.get(url)
        pass

    pass
