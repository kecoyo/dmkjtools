"""
下载到本地, 并删除OSS文件
"""

import os
import oss2
from common.oss_client import oss_client
from common.task import CsvTask


# 切换到工作目录
os.chdir("tmp\\alioss\\")

INPUT_FILE = "download_delete_file.csv"  # 输入文件，格式：key, save_path


class ProcessTask(CsvTask):
    """处理任务"""

    def process_row(self, row):
        try:
            # 下载文件
            oss_client.download_file(row["key"], row["save_path"])
            # 删除OSS文件
            oss_client.delete_object(row["key"])
            row["status"] = "success"
        except oss2.exceptions.NoSuchKey as e:
            row["status"] = "NoSuchKey"
            raise e

        print(row)


process = ProcessTask(INPUT_FILE, max_workers=1)
process.start()
