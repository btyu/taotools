# WSILATools
# Websoft, Nanjing University
# Author: YU Botao


import json
import os

from taotools.file import ensure_dirs


def json_save(obj, file_path: str, indent: int = 4, ensure_ascii: bool = False, newline: str = '\n'):
    """
    保存变量为JSON格式，若目标路径不存在将会自动创建。

    :param obj: object，待保存的变量。
    :param file_path: str，JSON文件的路径。
    :param indent: int，缩进大小。
    :param ensure_ascii: bool，确保文件仅包括ASCII字符。
    :param newline: str，换行符，默认统一为"\n"。
    :return:
    """
    dir_name = os.path.dirname(file_path)
    ensure_dirs(dir_name)
    with open(file_path, 'w', encoding='utf-8', newline=newline) as f:
        json.dump(obj, f, indent=indent, ensure_ascii=ensure_ascii)


def json_load(file_path):
    """
    加载JSON文件。

    :param file_path: str，JSON文件路径。
    :return:
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        obj = json.load(f)
    return obj
