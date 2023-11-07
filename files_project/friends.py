# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

# readlines() : Return all lines in the file, as a list where each line is an item in the list object

friends = input('Enter three friend names, separated by commas (no space, please): ').split(',')
# Susan,Peppa,Kate
people = open("people.txt", "r")
people_nearby = [name.strip() for name in people.readlines()]  # Remove leading/trailing whitespace
people.close()
friends_set = set(friends)
print(friends_set)
people_nearby = set(people_nearby)
print(people_nearby)
nearby_friends = friends_set.intersection(people_nearby)
print(nearby_friends)
nearby_friends_file = open('nearby_friends.txt', 'w')
for friend in nearby_friends:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')
nearby_friends_file.close()