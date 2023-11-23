"""
列出OSS存储桶
"""

import os
from pathlib import Path
from common.fs import write_csv
from common.oss_client import oss_client
from common.task import Task


# 切换到工作目录
os.chdir(os.path.dirname(__file__))


class ProcessTask(Task):
    """处理任务"""

    def read_list(self):
        buckets = [{"name": item.name} for item in oss_client.list_bucket()]
        return buckets

    def process_row(self, row):
        print(row)

    def write_list(self):
        path = Path(__file__)
        write_csv(path.stem + ".csv", self.list)


process = ProcessTask(max_workers=1)
process.start()
