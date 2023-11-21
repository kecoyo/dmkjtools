import os
import re
from common.fs import copy_file, ensure_dir, readdir
from common.logger import logger
from common.request import check_exists
from common.task import Task
from PIL import Image
import pytesseract

"""
批量识别图片中的文字，提取证书编号作为文件名
"""

IMG_DIR = "d:\\cert_imgs\\"
OUT_DIR = "d:\\cert_imgs_output\\"

ensure_dir(OUT_DIR)


class ProcessTask(Task):
    def read_list(self):
        files = readdir(IMG_DIR)
        return files

    def process_row(self, row):
        print(row)

        # 打开图像
        image = Image.open(IMG_DIR + row)

        # 使用Tesseract进行文本提取
        text = pytesseract.image_to_string(image, lang="script/HanS")

        # # 输出提取的中文文本
        # print(text)

        find = re.findall(r"([A-Za-z]+\d+)", text)
        if len(find) > 0:
            cert_no = find[0]
            copy_file(IMG_DIR + row, OUT_DIR + cert_no.upper() + ".png")
        else:
            raise Exception("未找到证书编号: " + row)


process = ProcessTask(max_workers=4)
process.start()
