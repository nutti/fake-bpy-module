import os
from typing import List

LOG_LEVEL_DEBUG = 0
LOG_LEVEL_INFO = 1
LOG_LEVEL_NOTICE = 2
LOG_LEVEL_WARN = 3
LOG_LEVEL_ERR = 4

LOG_LEVEL = LOG_LEVEL_WARN


def check_os():
    if os.name == "nt":
        return "Windows"
    elif os.name == "posix":
        return "Linux"


def output_log(level: int, message: str):
    LOG_LEVEL_LABEL: List[str] = ["DEBUG", "INFO", "NOTICE", "WARN", "ERR"]
    if level >= LOG_LEVEL:
        print("[{0}] {1}".format(LOG_LEVEL_LABEL[level], message))


def remove_unencodable(str_: str) -> str:
    """
    :type str_: str
    :param str_: string to remove unencodable character
    :return: string removed unencodable character
    """
    s = str_.replace('\xb2', '')
    s = s.replace('\u2013', '')
    s = s.replace('\u2019', '')
    return s
