import random
import time
import queue

from threading import Thread

counter = 0
job_queue = queue.Queue() # things to be printed out
counter_queue = queue.Queue() # amounts by which counter should increase

def increment_manager():
    global counter
    while True:
        increment = counter_queue.get() # This waits until an item is available and then locks it
        time.sleep(random.random())
        old_counter = counter
        time.sleep(random.random())
        counter = old_counter+increment
        time.sleep(random.random())
        job_queue.put((f'New Counter Value is {counter}', '--------'))
        time.sleep(random.random())
        counter_queue.task_done() # unlock queue

Thread(target=increment_manager, daemon=True).start()

def print_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()

Thread(target = print_manager, daemon=True).start()

def increment_counter():
    counter_queue.put(1)

worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    thread.start()

for thread in worker_threads:
    thread.join()

counter_queue.join()
job_queue.join()