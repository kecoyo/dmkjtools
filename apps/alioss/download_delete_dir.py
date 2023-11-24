"""
下载OSS文件到本地
"""

import os
from pathlib import Path
import oss2
from common.fs import write_csv
from common.oss_client import oss_client
from common.task import Task


# 切换到工作目录
os.chdir(os.path.dirname(__file__))

OSS_DIR = "app_res/activity/aaaaaaaa/"  # 要下载删除的OSS文件夹
LOCAL_DIR = "download\\"  # 本地保存的文件夹
MAX_KEYS = 1000  # 最大数量


class ProcessTask(Task):
    """处理任务"""

    def read_list(self):
        objects = oss_client.list_object(prefix=OSS_DIR, max_keys=MAX_KEYS)
        return [
            {
                "key": item.key,
                "path": LOCAL_DIR + item.key.replace(OSS_DIR, "", 1).replace("/", os.sep),
            }
            for item in objects
            if not item.key.endswith("/")
        ]

    def process_row(self, row):
        try:
            # 下载文件
            oss_client.download_file(row["key"], row["path"])

            # 删除OSS文件
            oss_client.delete_object(row["key"])

            row["status"] = "success"
        except oss2.exceptions.OssError as e:
            row["status"] = e.status
            row["error"] = e.message
            raise e
        except Exception as e:
            row["status"] = "failed"
            row["error"] = str(e)
            raise e

        print(row)

    def write_list(self):
        path = Path(__file__)
        write_csv(path.stem + ".csv", self.list)


if __name__ == "__main__":
    process = ProcessTask(max_workers=1)
    process.start()
