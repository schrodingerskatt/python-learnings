# define superclass
class super_class:
    pass
# inheritance
class sub_class(super_class):
    pass

class Animal:
    name = ""
    def eat(self):
        print("I can eat")
class Dog(Animal):

    def eat(self): # method overriding , preference will be given to subclass. this eat() function will be executed
        print("I like to eat bones")

    def display(self):
        print("My name is", self.name)

# create an object of the subclass
shibainu = Dog()
# access superclass attribute and method 
shibainu.name = "geralt"
shibainu.eat()
# call subclass method 
shibainu.display()

# but suppose we need to access superclass method from subclass, we want eat() function of parent class as well
# to achieve this we use super() method

class Zoo:
    animals = " "
    def hungry(self):
        print("This animal is hungry")
    
class Lion(Zoo):
    def hungry(self):
        super().hungry()  # call the hungry() method of the superclass using super()
        print("I want meat")
shera = Lion()
shera.hungry()

# multiple inheritance in python

class SuperClass1:
    pass
    # features of SuperClass1

class SuperClass2:
    pass
    # features of SuperClass2

class MultiDerived(SuperClass1, SuperClass2):
    pass
    # features of SuperClass1 + SuperClass2 + MultiDerived class

class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass

# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()

# multilevel inheritance

class SuperClass:
    pass
    # Super class code here

class DerivedClass1(SuperClass):
    pass
    # Derived class 1 code here

class DerivedClass2(DerivedClass1):
    pass
    # Derived class 2 code here

class SuperClass:
    def super_method(self):
        print("Super Class Method")

class DerivedClassI(SuperClass):
    def derived_method(self):
        print("Derived class I method")

class DerivedClassII(DerivedClassI):
    def derived_method_II(self):
        print("Derived class II method")

d = DerivedClassII()
d.super_method()
d.derived_method()
d.derived_method_II()

# Method Resolution Order

'''
If two superclasses have the same method name and the derived class calls that method.
Python uses the MRO to search for the right method to call.
'''
'''
1. Here, SuperClassI and SuperClassII both of these classes define a method info().

2. So when info() is called using the d1 object of the Derived class, Python uses the MRO to determine which method to call.

3. The MRO specifies that methods should be inherited from the leftmost superclass first, so info() of SuperClassI is called rather than that of SuperClassII.


'''
class SuperClassI:
    def info(self):
        print("Super Class I method")

class SuperClassII:
    def info(self):
        print("Super Class II method")

class Derived(SuperClassI, SuperClassII):
    pass

d1 = Derived()
d1.info()

# Diamond Problem
class A:
    def met(self):
        print("This is method from class A")
class B(A):
    def met(self):
        print("This is method from class B")
class C(A):
    def met(self):
        print("This is method from class C")
class D(C, B): # since, C comes here before B. def met() for C will be printed.
    # in case we have defined def met(self) inside D. it would have printed that function
    pass

a = A()
b = B()
c = C()
d = D()
d.met()