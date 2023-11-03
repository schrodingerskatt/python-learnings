class Employee:
    no_of_leaves = 8
    _protec = 110 # protected is shown using single underscore
    __company = "Tower Research Capital"

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
    
emp = Employee("Ananya", 4500000, "Software Development Engineer")
print(emp._protec) # protected : base class and dreived class can use it but not outside class
print(emp._Employee__company)

