
friends = input('Enter three friend names, separated by commas (no space, please): ').split(',')
# ['Susan', 'Peppa', 'Kate']
people = open("people.txt","r")
people_nearby = people.readlines()
people.close()
friends_set = set(friends)
print(friends_set)
people_nearby = set(people_nearby)
print(people_nearby)
nearby_friends = friends_set.intersection(people_nearby)
print(nearby_friends)