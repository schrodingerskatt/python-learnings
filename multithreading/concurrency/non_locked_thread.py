import time
import random

from threading import Thread
counter = 0

def increment_counter():
    global counter
    time.sleep(random.random())
    counter+=1
    time.sleep(random.random())
    print(f'New counter value:{counter}')
    time.sleep(random.random())
    print('----------------------------')

for x in range(10):
    t = Thread(target = increment_counter)
    time.sleep(random.random())
    t.start()

'''OUTPUT

New counter value:1
New counter value:2
----------------------------
----------------------------
New counter value:3
New counter value:5
New counter value:5
----------------------------
----------------------------
----------------------------
New counter value:7
----------------------------
New counter value:9
New counter value:9
----------------------------
----------------------------
New counter value:10
----------------------------
New counter value:10
----------------------------

We can see the problem here, multiple threads are trying to access, same global value at the same time,
we can see the problem by using time.sleep(random.random()), If we want this to happen sequentially
we have to use concept of queuing in thread.
'''