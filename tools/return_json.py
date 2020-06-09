from tools.read_json import ReadJson

class ReturnJson(object):
    @staticmethod
    def my_tuple():
        """单个json数据
        :return:返回单个json数据
        """
        list = []
        rj = ReadJson("login.json").read_json()
        list.append((rj["url"], rj["username"], rj["password"], rj["expect_result"]))
        return list

    @staticmethod
    def my_tuples(url,expect_result):
        """多个json数据
            :return:返回多个json数据
            """
        list = []
        rj = ReadJson("ehr.json").read_json().values()
        for x in rj:
            list.append((x.get(url), x.get(expect_result)))
        print(list)
        return list

    # 未完成  动态传入不定的参数
    # def my_tuples(self,*args):
    #     """多个json数据
    #         :return:返回多个json数据
    #         """
    #     listA = []
    #     listB = []
    #     listC = []
    #     rj = ReadJson("ehr.json").read_json().values()
    #     for x in args:
    #         listA.append(x)
    #     # print(listA)
    #
    #     for y in rj:
    #         for z in listA:
    #             listB = []
    #             listB.append(y.get(z))
    #             listC.append(listB)
    #
    #         pass
    #
    #     print(listC)
    #     return list
if __name__ == '__main__':
    a = ReturnJson().my_tuples("url","expect_result")
    # print(a)