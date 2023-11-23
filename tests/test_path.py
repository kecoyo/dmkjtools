import os
import sys
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

    def test_cur_path(self):
        cur_path1 = os.path.dirname(__file__)
        cur_path2 = sys.path[0]
        self.assertEqual(cur_path1, cur_path2)
