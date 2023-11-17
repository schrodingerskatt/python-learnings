# main_script.py
from concurrent.futures import ProcessPoolExecutor
from functions import ask_user, complex_calculation
import time
# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')

# Ensure that the target function is inside an if __name__ == '__main__': block
if __name__ == '__main__':
    start = time.time()
    with ProcessPoolExecutor(max_workers=2) as pool:
        pool.submit(complex_calculation)
        pool.submit(complex_calculation)

    print(f'Two process total time: {time.time()-start}')
