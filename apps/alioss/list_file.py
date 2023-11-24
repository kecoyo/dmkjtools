"""
列出OSS目录下的文件
"""

import os
from pathlib import Path
from common.fs import write_csv
from common.oss_client import oss_client
from common.task import Task


# 切换到工作目录
os.chdir(os.path.dirname(__file__))

OSS_DIR = "app_res/activity/aaaaaaaa/"  # OSS目录
MAX_KEYS = 1000  # 最大数量


class ProcessTask(Task):
    """处理任务"""

    def read_list(self):
        data = oss_client.list_object(prefix=OSS_DIR, max_keys=MAX_KEYS)
        return [{"key": item.key} for item in data]

    def process_row(self, row):
        print(row)

    def write_list(self):
        path = Path(__file__)
        write_csv(path.stem + ".csv", self.list)


if __name__ == "__main__":
    process = ProcessTask(max_workers=1)
    process.start()
