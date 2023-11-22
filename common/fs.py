#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. 利用os模块编写一个能实现dir -l输出的程序。
# 2. 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

import json
import os
import shutil
from pathlib import Path

import pandas as pd


def exists(path):  # 判断目录或文件是否存在
    return os.path.exists(path)


def exists_dir(path):  # 判断目录是否存在
    return os.path.exists(path) and os.path.isdir(path)


def create_dir(name):  # 创建目录
    if name and not os.path.exists(name):
        # 使用 os.mkdir 创建目录，如果父目录不存在，报错；
        # 如果目录已经存在了，报错。
        # os.mkdir(name)

        # 使用 os.makedirs 递归创建目录，如果目录已经存在了，报错。
        os.makedirs(name)


def ensure_dir(name):  # 确保目录存在
    if name and not os.path.exists(name):
        # 使用 os.mkdir 创建目录，如果父目录不存在，报错；
        # 如果目录已经存在了，报错。
        # os.mkdir(name)

        # 使用 os.makedirs 递归创建目录，如果目录已经存在了，报错。
        os.makedirs(name)


def remove_dir(name):  # 删除目录
    if os.path.exists(name):
        # os.rmdir(name) # 删除目录
        shutil.rmtree(name)  # 递归删除目录


def move_dir(src, dest):  # 移动或重命名目录
    dest_dir = os.path.dirname(dest)
    create_dir(dest_dir)
    shutil.move(src, dest)


def copy_dir(src, dest):  # 拷贝目录
    dest_dir = os.path.dirname(dest)
    create_dir(dest_dir)
    shutil.copytree(src, dest, dirs_exist_ok=True)


def exists_file(path):  # 判断文件是否存在
    return os.path.exists(path) and os.path.isfile(path)


def remove_file(path):  # 删除文件
    if os.path.exists(path):
        os.remove(path)


def move_file(src, dest):  # 移动或重命名文件
    dest_dir = os.path.dirname(dest)
    create_dir(dest_dir)
    shutil.move(src, dest)


def copy_file(src, dest):  # 拷贝文件
    dest_dir = os.path.dirname(dest)
    create_dir(dest_dir)
    shutil.copy2(src, dest)


def get_file_stat(file):  # 获取文件
    stat = os.stat(file)
    return stat


def get_file_size(file):  # 获取文件大小
    stats = os.stat(file)
    return stats.st_size


def readdir(dir, pattern="*.*"):  # 读目录
    """
    读目录

    :param dir: 目录
    :param pattern: 匹配模式，如 *.jpg, *.*, */, 默认为 *.*
    :return: 文件或目录列表
    """
    files = [file for file in Path(dir).glob(pattern)]
    return files


def readdirp(dir, pattern="*.*"):  # 读目录
    """
    递归读取目录

    :param dir: 目录
    :param pattern: 匹配模式，如 *.jpg, *.*, */, 默认为 *.*
    :return: 文件或目录列表
    """
    files = [file for file in Path(dir).rglob(pattern)]
    return files


def read_bytes(file):  # 读bytes文件
    return Path(file).read_bytes()


def write_bytes(file, data):  # 写bytes文件
    Path(file).write_bytes(data)


def read_text(file):  # 读text文件
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        return content


def write_text(file, data):  # 写text文件
    # 要确保目录存在
    file_dir = os.path.dirname(file)
    create_dir(file_dir)

    # 写文件
    f = open(file, "w", encoding="utf-8")
    f.write(data)
    f.close()


def read_json(file):  # 读Json文件
    with open(file, "r") as f:
        data = json.load(f)
        return data


def write_json(file, data):  # 写Json文件
    # 要确保目录存在
    file_dir = os.path.dirname(file)
    create_dir(file_dir)

    with open(file, "w") as f:
        json.dump(data, f)


def read_csv(file):  # 读csv文件
    df = pd.read_csv(file, encoding="utf-8")
    records = df.to_dict(orient="records")
    return records


def write_csv(file, data):  # 写csv文件
    # 要确保目录存在
    file_dir = os.path.dirname(file)
    create_dir(file_dir)

    df = pd.DataFrame(data)
    df.to_csv(file, encoding="utf-8", index=False)


def read_excel(file):  # 读excel文件
    df = pd.read_excel(file)
    records = df.to_records()
    return records


def write_excel(file, data):  # 写excel文件
    # 要确保目录存在
    file_dir = os.path.dirname(file)
    create_dir(file_dir)

    df = pd.DataFrame(data)
    df.to_excel(file, index=False)
