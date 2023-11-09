# A Generator in Python is a function that returns an iterator using the Yield keyword.

def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1

g = hundred_numbers()
print(next(g))
# range behaves like a generator but is not a generator

# generator class and iterators

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __iter__(self): # now this class is iteable, we can use the below commented for loop, if this method is prsent 
        return self # returns current object, this method makes our class both genertaor and iterable

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

# Create an instance of the generator
my_gen = FirstHundredGenerator()

print(my_gen.number)
my_gen.__next__()
print(my_gen.number)

# generator is an iterator not iterable unlike list, cant do sum(my_gen) or below for loop
#for i in my_gen:
    #print(i)
# iterable is an object that has an iter method, to make an object iterable either define __iter__ or
# use __len__() and __getitem__()
# iterators helps us to go to the next value whereas iterable used to go over all the values of iterators