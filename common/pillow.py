def wrap_text(text, draw, font, max_width):
    """
    一行文本换行，将一行文本拆分成多行文本。

    :param text: 要拆分的文本
    :param draw: 图像绘制对象，用于计算文本长度。
    :param font: 文本字体，使用字体的大小，用于计算文本长度。
    :param max_width: 文本区域的最大宽度。
    :returns: 拆分后多行文本的数组。
    """

    lines = []
    line = ""
    for char in list(text):
        if draw.textlength(line, font=font) < max_width:
            line += char
        else:
            if char in [",", "，", ".", "。", "!", "！", "”", "》"]:
                line += char
            else:
                lines.append(line)
                line = char

    lines.append(line)
    return lines


def wrap_texts(texts, draw, font, max_width):
    """
    多行文本换行，将一行文本拆分成多行文本。

    :param text: 要拆分的文本
    :param draw: 图像绘制对象，用于计算文本长度。
    :param font: 文本字体，使用字体的大小，用于计算文本长度。
    :param max_width: 文本区域的最大宽度。
    :returns: 拆分后多行文本的数组。
    """

    lines = []
    for text in texts:
        lines += wrap_text(text, draw, font, max_width)

    return lines
