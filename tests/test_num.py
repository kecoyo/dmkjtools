import unittest


class TestNum(unittest.TestCase):
    def test_round(self):  # 保留两位小数
        num = 1.22334577901
        self.assertEqual(round(num, 2), 1.22)
        self.assertEqual("%.2f" % num, "1.22")
        self.assertEqual(format(num, ".2f"), "1.22")
        self.assertEqual("{:.2f}".format(num), "1.22")
