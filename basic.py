name = "Ananya Arya"
profession = "Software Development Engineer"
department = "ML/AI/Data"
age = 25
PI = 3.14159 # all caps is a naming convention for constants
print(f"{name} is {profession} in {department} Department")
print("value of PI is "+ str(PI))
# or use print(f"value of PI is {PI}")

# integer floor divison use //
print(8//3)
# for float divison use /
print(8/3)

# strings in python
string_with_quotes = "Hi, what's up!"
another_string = 'He said, "You are amazing! "yesterday.'
# or you can use
another_string_2 = "He said, \"You are amazing! \"yesterday."
multiline_String = '''Hello 
                   How are you'''
# we can use multiline strings even without assinging to any variable
name = "Jose"
greeting = f"How are you, {name}?"
print(greeting)
name = "Bob"
print(greeting) # Jose will be printed, it won't be printing Bob
final_greeting = "How are you, {} ?"
jose_greeting = final_greeting.format(name) # this will print Bob
#jose_greeting = final_greeting.format(name=name)

# Boolean values in python are True and False
# List in python

friends = ["Ananya", "Nikita", "Khushbu", "Mansi", "Swathi", "Riya"]
print(friends)
print(friends[0])
print(friends[::-1]) # reverse
print(friends[:-1]) # will omit last value from the list
print(len(friends))
friends_ov = [["Mansi", 25],["Nikita",25],["Khushbu",25]]
print(friends_ov[0])
print(friends_ov[0][0])
print(friends_ov[0][1])
print(friends_ov)
friends.append("Priyanka")
print(friends)
friends.remove("Swathi")
print(friends)

# tuples
short_tuple = "Rolf", "Bolb" # this will be treated as tuple
tuple_form = ("Monica", "Chandler") # this is also a tuple
tuple_in_list = [("Rachel", "joey")]
tuple_form = tuple_form + ("Sasha", "Jenny","Mikhail",) # tuple didn't get modified, we created new tuple, tuples are immutable
print(tuple_form)

#sets
art_friends = {"Ana", "Biyanka", "Ariana", "Minney","Christian", "Robert"}
art_friends.add("Britney")
science_friends = {"Christopher", "Christian", "Anastasia","Ana"}
arts_not_science = art_friends.difference(science_friends)
print(arts_not_science)

# symmetric difference : members which are not in both sets, basically not intersection
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)
in_both = art_friends.intersection(science_friends)
print(in_both)
all_friends = art_friends.union(science_friends)
print(all_friends)

# Dictionary.Key-value pairs. all keys must be unique
people_age = {"Kylie":27, "Kimberly":43, "Kourtney":44, "Kendall":28, "Khloe":40}
print(people_age["Kendall"])
people_age["Kendall"] = 29
people_age["Rob"] = 39
print(people_age)
kwk = (
    {"season": 2001, "Episodes" : 340},
    {"season" : 2005, "Episodes": 2345}
)
print(kwk[0]["season"])
print(kwk[0]["Episodes"])
# dict is used to turn data into a dictionary
sisters = [("Ane",12),("Sia",15),("Monica",18)]
sisters = dict(sisters)
print(sisters)

# another good example
my_friends = {
    'Jose': {'last_seen': 6},
    'Rolf': {'surname': 'Smith'},
    'Anne': 6
}

print(my_friends['Jose'])

grades = [80, 75, 90, 100]
print(len(grades))
print(sum(grades))

# joining a list
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")