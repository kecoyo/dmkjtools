"""
删除指定的OSS文件
"""

import os
from common.oss_client import oss_client
from common.task import CsvTask


# 切换到工作目录
os.chdir("tmp\\alioss\\")

INPUT_FILE = "delete_file.csv"  # 输入文件, 格式: key


class ProcessTask(CsvTask):
    """处理任务"""

    def process_row(self, row):
        # 删除OSS文件
        oss_client.delete_object(row["key"])

        row["status"] = "ok"

        print(row)


process = ProcessTask(INPUT_FILE, max_workers=1)
process.start()
