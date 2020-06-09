import json


class ReadJson(object):
    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

#
#
# if __name__ == '__main__':
#     datas = ReadJson("login_more.json").read_json()
#     list = []
#
#     for data in datas.values():
#
#         list.append((data.get("url"),
#                      data.get("username"),
#                      data.get("password"),
#                      data.get("code"),
#                      data.get("expect_result")))
#     print(list)
