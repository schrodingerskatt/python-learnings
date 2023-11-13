friends_last_seen ={
    'Rolf': 31,
    'Jose':1,
    'Maria':7
}
print(id(friends_last_seen))

friends_last_seen = {
    'Rolf': 31,
    'Jose': 1,
    'Maria': 7
}
print(id(friends_last_seen))

'''They will print different ids, even though they contain same data, but the objects are different, here
dictionaries are created one after another, they cant have same ids because when the second dictionary
is created, first one is already existing.'''

friends_last_seen['Rolf'] = 0 # mutation
'''In bg, something like friends_last_seen.__setitem__(self,'Rolf') is happening. this call is modifying
self object. It is not creating new dictionary. therefore, it mutates the data instead of creating new one.'''
print(id(friends_last_seen))

my_int = 3
print(id(my_int))
my_int = my_int + 1
'''
In bg, something like my_int.__add__(self, 1): return cls(self.value+1) is hapening, it returns a new integer
object.
'''
print(id(my_int)) 
'''complete different ids will be printed, integer is immutable in python. In case, of my_int = my_int + 1
new object is created. [float, integer, tuple, string] are immutable'''

# -------------- Argument mutability --------------------------------------------------------------------

friends_age ={
    'Ananya' : 25,
    'Nikita' : 24,
    'Astha' : 31
}
def change_age(friends, name):
    print(id(friends))
    friends[name] = 34

print(id(friends_age)) # 1 2789077559936
print(id(friends_age['Nikita'])) # 2 140724664257688
change_age(friends_age, 'Nikita') # 2789077559936
print(id(friends_age['Nikita'])) # 3 140724664258008 value of friends_age['Nikita'] has been changed
print(id(friends_age)) # 4 2789077559936

# ----- Default value for parameters -----

accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}

def add_balance(amount:float, name:str = 'checking') -> float: # default argument here for name is 'checking'
    """Function to update the balance of an account and return the new balance"""
    accounts[name] += amount
    return accounts[name]
add_balance(500.00)
print(accounts['checking'])

# we can't have default argument as first parameter of a function. for eg : add_balance(name:str = 'checking', amount:float) is invalid.

# --------- Mutable default argument ---------

def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)

    return{
        'name':name,
        'main_account_holder':holder,
        'account_holders': account_holders
    }
a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Julia')
print(a2) # {'name': 'savings', 'main_account_holder': 'Julia', 'account_holders': ['Rolf', 'Julia']}
'''list is defined, when the function is defined. so we are going to see result like above.
To solve this problem use :

def create_account(name: str, holder: str, account_holders = None):
    if not account_holders:
        account_holders.append(holder)

    return{
        'name':name,
        'main_account_holder':holder,
        'account_holders': account_holders
    }
a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Julia')
'''

# -------------------------- Argument unpacking in python -----------------------------------------------
data ={
    'opened': 1001.00,
    'closed': 0.00
}
def add_values(amount: float, name: str) -> float:
    data[name] += amount
    return data[name]

dtrans = [
    (-180.23, 'opened'),
    (2300.54, 'closed'),
    (190.12, 'opened')
]

for t in dtrans:
    add_values(*t) # same as add_values(amount = t[0], name = t[1])

print(data['closed'])


    