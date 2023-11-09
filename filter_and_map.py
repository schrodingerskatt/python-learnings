# filter

friends = ['Jose', 'Rolf', 'Ana', 'Randy', 'Mary']
names = filter(lambda x: x.startswith('R'),friends) # filter returns a genertaor
print(next(names))
print(next(names))
# argument 1 : function that return True or False
# argument 2 : iterable
# or you can use generators

def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i
starts_with_r = my_custom_filter(lambda x: x.startswith('R'), friends)
print(next(starts_with_r))
print(next(starts_with_r)) # same result as above

# map : applies a function over entire iterables
friends_lower = map(lambda x: x.lower(), friends)
print(list(friends_lower))