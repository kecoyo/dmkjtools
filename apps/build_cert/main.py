"""
批量生成活动证书
"""

import os
from PIL import Image, ImageDraw, ImageFont
from common.fs import ensure_dir
from common.pillow import wrap_texts
from common.task import CsvTask


# 切换到工作目录
# os.chdir(sys.path[0])
os.chdir(os.path.dirname(__file__))

INPUT_FILE = "data_03.csv"  # 输入文件, 格式: key
OUTPUT_DIR = "images\\"  # 输出目录


class ProcessTask(CsvTask):
    """生成证书的处理任务的类"""

    def process_row(self, row):
        print(row)

        # 创建一个白色背景的空白图像
        img = Image.new("RGB", (3509, 2482), color="white")

        # 打开背景图，将背景图覆盖在空白图像上
        bg_img = Image.open(os.path.join(os.path.dirname(__file__), "bg.png"))
        img.paste(bg_img, (0, 0))

        # 在图像上创建一个Draw对象
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype("simsun.ttc", 91.67)

        text_color = (0, 0, 0)
        spacing = 50  # 行间隙

        # 写文本：证书编号
        text = f"证书编号：{row['cert_no']}"
        text_position = (2415, 824)
        draw.text(text_position, text, font=font, fill=text_color)

        # 写文本：内容信息
        texts = [
            f"{row['school']} {row['name']}：",
            f"    你在中国教育技术协会中小学专业委员会主办的2023智慧教育应用成果征集与推荐展示活动中，提交的{row['title']}",
            "    特发此证。",
        ]
        lines = wrap_texts(texts, draw, font, max_width=2743)
        text = "\n".join(lines)
        text_position = (376, 988)
        draw.multiline_text(text_position, text, font=font, fill=text_color, spacing=spacing)

        # 写文本：中国教育技术协会
        text = "中国教育技术协会\n中小学专业委员会\n2023年10月"
        text_position = (2269, 1759)
        draw.multiline_text(
            text_position,
            text,
            font=font,
            align="center",
            fill=text_color,
            spacing=spacing,
        )

        # 确保输出目录存在
        ensure_dir(OUTPUT_DIR)

        # 保存图像到文件
        img.save(OUTPUT_DIR + row["cert_no"] + ".png")


process = ProcessTask(INPUT_FILE, max_workers=1)
process.start()
