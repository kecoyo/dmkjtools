import unittest
import re


class TestRe(unittest.TestCase):
    # re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。
    def test_match(self):
        line = "Cats are smarter than dogs"
        matchObj = re.match(r"(.*) are (.*?) .*", line, re.M | re.I)

        self.assertEqual(matchObj.group(), "Cats are smarter than dogs")
        self.assertEqual(matchObj.group(1), "Cats")
        self.assertEqual(matchObj.group(2), "smarter")

    def test_search(self):
        line = "Cats are smarter than dogs"
        matchObj = re.search(r"(.*) are (.*?) .*", line, re.M | re.I)

        self.assertEqual(matchObj.group(), "Cats are smarter than dogs")
        self.assertEqual(matchObj.group(1), "Cats")
        self.assertEqual(matchObj.group(2), "smarter")

    def test_findall(self):
        result1 = re.findall(r"\d+", "runoob 123 google 456")
        result2 = ["123", "456"]
        self.assertEqual(result1, result2)

        result1 = re.findall(r"(\w+)=(\d+)", "set width=20 and height=10")
        result2 = [("width", "20"), ("height", "10")]
        self.assertEqual(result1, result2)

    def test_finditer(self):
        iter = re.finditer(r"\d+", "runoob 123 google 456")
        result1 = [x.group() for x in iter]
        result2 = ["123", "456"]
        self.assertEqual(result1, result2)

    def test_sub(self):
        phone = "2004-959-559 # 这是一个电话号码"
        result1 = re.sub(r"#.*$", "", phone)
        result2 = "2004-959-559 "
        self.assertEqual(result1, result2)

    def test_split(self):
        result1 = re.split("\W+", "runoob, runoob, runoob.")
        result2 = ["runoob", "runoob", "runoob", ""]
        self.assertEqual(result1, result2)
