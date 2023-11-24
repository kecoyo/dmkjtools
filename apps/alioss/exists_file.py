"""
OSS文件是否存在
"""

import os
from common.oss_client import oss_client
from common.task import CsvTask


# 切换到工作目录
os.chdir(os.path.dirname(__file__))

INPUT_FILE = "exists_file.csv"  # 输入文件，格式：key


class ProcessTask(CsvTask):
    """处理任务"""

    def process_row(self, row):
        # 下载文件
        try:
            exists = oss_client.object_exists(row["key"])
            row["status"] = exists and "exists" or "not_exists"
            row["error"] = ""
        except Exception as e:
            row["status"] = "failed"
            row["error"] = str(e)
            raise e

        print(row)


if __name__ == "__main__":
    process = ProcessTask(INPUT_FILE, max_workers=1)
    process.start()
