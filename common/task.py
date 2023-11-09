from time import time

from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import utc

from common.fs import read_csv, write_csv
from common.logger import logger


class Task:
    success = 0  # 成功个数
    fail = 0  # 失败个数

    def __init__(self, input, process_row, max_workers=1, on_completed=None):
        self.input = input  # 输入函数
        self.process_row = process_row  # 处理函数
        self.max_workers = max_workers  # 最大线程数
        self.on_completed = on_completed  # 全部处理完成后执行的函数

        jobstores = {
            "default": MemoryJobStore(),  # 默认内存任务
        }
        executors = {
            "default": ThreadPoolExecutor(max_workers=self.max_workers),  # 默认线程数
        }
        job_defaults = {
            "coalesce": False,  # 是否合并执行
            "max_instances": 3,  # 最大实例数
            "misfire_grace_time": None,  # 不管多晚都允许作业运行
        }

        self.scheduler = BlockingScheduler(
            jobstores=jobstores,
            executors=executors,
            job_defaults=job_defaults,
            timezone=utc,
        )

        self.scheduler.add_listener(
            self.job_event_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR
        )

    def job_event_listener(self, event):
        if event.exception:
            self.fail += 1
        else:
            self.success += 1

        if self.success + self.fail == len(self.list):
            self.scheduler.shutdown(wait=False)

    # 开始运行
    def run(self):
        start_time = time()  # 开始时间
        self.read_data()
        self.process()
        self.write_data()
        end_time = time()  # 结束时间
        logger.info(
            f"执行完成。成功: {self.success}, 失败: {self.fail}, 用时：{round(end_time - start_time, 3)}s"
        )
        self.completed()

    # 读数据
    def read_data(self):
        if callable(self.input):
            self.list = self.input()
        else:
            raise Exception("options.input must be a function.")

    # 写数据
    def write_data(self):
        pass

    # 处理整个过程
    def process(self):
        for item in self.list:
            self.scheduler.add_job(self.process_row, args=[item])

        try:
            self.scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass

    # 处理完成
    def completed(self):
        if self.on_completed:
            self.on_completed(self)


class CsvTask(Task):
    def __init__(self, input, process_row, max_workers=1, on_completed=None):
        super().__init__(input, process_row, max_workers, on_completed)

    def read_data(self):
        self.list = read_csv(self.input)

    def write_data(self):
        write_csv(self.input, self.list)


def create_task(input, process_row, **kwargs):
    Task(input, process_row, **kwargs).run()


def create_csv_task(input, processRow, **kwargs):
    CsvTask(input, processRow, **kwargs).run()
