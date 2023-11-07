my_file = open('data.txt','r')
file_content = my_file.read()

my_file.close()
print(file_content)
data = input('Enter some more details')
my_file_writing = open('data.txt', 'w')
my_file_writing.write(data) # will overwrite the contents
my_file_writing.close()
