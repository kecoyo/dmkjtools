from common.request import download_file
from common.task import create_task


# 任务处理方法
def process_row(i, row):
    download_file(
        "https://fileimosscdn.lejiaolexue.com/dmres/1/15d38b3b6de83b03a9c8c4b744a29564.pptx",
        f"d:/output/test/1/1_{row}.pptx",
    )


# 创建简单任务
create_task(lambda: range(10), process_row, max_workers=4)
