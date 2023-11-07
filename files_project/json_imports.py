import json
file = open('friends_json.txt','r')
file_contents = json.load(file) # reads file and turn the content into dictionary
file.close()
print(file_contents['friends'][0])
