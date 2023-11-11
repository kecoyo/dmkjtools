def merge_dict(dict1, dict2):  # 合并字典
    res = {**dict1, **dict2}
    return res


def merge_dict2(dict1, dict2):  # 合并字典
    return dict1.update(dict2)
