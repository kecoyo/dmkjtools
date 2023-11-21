import os
import sys
from time import time

from abc import ABCMeta, abstractmethod
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from pytz import utc

from common.fs import read_csv, write_csv

# from common.logger import logger


class Task:

    """
    简单多线程任务

    :param max_workers: 线程的最大数量
    """

    __meta_class__ = ABCMeta

    def __init__(self, max_workers=1):
        self.list = []  # 任务列表
        self.success = 0  # 成功任务数
        self.fail = 0  # 失败任务数

        self.jobstores = {
            "default": MemoryJobStore(),  # 默认内存任务
        }
        self.executors = {
            "default": ThreadPoolExecutor(max_workers=max_workers),  # 默认线程数
        }
        self.job_defaults = {
            "coalesce": False,  # 是否合并执行
            "max_instances": 3,  # 最大实例数
            "misfire_grace_time": None,  # 不管多晚都允许作业运行
        }
        self.scheduler = BlockingScheduler(
            jobstores=self.jobstores,
            executors=self.executors,
            job_defaults=self.job_defaults,
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
    def start(self):
        start_time = time()  # 开始时间
        self.list = self.read_list()
        self.process()
        self.write_list(self.list)
        end_time = time()  # 结束时间

        print(
            f"执行完成。成功: {self.success}, 失败: {self.fail}, 用时：{round(end_time - start_time, 3)}s"
        )

    # 读数据
    def read_list(self):
        return []

    # 写数据
    def write_list(self, list):
        pass

    # 处理整个过程
    def process(self):
        if len(self.list) == 0:  # 列表中没有任务，不启动
            return

        for item in self.list:
            self.scheduler.add_job(self.process_row, args=[item])

        try:
            self.scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass

    # 处理单个任务
    @abstractmethod
    def process_row(self, row):
        pass


class CsvTask(Task):
    # 输入csv文件路径
    input = ""

    def read_list(self):
        # 默认csv文件和py文件同名
        if self.input == "":
            self.input = sys.argv[0].replace(".py", ".csv")

        return read_csv(self.input)

    def write_list(self, list):
        write_csv(self.input, list)
