import time
from threading import Thread

def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask user, {time.time()-start}')

def complex_calculation():
    start = time.time()
    print('Started Calculating')
    [x**2 for x in range(20000000)]
    print(f'complex calculation, {time.time()-start}')

# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')

thread1 = Thread(target = complex_calculation) 
thread2 = Thread(target= ask_user)
'''Now, we have three threads, main thread, thread 1 for complex calculation and thread 2 for 
   asking user'''
start = time.time()

thread1.start()
thread2.start()

# we will tell main thread to wait, until these two threads are finished

thread1.join() # This will tell main thread to wait till thread1 is finished
thread2.join() # This will tell main thread to wait till thread2 is finished

print(f'Two thread total time : {time.time()-start}')
