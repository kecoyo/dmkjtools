import unittest
import time
from datetime import date, datetime, timedelta


class TestDateTime(unittest.TestCase):
    def test_time(self):  # 当前时间戳
        secs = time.time()
        self.assertNotEqual(secs, 1699507234.6535578)

    def test_localtime(self):  # 当前时间元组
        # 当前时间元组：time.struct_time(tm_year=2023, tm_mon=11, tm_mday=9, tm_hour=13, tm_min=20, tm_sec=34, tm_wday=3, tm_yday=313, tm_isdst=0)
        localtime = time.localtime(1699507234)
        self.assertEqual(localtime.tm_year, 2023)
        self.assertEqual(localtime.tm_mon, 11)
        self.assertEqual(localtime.tm_mday, 9)
        self.assertEqual(localtime.tm_hour, 13)
        self.assertEqual(localtime.tm_min, 20)
        self.assertEqual(localtime.tm_sec, 34)

    def test_time_format(self):  # 时间格式化
        secs = 1699507234.0
        localtime = time.localtime(secs)
        str = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
        self.assertEqual(str, "2023-11-09 13:20:34")

    def test_time_parse(self):  # 时间解析
        str = "2023-11-09 13:20:34"
        localtime = time.strptime(str, "%Y-%m-%d %H:%M:%S")
        secs = time.mktime(localtime)
        self.assertEqual(secs, 1699507234.0)

    def test_date_format(self):  # 日期格式化
        self.assertEqual(date(2023, 12, 4).isoformat(), "2023-12-04")
        self.assertEqual(date(2023, 12, 4).ctime(), "Mon Dec  4 00:00:00 2023")
        self.assertEqual(date(2023, 12, 4).timetuple().tm_year, 2023)
        self.assertEqual(date(2023, 12, 4).strftime("%d/%m/%y"), "04/12/23")

    def test_date_parse(self):  # 日期解析
        self.assertEqual(date.today().year, 2023)
        self.assertEqual(date(2002, 12, 4).year, 2023)
        self.assertEqual(date.fromtimestamp(time.time()).year, 2023)
        self.assertEqual(date.fromisoformat("2023-11-04").year, 2023)
        self.assertEqual(date.strptime("31/01/23", "%d/%m/%y").year, 2023)

    def test_datetime_format(self):  # 日期时间格式化
        self.assertEqual(datetime(2023, 12, 4).isoformat(), "2023-12-04T00:00:00")
        self.assertEqual(datetime(2023, 12, 4).ctime(), "Mon Dec  4 00:00:00 2023")
        self.assertEqual(datetime(2023, 12, 4).timetuple().tm_year, 2023)
        self.assertEqual(
            datetime(2023, 12, 4, 0, 0, 0).strftime("%d/%m/%y %H:%M:%S"),
            "04/12/23 00:00:00",
        )

    def test_datetime_parse(self):  # 日期时间解析
        self.assertEqual(datetime.today().year, 2023)
        self.assertEqual(datetime(2023, 12, 4).year, 2023)
        self.assertEqual(datetime.fromtimestamp(time.time()).year, 2023)
        self.assertEqual(datetime.fromisoformat("2023-11-04").year, 2023)
        self.assertEqual(
            datetime.strptime("31/01/23 23:59:59", "%d/%m/%y %H:%M:%S").year, 2023
        )

    def test_timedelta(self):  # 时长
        delta1 = timedelta(seconds=60)
        delta2 = timedelta(minutes=1)
        self.assertEqual(delta1.seconds, delta2.seconds)
