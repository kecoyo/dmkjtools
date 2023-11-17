import unittest
import common.config as config


"""
测试加载配置文件
"""


class TestConfig(unittest.TestCase):
    def test_config(self):  # 获取配置文件中的配置项
        self.assertEqual(config.get("database", "host"), "localhost")
