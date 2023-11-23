"""
上传本地目录到OSS目录
"""

import os
from pathlib import Path
from common.fs import readdirp, write_csv
from common.oss_client import oss_client
from common.task import Task


# 切换到工作目录
os.chdir("tmp\\alioss\\")

LOCAL_DIR = "aaaaaaaa\\"  # 本地要上传的目录
OSS_DIR = "app_res/activity/aaaaaaaa/"  # 要保存的OSS目录


class ProcessTask(Task):
    """处理任务"""

    def read_list(self):
        files = readdirp(LOCAL_DIR)
        return [
            {
                "path": str(item),
                "key": OSS_DIR + str(item).replace(LOCAL_DIR, "").replace(os.sep, "/"),
            }
            for item in files
        ]

    def process_row(self, row):
        # 上传文件
        oss_client.put_file(row["key"], row["path"])

        print(row)

    def write_list(self):
        path = Path(__file__)
        write_csv(path.stem + ".csv", self.list)


process = ProcessTask(max_workers=1)
process.start()
