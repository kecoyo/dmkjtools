import os
from common.fs import read_csv
from common.logger import logger
from common.task import CsvTask

"""
示例: CsvTask多线程任务处理
"""


class DemoTask(CsvTask):
    def process_row(self, row):
        # print(row)
        # print(dir(row))
        logger.info("{},{}".format(row["userId"], row["uname"]))
        row["status"] = "OK"
        # raise Exception("aaa")


# 创建任务，启动任务
process = DemoTask(max_workers=4)
process.start()
