import os
from PIL import Image
from common.oss_client import OssClient
from common.task import Task
import common.fs as fs
from pathlib import Path

"""
列出OSS存储桶
"""


# OSS客户端
oss_client = OssClient(os.getenv("OSS_ENDPOINT"), "file-im")


class ProcessTask(Task):
    def read_list(self):
        list = [{"name": item.name} for item in oss_client.list_bucket()]
        return list

    def process_row(self, row):
        print(row)

    def write_list(self, list):
        path = Path(__file__)
        output = path.parent.joinpath(path.stem + ".csv")
        fs.write_csv(output, list)


process = ProcessTask(max_workers=1)
process.start()
