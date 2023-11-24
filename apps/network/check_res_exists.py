"""
检查资源状态
"""

import os
from common.request import check_exists
from common.task import CsvTask


# 切换到工作目录
os.chdir(os.path.dirname(__file__))

INPUT_FILE = "check_res_exists.csv"  # 输入文件, 格式: url


class ProcessTask(CsvTask):
    """处理任务"""

    def process_row(self, row):
        try:
            status = check_exists(row["url"])
            row["status"] = status
            row["error"] = ""
        except Exception as e:
            row["status"] = "failed"
            row["error"] = str(e)
            raise e

        print(row)


if __name__ == "__main__":
    process = ProcessTask(INPUT_FILE, max_workers=1)
    process.start()
