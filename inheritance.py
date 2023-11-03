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