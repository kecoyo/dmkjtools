import os

from common.request import check_exists
from common.task import create_csv_task


# 任务处理方法
def process_row(row):
    # print(row)
    # print(dir(row))
    # logger.info("{},{}".format(row["userId"], row["uname"]))
    # row["status"] = "OK"
    # del row["status"]
    # raise Exception("aaa")
    status = check_exists(row["mp4url"])
    row["status"] = status


# 创建Csv任务
create_csv_task(
    os.path.join(os.path.dirname(__file__), "check_res_exists.csv"),
    process_row,
    max_workers=10,
)
