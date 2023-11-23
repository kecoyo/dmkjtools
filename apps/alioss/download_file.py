"""
下载OSS文件到本地
"""

import os
from common.oss_client import oss_client
from common.task import CsvTask


# 切换到工作目录
os.chdir("tmp\\alioss\\")

INPUT_FILE = "download_file.csv"  # 输入文件，格式：key, save_path


class ProcessTask(CsvTask):
    """处理任务"""

    def process_row(self, row):
        print(row)

        # 下载文件
        oss_client.download_file(row["key"], row["save_path"])


process = ProcessTask(INPUT_FILE, max_workers=1)
process.start()
