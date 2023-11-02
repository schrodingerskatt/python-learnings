class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name # new variable property inside self called name
        self.grades = new_grades
    def average(self): # this function is called method
        return sum(self.grades)/len(self.grades)

Student_one = Student('Mansi Khanna', [70, 89, 90, 65])
Student_two = Student('Sam Kris', [90, 67, 95, 88])
avg_one = Student_one.average()
# same as above
print(Student.average(Student_one))

class Garage:
    def __init__(self):
        self.cars = []
    def __len__(self):
        return len(self.cars)
    def __getitem__(self, i):
        return self.cars[i]

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford.cars) # ['Fiesta', 'Focus']
print(len(ford.cars))
for car in ford:
    print(car)
'''
"Dunder" is short for "double underscore," and these methods are special methods in Python that are 
surrounded by double underscores on both sides of their names. They are also known as magic methods or 
special methods and are used to define how objects of a class behave in various situations.

Some common examples of dunder methods include:

1. __init__: This method is used to initialize an object when it's created.
2. __str__: This method is used to define a human-readable string representation of an object.
3. __repr__: This method is used to define an unambiguous string representation of an object, typically used for debugging.
4. __add__, __sub__, and other arithmetic operator methods: These methods define how objects of a class behave when used with arithmetic operators.
5. __len__: This method defines the behavior of the len() function when applied to an object of the class.
6. __getitem__ and __setitem__: These methods are used to define behavior for indexing and slicing objects of a class.
'''
# inheritance in python
class Students: # parent class
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks)/len(self.marks)
    
class WorkingStudent(Students): # child class
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
    @property # decorators
    def weekly_salary(self):
        return self.salary*37.9


rolf = WorkingStudent("ROlf", 'MIT', 15.50)
print(rolf.salary)
rolf.marks.append(99)
rolf.marks.append(89)
print(rolf.average())
#print(round(rolf.weekly_salary(),3))

# @property decorator
print(rolf.weekly_salary)

# @classmethod

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)
my_obj = Foo()
my_obj.hi()
