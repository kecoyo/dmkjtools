import os
from pathlib import Path
from common.fs import readdirp, write_csv
from common.oss_client import OssClient
from common.task import Task

"""
上传文件到阿里云OSS
"""


work_dir = os.getenv("ALIOSS_WORK_DIR")  # 工作目录
local_dir = os.getenv("ALIOSS_LOCAL_DIR")  # 本地文件夹
oss_dir = os.getenv("ALIOSS_OSS_DIR")  # OSS文件夹
max_keys = os.getenv("ALIOSS_MAX_KEYS")  # 最大数量

# OSS客户端
oss_client = OssClient(os.getenv("OSS_ENDPOINT"), os.getenv("OSS_BUCKET"))


class ProcessTask(Task):
    def read_list(self):
        list = readdirp(local_dir)
        return [
            {
                "path": str(item),
                "key": oss_dir + str(item).replace(local_dir, "").replace(os.sep, "/"),
            }
            for item in list
        ]

    def process_row(self, row):
        print(row)

        # 上传文件
        oss_client.put_file(row["key"], row["path"])

    def write_list(self, list):
        path = Path(__file__)
        write_csv(os.path.join(work_dir, path.stem + ".csv"), list)


process = ProcessTask(max_workers=1)
process.start()
