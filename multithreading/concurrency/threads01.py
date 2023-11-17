import time
from concurrent.futures import ThreadPoolExecutor 
# It allows us to use bunch of thread pools to execute jobs

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

start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')

start = time.time()
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)

print(f'Two thread total time: {time.time()-start}')



