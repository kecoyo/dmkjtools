import os
import subprocess
from pathlib import Path
from common.fs import readdirp, write_csv
from common.task import Task

"""
magick图片处理
"""
work_dir = "tmp\\image\\"
os.chdir(work_dir)

src_dir = "input\\"  # 源目录
dest_dir = "output\\"  # 目标目录
quality = 85  # 85 为质量
resize = None  # "120x120"
crop = None  # "320x320+10+10"


class ProcessTask(Task):
    def read_list(self):
        list = readdirp(src_dir)
        return [
            {
                "src": str(item),
                "dest": str(item).replace(src_dir, dest_dir),
            }
            for item in list
        ]

    def process_row(self, row):
        # magick KJ0001.png KJ0001-tuya.jpg # 转换格式 png -> jpg
        # magick KJ0001.png -quality 85 KJ0001-tuya.jpg # 质量压缩 85 为质量
        # magick KJ0001.png  -resize 120x120 KJ0001-tuya.jpg # 缩放 120x120 为宽高
        # magick KJ0001.png  -crop 320x320+10+10 KJ0001-tuya.jpg # 裁剪 320x320+10+10: 320x320是裁剪的宽高，+10+10是裁剪的起始位置

        cmd = f'magick "{row["src"]}" '
        if quality:
            cmd += f"-quality {quality} "
        if resize:
            cmd += f'-resize "{resize}" '
        if crop:
            cmd += f'-crop "{crop}" '
        cmd += f'"{row["dest"]}"'
        print("$", cmd)

        p = subprocess.run(cmd, shell=True, capture_output=True, encoding="utf-8")
        row["returncode"] = p.returncode
        row["stdout"] = p.stdout
        row["stderr"] = p.stderr

        print(row)

    def write_list(self):
        path = Path(__file__)
        write_csv(path.stem + ".csv", self.list)


process = ProcessTask(max_workers=1)
process.start()
