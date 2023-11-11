import unittest
import random

"""
学习、测试内置函数和对象
"""


class TestBuildIn(unittest.TestCase):
    def test_globals(self):  # 全局变量的字典
        obj = globals()
        self.assertEqual(__name__, "test_builtin")

    def test_random(self):  # 生成随机数
        num = random.random()
        self.assertTrue(0 < num < 1)
