class Employee:
    no_of_leaves = 8 # all the objects will share this variable. objects can access them but they cant change it
    pass
harry = Employee()
meghan = Employee()

harry.name = "Harry"
harry.location = "England"
harry.role = "Prince"

meghan.name = "Meghan"
meghan.location = "US"
meghan.role = "actress"

# we can access, no of leaves through both objects and class but can change only through class

print(Employee.no_of_leaves) # 8
print(meghan.no_of_leaves) # 8
meghan.no_of_leaves = 2
print(meghan.no_of_leaves) # 2
print(Employee.no_of_leaves) # 8, it will print 8 only
