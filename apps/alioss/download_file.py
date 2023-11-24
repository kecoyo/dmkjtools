"""
下载OSS文件到本地
"""

import os
from common.oss_client import oss_client
from common.task import CsvTask


# 切换到工作目录
os.chdir(os.path.dirname(__file__))

INPUT_FILE = "download_file.csv"  # 输入文件，格式：key, path


class ProcessTask(CsvTask):
    """处理任务"""

    def process_row(self, row):
        print(row)

        # 下载文件
        try:
            oss_client.download_file(row["key"], row["path"])
            row["status"] = "success"
            row["error"] = ""
        except Exception as e:
            row["status"] = "failed"
            row["error"] = str(e)
            raise e


if __name__ == "__main__":
    process = ProcessTask(INPUT_FILE, max_workers=1)
    process.start()
