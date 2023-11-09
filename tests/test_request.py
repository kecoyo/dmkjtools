import unittest

from common.request import *


class TestRequest(unittest.TestCase):
    def test_check_exists(self):
        url = "https://fileimosscdn.lejiaolexue.com/shixun/bae303302d3282f0141406398e21e4cc7e42c45f.mp4"
        status = check_exists(url)
        self.assertEqual(status, 200)

    def test_get_json(self):
        json = get_json("https://tk.ljlx.com/base/school_stage")
        self.assertEqual(json["result"], 0)

        kw = {"stage_id": 2}
        json = get_json("https://tk.ljlx.com/base/subject", params=kw)
        self.assertEqual(json["result"], 0)

    def test_post_json(self):
        json = post_json("https://tk.ljlx.com/base/school_stage")
        self.assertEqual(json["result"], 0)

        data = {"vendorid": 34, "deviceid": 1}
        json = post_json(
            "http://api.banpai.ljlx.com/classshow/api/queryVendorConfig", json=data
        )
        self.assertEqual(json["result"], 0)

        data = {"user_ids": "[1924049]"}
        json = post_json(
            "https://api.ljlx.com/platform/userinfo/getuserinfosimples", data=data
        )
        self.assertEqual(json["result"], 0)

    def test_get_text(self):
        text = get_text("https://www.runoob.com/")
        self.assertNotEqual(text, "")

    def test_post_text(self):
        text = post_text("https://www.runoob.com/")
        self.assertNotEqual(text, "")
