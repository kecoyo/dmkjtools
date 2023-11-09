"""
Demonstrates how to use the blocking scheduler to schedule a job that executes on 3 second
intervals.
"""

import os
from datetime import datetime
from time import sleep

from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from apscheduler.schedulers.blocking import BlockingScheduler


def process_row(row):
    print(row, "The time is: %s" % datetime.now())
    sleep(1)


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    success = 0
    fail = 0


    def my_listener(event):
        global success, fail
        if event.exception:
            print("The job crashed :(")  # or logger.fatal('The job crashed :(')
            fail += 1
        else:
            print("The job worked :)")
            success += 1

        if success + fail == 10:
            sleep(2)
            # scheduler.remove_listener(my_listener)
            scheduler.shutdown(wait=False)


    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

    for x in range(10):
        scheduler.add_job(process_row, args=[{id: x}])

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

    print("Press Ctrl+{0} to exit".format("Break" if os.name == "nt" else "C"))
