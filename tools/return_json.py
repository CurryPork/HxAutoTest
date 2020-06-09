from tools.read_json import ReadJson

class ReturnJson(object):
    @staticmethod
    def return_json():
        """任意多个json数据
            :return:返回多个json数据
            """
        list = []
        rj = ReadJson("ehr.json").read_json().values()
        for x in rj:
            list.append(x)
        print(list)
        return list
if __name__ == '__main__':
    a = ReturnJson().return_json()
