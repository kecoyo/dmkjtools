__config = None

"""
配置文件读取
"""


def get_config():
    global __config

    if __config is None:
        from configparser import ConfigParser

        __config = ConfigParser()
        __config.read(["config.ini", "config.cfg", "config.conf"])

    return __config


def get_sections():
    config = get_config()
    return config.sections()


def get_items(section):
    config = get_config()
    return config.items(section)


def get(section, option):
    config = get_config()
    return config.get(section, option)
