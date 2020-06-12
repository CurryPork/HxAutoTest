# 基础配置信息
import codecs
import configparser
import os

class ReadConfig:
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    def __init__(self):

        self.CONFIG_PATH = self.path_dir+"\conf\config.ini"
        self.CASE_EXCEL = self.path_dir+"\data\case_ehr.xlsx"
        self.html_report_path = self.path_dir+"\report"
        my_config = open(self.CONFIG_PATH, "r", encoding="utf8")
        data = my_config.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(self.CONFIG_PATH, "w", encoding="utf8")
            file.write(data)
            file.close()
        my_config.close()
        # 读取config.ini 配置文件
        self.cf = configparser.ConfigParser()
        self.cf.read(self.CONFIG_PATH)

    def get_info(self, modlue, name):

        return self.cf.get(modlue, name)


if __name__ == '__main__':
    a = ReadConfig()
    # print(a.cf.get("LOGIN_INFO","loginHost"))
    print(a.get_info("LOGIN_INFO", "tester"))