"""
magick图片处理
"""

import os
import subprocess
from common.fs import readdirp
from common.task import Task


# 切换到工作目录
os.chdir(os.path.dirname(__file__))

INPUT_DIR = "input\\"  # 源目录
OUTPUT_DIR = "output\\"  # 目标目录
QUALITY = 85  # 85 为质量
RESIZE = None  # "120x120"
CROP = None  # "320x320+10+10"
FORMAT = "jpg"  # "jpg"


class ProcessTask(Task):
    """处理任务"""

    def read_list(self):
        files = readdirp(INPUT_DIR)
        return [
            {
                "src": str(item),
                "dest": str(item).replace(INPUT_DIR, OUTPUT_DIR),
            }
            for item in files
        ]

    def process_row(self, row):
        # magick KJ0001.png KJ0001-tuya.jpg # 转换格式 png -> jpg
        # magick KJ0001.png -quality 85 KJ0001-tuya.jpg # 质量压缩 85 为质量
        # magick KJ0001.png  -resize 120x120 KJ0001-tuya.jpg # 缩放 120x120 为宽高
        # magick KJ0001.png  -crop 320x320+10+10 KJ0001-tuya.jpg # 裁剪 320x320+10+10: 320x320是裁剪的宽高，+10+10是裁剪的起始位置

        cmd = f'magick "{row["src"]}" '
        if QUALITY:
            cmd += f"-quality {QUALITY} "
        if RESIZE:
            cmd += f'-resize "{RESIZE}" '
        if CROP:
            cmd += f'-crop "{CROP}" '
        if FORMAT:
            cmd += f'-format "{FORMAT}" '
            # 把row["dest"]的后缀改为FORMAT
            row["dest"] = os.path.splitext(row["dest"])[0] + "." + FORMAT

        cmd += f'"{row["dest"]}"'
        print(cmd)

        p = subprocess.run(cmd, shell=True, check=True, capture_output=True, encoding="utf-8")
        row["returncode"] = p.returncode
        row["stdout"] = p.stdout
        row["stderr"] = p.stderr

        print(row)


if __name__ == "__main__":
    process = ProcessTask(max_workers=1)
    process.start()
