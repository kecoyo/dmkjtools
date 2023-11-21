import os
from pathlib import Path
from PIL import Image
from common.oss_client import OssClient
from common.request import download_file
from common.task import Task
import common.fs as fs

"""
上传文件到阿里云OSS
"""


local_dir = "tmp\\alioss\\"  # 本地文件夹
oss_dir = "app_res/activity/bbbbbbbb/"  # OSS文件夹


# OSS客户端
oss_client = OssClient(os.getenv("OSS_ENDPOINT"), "file-im")


class ProcessTask(Task):
    def read_list(self):
        list = fs.readdirp(local_dir)
        return [
            {
                "key": oss_dir + str(item).replace(local_dir, "").replace(os.sep, "/"),
                "path": str(item),
            }
            for item in list
        ]

    def process_row(self, row):
        print(row)
        # 上传文件
        oss_client.put_file(row["key"], row["path"])

    def write_list(self, list):
        path = Path(__file__)
        output = path.parent.joinpath(path.stem + ".csv")
        fs.write_csv(output, list)


process = ProcessTask(max_workers=1)
process.start()
