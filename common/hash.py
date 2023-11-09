import hashlib


def str_md5(str):  # 获取字符串的md5
    m = hashlib.md5()
    m.update(str.encode("utf-8"))
    return m.hexdigest()


def file_md5(file):  # 获取文件的md5
    with open(file, "rb") as f:
        content = f.read()
        m = hashlib.md5()
        m.update(content)
        return m.hexdigest()
