from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
    # if we have defined abstract method then every subclass is supposed to use this method.
    # lets say, i remove def printarea() from Rectangle class, then this code will throw error, because it didn't defined printarea()
class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
    
    def printarea(self):
        return self.length*self.breadth
    
rect = Rectangle()
# you cant create object of abstract base class