import os
import re
import common.fs as fs
from common.logger import logger
from common.request import check_exists
from common.task import Task
from PIL import Image
import pytesseract

"""
magick图片处理
"""

src_dir = "tmp\\image\\"
dest_dir = "tmp\\image_output\\"


class ProcessTask(Task):
    def read_list(self):
        list = fs.readdirp(src_dir)
        return [
            {
                "src": str(item),
                "dest": str(item).replace(src_dir, dest_dir),
            }
            for item in list
        ]

    def process_row(self, row):
        print(row)

        # magick KJ0001.png KJ0001-tuya.jpg # 转换格式 png -> jpg
        # magick KJ0001.png -quality 85 KJ0001-tuya.jpg # 质量压缩 85 为质量
        # magick KJ0001.png  -resize 120x120 KJ0001-tuya.jpg # 缩放 120x120 为宽高
        # magick KJ0001.png  -crop 320x320+10+10 KJ0001-tuya.jpg # 裁剪 320x320+10+10: 320x320是裁剪的宽高，+10+10是裁剪的起始位置


process = ProcessTask(max_workers=1)
process.start()
