import os

from common.logger import logger
from common.task import create_csv_task


# 任务处理方法
def process_row(row):
    # print(row)
    # print(dir(row))
    logger.info("{},{}".format(row["userId"], row["uname"]))
    row["status"] = "OK"
    # raise Exception("aaa")


# 创建Csv任务
create_csv_task(
    os.path.join(os.path.dirname(__file__), "check_res_exists.csv"),
    process_row,
    max_workers=1,
)
