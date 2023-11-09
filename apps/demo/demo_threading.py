import threading
from time import sleep, time


def sing():
    for i in range(3):
        print("正在唱歌。。。。%d" % i)
        sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞。。。%d" % i)
        sleep(1)


if __name__ == "__main__":
    start_time = time()
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    end_time = time()
    print(f"执行时间为：{round(end_time - start_time, 2)}秒")
