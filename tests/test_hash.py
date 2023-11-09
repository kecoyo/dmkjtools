import unittest

from common.hash import *


class TestHash(unittest.TestCase):
    def test_str_md5(self):
        str = "yangkk"
        md5 = str_md5(str)
        print(md5)
        self.assertTrue(md5 != "")

    def test_file_md5(self):
        file = "d:/output/test/license.zip"
        md5 = file_md5(file)
        print(md5)
        self.assertTrue(md5 != "")
