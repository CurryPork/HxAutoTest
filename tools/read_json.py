import json
from conf.config import ReadConfig

class ReadJson(object):
    def __init__(self, filename):
        path_dir = ReadConfig().path_dir
        self.filepath = path_dir+"\data\\"+ filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

if __name__ == '__main__':
    a = ReadJson("ehr.json")
    print(a.read_json())
