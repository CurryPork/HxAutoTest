from tools.read_json import ReadJson

class ReturnJson(object):
    @staticmethod
    def my_tuple():
        """单个json数据
        :return:返回单个json数据
        """
        list = []
        rj = ReadJson("login.json").read_json()
        list.append((rj["url"], rj["username"], rj["password"]))
        return list

    @staticmethod
    def my_tuples():
        """多个json数据
            :return:返回多个json数据
            """
        list = []
        rj = ReadJson("login_more.json").read_json().values()
        for x in rj:
            # list.append((x.get("url"), x.get("username"), x.get("password")))
            list.append((x["url"]), x["username"], x["password"])
        return list
    pass