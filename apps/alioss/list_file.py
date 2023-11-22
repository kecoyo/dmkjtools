import os
from pathlib import Path
from common.fs import write_csv
from common.oss_client import OssClient
from common.task import Task

"""
列出OSS文件
"""

work_dir = os.getenv("ALIOSS_WORK_DIR")  # 工作目录
local_dir = os.getenv("ALIOSS_LOCAL_DIR")  # 本地文件夹
oss_dir = os.getenv("ALIOSS_OSS_DIR")  # OSS文件夹
max_keys = os.getenv("ALIOSS_MAX_KEYS")  # 最大数量


# OSS客户端
oss_client = OssClient(os.getenv("OSS_ENDPOINT"), os.getenv("OSS_BUCKET"))


class ProcessTask(Task):
    def read_list(self):
        list = oss_client.list_object(prefix=oss_dir, max_keys=int(max_keys))
        return [{"key": item.key} for item in list]

    def process_row(self, row):
        print(row)

    def write_list(self, list):
        path = Path(__file__)
        write_csv(work_dir + path.stem + ".csv", list)


process = ProcessTask(max_workers=1)
process.start()
