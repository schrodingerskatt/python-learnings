# if-else

friends = ["Rolf", "Massimo", "Laura", "Nacho", "Clara", "Jose"]
family = ["kris", "Mario", "Jose", "Kimberly", "Kate"]
user_name = input("Enter your name ")
if user_name in friends:
    print("Welcome ! my friend")
elif user_name in family:
    print("Hello ! Family")
else:
    print("Hello ! stranger")

# while loop
is_learning = True
while is_learning:
    print ("You are learning")
    is_learning = False

# for loop
for friend in friends:
    print(friend) # value
for i, friend in enumerate(friends):
    print(i) # index
    print(friend) # value
for i in range(len(friends)):
    print(friends[i]) # index wise access
for _ in friends:
    print("Happy Birthday") # when we simply want to run loop

# Destructuring
currencies = 0.8, 1.2
usd, eur = currencies
print(usd) # 0.8
print(eur) # 1.2

# iterating over a list of tuples
fruit_cost = [("banana", 34.45),("Apple", 12.30),("melon", 29.00)]
for fruit, cost in fruit_cost:
    print(f"{fruit} and {cost}")

# iterating over a dictionary
people_age = {"Kylie":27, "Kimberly":43, "Kourtney":44, "Kendall":28, "Khloe":40}
for name in people_age:
    print(name) # only names will be printed
for age in people_age.values():
    print(age) # ages will be printed
for name, age in people_age.items():
    print(f"Hi,my name is {name} and my age is {age}")

# break and continue
cars = ["ok", "ok", "ok","ok","ok"]
for status in cars:
    if status == "ok":
        print("Happy Driving !")
        continue
    else:
        break    
else:
    print("All cars had happy driving") # this statement will run if 'break' statement is not encountered

# list slicing
kwk = ["Kourtney", "Kimberly", "Khloe", "Robert", "Kendall", "Kylie", "Kris", "Malika", "Rita", "BlackChyna", "Hailey"]
print(kwk[1:4]) # from pos 1 to 3. stops at 4
print(kwk[:4]) # 4 elements from the start
print(kwk[:]) # prints entire list
print(kwk[:-3]) # except last 3 all will be printed
print(kwk[-3:]) # last 3

# list comprehension
doubled_numbers = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
doubled_numbers = [number*2 for number in range(5)]
print(doubled_numbers)
values = [f"Numbers are {number}"for number in numbers]
print(values)
kwk_lower = [name.lower() for name in kwk]
print(kwk_lower)

# list comprehension with conditions
ages = [22, 23, 25, 45, 67, 34, 33]
odds = [age for age in ages if age%2 == 1]
print(odds)

disney = ["spiderman", "mickey", "rapunzel"]
marvel = ["IronMan", "Spiderman", "Thor"]
present = [name for name in marvel if name.lower() in disney]
print(present)
present_friends = [
    name.title()
    for name in marvel
    if name.lower() in [f.lower() for f in marvel]
]
print(present_friends)

friends_lower = {n.lower() for n in friends}
family_lower = {n.lower() for n in family}
family_friend = friends_lower.intersection(family_lower)
family_friend = {name.title() for name in family_friend}
print(family_friend)
time_since_then = [1, 7, 8, 12, 4, 65]
long_timers = {
    friends[i]:time_since_then[i]
    for i in range(len(friends))
    if time_since_then[i] > 7
}
print(long_timers)

# zip function
print(dict(zip(friends, time_since_then))) # zips both the list in dictionary format
long_timers_list = list(zip(friends,time_since_then, [1, 2, 3, 4, 5, 6]))
print(long_timers_list)

# enumerate 
print(list(enumerate(friends)))
# [(0, 'Rolf'), (1, 'Massimo'), (2, 'Laura'), (3, 'Nacho'), (4, 'Clara'), (5, 'Jose')]
# similar result as zip

# functions in python

