import queue

q = queue.Queue()

for item in range(100):
    q.put("The task is {}".format(item))

while not q.empty():
    task = q.get()
    print(task)

print(f"processing task {task}")
