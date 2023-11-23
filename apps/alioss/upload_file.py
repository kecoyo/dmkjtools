"""
上传本地文件到阿里云OSS
"""

import os
from common.oss_client import oss_client
from common.task import CsvTask


# 切换到工作目录
os.chdir(os.path.dirname(__file__))

INPUT_FILE = "upload_file.csv"  # 输入文件, 格式：key, path


class ProcessTask(CsvTask):
    """处理任务"""

    def process_row(self, row):
        # 上传文件
        oss_client.put_file(row["key"], row["path"])

        print(row)


process = ProcessTask(INPUT_FILE, max_workers=1)
process.start()
