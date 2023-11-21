import os
from pathlib import Path
from PIL import Image
from common.oss_client import OssClient
from common.request import download_file
from common.task import Task
import common.fs as fs

"""
列出指定目录下的所有文件
"""

local_dir = "tmp\\alioss\\"  # 本地文件夹
oss_dir = "app_res/activity/bbbbbbbb/app_res/activity/cert_imgs/"  # OSS文件夹


# OSS客户端
oss_client = OssClient(os.getenv("OSS_ENDPOINT"), "file-im")


class ProcessTask(Task):
    def read_list(self):
        list = oss_client.list_object(prefix=oss_dir, max_keys=1000)
        return [
            {
                "key": item.key,
                "path": local_dir + item.key.replace(oss_dir, "").replace("/", os.sep),
            }
            for item in list
            if not item.key.endswith("/")
        ]

    def process_row(self, row):
        print(row)

        # 下载文件
        oss_client.download_file(row["key"], row["path"])

    def write_list(self, list):
        path = Path(__file__)
        output = path.parent.joinpath(path.stem + ".csv")
        fs.write_csv(output, list)


process = ProcessTask(max_workers=1)
process.start()
