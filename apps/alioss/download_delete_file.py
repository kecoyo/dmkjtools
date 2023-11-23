"""
下载到本地, 并删除OSS文件
"""

import os
from common.oss_client import oss_client
from common.task import CsvTask


# 切换到工作目录
os.chdir(os.path.dirname(__file__))

INPUT_FILE = "download_delete_file.csv"  # 输入文件，格式：key, path


class ProcessTask(CsvTask):
    """处理任务"""

    def process_row(self, row):
        print(row)

        try:
            # 下载文件
            oss_client.download_file(row["key"], row["path"])
            # 删除OSS文件
            oss_client.delete_object(row["key"])
            row["status"] = "success"
            row["error"] = ""
        except Exception as e:
            row["status"] = "failed"
            row["error"] = str(e)
            raise e


process = ProcessTask(INPUT_FILE, max_workers=1)
process.start()
