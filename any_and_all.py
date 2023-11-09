# any() and all()

# any () takes an iterable and returns True, if any of its iterables is True
friends = [
{
'name': 'Rolf',
'location': 'San Francisco'
},
{
'name': 'Ana',
'location': 'San Francisco'
},
{
'name': 'Sarah',
'location' : 'Chicago'
},
]
your_location = input("Where are you right now ?")
friends_nearby = [friend for friend in friends if friend['location']==your_location]
if any(friends_nearby): # True if there's atleast one; or False if empty
    print("You are not Alone !")

print(all([1,2,3])) # True
print(all([0,1,2])) # False