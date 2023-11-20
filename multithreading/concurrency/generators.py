def countdown(n):
    while n > 0:
        yield n
        n-= 1

c1 = countdown(12)
c2 = countdown(20)

#print(next(c1))
#print(next(c2))
#print(next(c1))
#print(next(c2))
'''This gives illusion of threading, if its very fast, using generators is one of the way to achieve of
multitasking in python'''

tasks = [countdown(10), countdown(5), countdown(20)]
while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task Finished')
