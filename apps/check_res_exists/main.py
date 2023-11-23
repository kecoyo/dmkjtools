import os

from common.logger import logger
from common.request import check_exists
from common.task import CsvTask

"""
检查资源状态
"""


class CheckResExistsTask(CsvTask):
    input = os.path.join(os.path.dirname(__file__), "data.csv")

    def process_row(self, row):
        # status = check_exists(row["url"])
        # row["status"] = status
        print(row)


process = CheckResExistsTask()
process.start()
