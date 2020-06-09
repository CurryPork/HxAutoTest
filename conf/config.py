# 基础配置信息
import codecs
import configparser
CONFIG_PATH = "../conf/config.ini"

class ReadConfig:

    def __init__(self):
        my_config = open(CONFIG_PATH, "r", encoding="utf8")
        data = my_config.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(CONFIG_PATH, "w", encoding="utf8")
            file.write(data)
            file.close()
        my_config.close()
        # 读取config.ini 配置文件
        self.cf = configparser.ConfigParser()
        self.cf.read(CONFIG_PATH)

    def get_loginfo(self, modlue, name):

        return self.cf.get(modlue, name)


if __name__ == '__main__':
    a = ReadConfig()
    # print(a.cf.get("LOGIN_INFO","loginHost"))
    print(a.get_loginfo("LOGIN_INFO","tester"))