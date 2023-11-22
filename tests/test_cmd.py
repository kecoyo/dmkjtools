import subprocess
import os
import time
import unittest

"""
学习、测试内置函数和对象
"""


class TestCmd(unittest.TestCase):
    def test_os_system(self):  # 测试os.system()函数
        """
        需要等待子进程执行完再继续执行的用这个
        """
        cmd = "git status"
        ret = os.system(cmd)  # 执行命令, 返回状态码，0表示成功, 非0表示失败，会打印执行后的返回信息到控制台
        self.assertEqual(ret, 0)

    def test_os_popen(self):  # 测试os.popen()函数
        """
        两个程序可以并行执行的用这个
        """
        cmd = "git status"
        ret = os.popen(cmd)
        print(ret.read())  # 打印执行后的返回信息到控制台
        self.assertNotEqual(ret, "")

    def test_subprocess_run(self):
        ret = subprocess.run(["git", "status"])  # 执行命令, 返回一个对象，会打印执行后的返回信息到控制台
        print("returncode:", ret.returncode)
        print("args:", ret.args)
        print("stdout:", ret.stdout)
        self.assertEqual(ret.returncode, 0)
