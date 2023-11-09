import os
from common.fs import read_csv
from common.logger import logger
from common.task import Task

"""
示例：Task多线程任务处理
"""


class DemoTask(Task):
    def read_data(self):
        self.list = read_csv(
            os.path.join(os.path.dirname(__file__), "demo_csv_task.csv")
        )

    def process_row(self, row):
        logger.info(row)


# 创建任务，启动任务
process = DemoTask(max_workers=1)
process.start()
