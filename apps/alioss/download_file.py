import os
from pathlib import Path
from common.fs import write_csv
from common.oss_client import OssClient
from common.task import Task

"""
下载OSS文件到本地
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
        return [
            {
                "key": item.key,
                "path": local_dir + item.key.replace(oss_dir, "", 1).replace("/", os.sep),
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
        write_csv(os.path.join(work_dir, path.stem + ".csv"), list)


process = ProcessTask(max_workers=1)
process.start()
