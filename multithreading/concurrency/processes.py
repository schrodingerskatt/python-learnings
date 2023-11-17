# from multiprocessing import Process
import time
from concurrent.futures import ProcessPoolExecutor

####### SINGLE PROCESS

def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print('ask_user: ', time.time() - start)

def complex_calculation():
    print('Started calculating...')
    start = time.time()
    [x**2 for x in range(20000000)]
    print('complex_calculation: ', time.time() - start)

# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')

####### TWO PROCESSES

# Ensure that the target function is inside an if __name__ == '__main__': block

'''
you should modify your code by placing the target function (in this case, complex_calculation) inside an 
if __name__ == '__main__': block. This is necessary because on Windows, each process imports the main 
module when it starts, and if the target function is not protected by this check, it will be executed 
recursively, causing issues.
'''

if __name__ == '__main__':
    # With two processes, we can do them both at once...
    '''process = Process(target=complex_calculation)
    process.start()

    start = time.time()

    ask_user()

    process.join()  # this waits for the process to finish

    print('Two process total time: ', time.time() - start)'''
    
    start = time.time()
    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(complex_calculation)

    print(f'Two process total time: {time.time()-start}')
