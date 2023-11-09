import os
import unittest
from pathlib import Path


class TestPath(unittest.TestCase):
    def test_getcwd(self):
        os.chdir("D:\\output")
        self.assertEqual(os.getcwd(), "D:\\output")

    def test_chdir_system(self):
        os.chdir("D:/output")
        os.system("mkdir today")
        self.assertTrue(Path("d:/output/today").exists())

    def test___file__(self):
        self.assertIn("test_path.py", __file__)

    def test___name__(self):
        self.assertEqual(__name__, "test_path")

    def test___package__(self):
        self.assertEqual(__package__, "")

    def test_basepath(self):
        basepath = os.path.abspath(os.path.dirname(__file__))  # 当前模块文件的根目录
        self.assertEqual(basepath, f"d:\\PythonProjects\\dmkjtools\\tests")
