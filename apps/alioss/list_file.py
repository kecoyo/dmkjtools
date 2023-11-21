import os
from pathlib import Path
from PIL import Image
from common.oss_client import OssClient
from common.task import Task
import common.fs as fs

"""
列出指定目录下的所有文件
"""

oss_dir = "app_res/activity/bbbbbbbb/"  # OSS文件夹


# OSS客户端
oss_client = OssClient(os.getenv("OSS_ENDPOINT"), "file-im")


class ProcessTask(Task):
    def read_list(self):
        list = oss_client.list_object(prefix=oss_dir, max_keys=1000)
        return [{"key": item.key} for item in list if not item.key.endswith("/")]

    def process_row(self, row):
        print(row)

    def write_list(self, list):
        path = Path(__file__)
        output = path.parent.joinpath(path.stem + ".csv")
        fs.write_csv(output, list)


process = ProcessTask(max_workers=1)
process.start()
