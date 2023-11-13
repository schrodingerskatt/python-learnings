'''
* counter
* defaultdict
* ordereddict
* nameddtuple
* deque
'''
from collections import Counter

device_tempeartures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]
temperature_counter = Counter(device_tempeartures)
print(temperature_counter[14.0])

print(Counter({'hello':5,'hi':13})['hi'])

coworkers = [('Rolf', 'MIT'),('Julia', 'Caltech'),('Rolf', 'Cambridge'),('Susan', 'Princeton')]

# traditional way
'''
alma_maters = {}
for cw, pl in coworkers:
    if cw not in alma_maters:
        alma_maters[cw] = []
    alma_maters[cw].append(pl) '''

# to solve this problem we can use defaultdict
from collections import defaultdict

alma_maters = defaultdict(list)
for coworker, place in coworkers:
    alma_maters[coworker].append(place)
print(alma_maters)
print(alma_maters['Rolf']) # ['MIT', 'Cambridge']
print(alma_maters['Anastasia']) # [], In case u dont want an empty list for absent values use : alma_maters.default_factory = None

my_company = 'Teclado'
coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'),('Ana', 'Google')]
coworker_companies = defaultdict(lambda:my_company) # sets default value as Teclado

for person, company in other_coworkers:
    coworker_companies[person]=company

print(coworker_companies['Ana'])
print(coworker_companies['Rhys'])

from collections import OrderedDict

# elements will be in order in which they are inserted

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 8
o['Jen'] = 11
print(o) # OrderedDict({'Rolf': 6, 'Jose': 8, 'Jen': 11})
o.move_to_end('Rolf')
print(o) # OrderedDict({'Jose': 8, 'Jen': 11, 'Rolf': 6})
o.move_to_end('Jen', last = False)
print(o) # OrderedDict({'Jen': 11, 'Jose': 8, 'Rolf': 6})
o.popitem() # removes Rolf
print(o) # OrderedDict({'Jen': 11, 'Jose': 8})

from collections import namedtuple
Account = namedtuple('Account', ['name', 'balance'])
account = Account('checking', 1850.00)
print(account)
name, balance = account
print(name)
print(balance)
accountNamedTuple = Account(*account)
print(accountNamedTuple._asdict()['balance'])

from collections import deque
# it is thread safe
friends = deque(('Ananya', 'Jose', 'Marylin', 'Gini', 'Joshua'))
friends.append('Nikita')
friends.appendleft('Kamil')
print(friends) # deque(['Kamil', 'Ananya', 'Jose', 'Marylin', 'Gini', 'Joshua', 'Nikita'])
friends.pop()
print(friends) # deque(['Kamil', 'Ananya', 'Jose', 'Marylin', 'Gini', 'Joshua'])
friends.popleft()
print(friends) # deque(['Ananya', 'Jose', 'Marylin', 'Gini', 'Joshua'])