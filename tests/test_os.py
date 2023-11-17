import unittest
import os

"""
os相关功能测试
"""


class TestBuildIn(unittest.TestCase):
    def test_getenv(self):  # 获取环境变量
        debug = os.getenv("DEBUG", "0")
        self.assertEqual(debug, "1")
