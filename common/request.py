import os
import time

import requests

import common.fs as fs
from common.logger import logger


def check_exists(url):
    """
    检查url状态

    :param url: 文件的URL
    :returns 响应状态码
    """
    logger.info("Requesting [{}]".format(url))
    t0 = time.time()

    status_code = 200
    try:
        res = requests.head(url)
        status_code = res.status_code
    except Exception as e:
        status_code = 500

    t1 = time.time()
    logger.info(
        "Request completed. [{}] runs {:.2f} seconds.".format(status_code, t1 - t0)
    )

    return status_code


def get_json(url, params=None, **kwargs):
    """
    Sends a GET request, and return json.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    """
    res = requests.get(url, params=params, **kwargs)
    return res.json()


def post_json(url, data=None, json=None, **kwargs):
    """
    Sends a POST request, and return json.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    """
    res = requests.post(url, data=data, json=json, **kwargs)
    return res.json()


def get_text(url, params=None, **kwargs):
    """
    Sends a GET request, and return json.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    """
    res = requests.get(url, params=params, **kwargs)
    return res.text


def post_text(url, data=None, json=None, **kwargs):
    """
    Sends a POST request, and return json.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    """
    res = requests.post(url, data=data, json=json, **kwargs)
    return res.text


def download_file(url, filepath):  # 下载文件
    """下载文件

    :param url: 文件的URL
    :param filepath: 文件的保存路径
    :returns
    """
    logger.info("Downloading [{}]".format(url))
    t0 = time.time()

    res = requests.get(url)
    if fs.exists_dir(filepath):  # 如果传入参数是目录，则拼上url中的文件名，否则，使用传入文件路径
        filename = os.path.split(url)[1]
        filepath = os.path.join(filepath, filename)
    with open(filepath, "wb") as f:
        f.write(res.content)

    t1 = time.time()
    logger.info("Download completed. [{}] runs {:.2f} seconds.".format(url, t1 - t0))


# download_file(
#     "https://fileimosscdn.lejiaolexue.com/dmres/1/15d38b3b6de83b03a9c8c4b744a29564.pptx",
#     "d:/output/test/1234.pptx",
# )


# check_exists(
#     "https://fileimosscdn.lejiaolexue.com/dmres/1/15d38b3b6de83b03a9c8c4b744a29564.pptx"
# )
