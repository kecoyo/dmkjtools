import unittest
import keyword


class TestString(unittest.TestCase):
    def test_format(self):  # 字符串拼接、格式化
        num = 10
        self.assertEqual("The number is " + str(num), "The number is 10")
        self.assertEqual("The number is {}".format(num), "The number is 10")
        self.assertEqual(f"The number is {num}", "The number is 10")
        self.assertEqual("The number is %05d" % num, "The number is 00010")
        self.assertEqual(f"The number is %(num)d" % {"num": num}, "The number is 10")

    def test_slice(self):  # 字符串分片
        str = "123456789"
        self.assertEqual(str[0:-1], "12345678")  # 输出第一个到倒数第二个的所有字符
        self.assertEqual(str[0], "1")  # 输出字符串第一个字符
        self.assertEqual(str[2:5], "345")  # 输出从第三个开始到第六个的字符（不包含）
        self.assertEqual(str[2:], "3456789")  # 输出从第三个开始后的所有字符
        self.assertEqual(str[1:5:2], "24")  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
        self.assertEqual(str * 2, "123456789123456789")  # 输出字符串两次
        self.assertEqual(str + "你好", "123456789你好")  # 连接字符串

        print("------------------------------")

        print("hello\nrunoob")  # 使用反斜杠(\)+n转义特殊字符
        print(r"hello\nrunoob")  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

    def test_in_kwlist(self):  # 关键字列表
        kw = keyword.kwlist
        self.assertIn("continue", kw)
        self.assertNotIn("yangkk", kw)
