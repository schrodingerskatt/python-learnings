class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self): # self refers to current object, about which we are talking, basically the instance on which the function is applied
        return f"Name is {self.name}, salary is {self.salary} and role is {self.role}"
    
    @classmethod # class method can only access instance variables of class, we can access them from any instance of this class or direcctly through class
    # we can also use class method as alternative of constructors
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])
    
    @staticmethod #this will work outside class as well, but in case if u want to run it only for objects of Employee class it is better to keep it inside
    def printgood(string):
        print("This is good" + string)
    
harry = Employee("Harry", 445, "Instructor")
karan = Employee.from_str("Karan-459-Teacher") # alternative constructor
print(karan.salary)
print(harry.salary)
karan.printgood("hey") #nothing will be printed since there is no return type, to return something u can add return in static method
harry.change_leaves(34)
print(harry.no_of_leaves)
#rohan = Employee()
#harry.name = "Harry"
#harry.salary = "455"
#harry.role = "Instructor"
#rohan.name = "Rohan"
#rohan.salary = 0
#rohan.role = "learner"
#print(rohan.printdetails())

# static method : method that doesn't access instance nor class variable. it will just stay in class