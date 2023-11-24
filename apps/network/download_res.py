"""
检查资源状态
"""

import os
from common.request import download_file
from common.task import CsvTask


# 切换到工作目录
os.chdir(os.path.dirname(__file__))

INPUT_FILE = "download_res.csv"  # 输入文件, 格式: url, path
OUTPUT_DIR = "download\\"  # 输出目录


class ProcessTask(CsvTask):
    """处理任务"""

    def process_row(self, row):
        try:
            if self.is_empty(row["path"]):
                row["path"] = row["url"].split("/")[-1]

            download_file(row["url"], OUTPUT_DIR + row["path"])

            row["status"] = "success"
            row["error"] = ""
        except Exception as e:
            row["status"] = "failed"
            row["error"] = str(e)
            raise e

        print(row)


if __name__ == "__main__":
    process = ProcessTask(INPUT_FILE, max_workers=1)
    process.start()
