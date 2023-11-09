import unittest
import json


class TestJson(unittest.TestCase):
    def test_dumps(self):  # 时间格式化
        data = {"no": 1, "name": "Runoob", "url": "http://www.runoob.com"}
        str = '{"no": 1, "name": "Runoob", "url": "http://www.runoob.com"}'
        json_str = json.dumps(data)
        self.assertEqual(json_str, str)

    def test_time_parse(self):  # 时间解析
        data = {"no": 1, "name": "Runoob", "url": "http://www.runoob.com"}
        str = '{"no": 1, "name": "Runoob", "url": "http://www.runoob.com"}'
        json_data = json.loads(str)
        self.assertEqual(json_data, data)
