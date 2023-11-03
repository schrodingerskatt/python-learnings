# encapsulation in python is achieved using Double underscore i.e. (__name and __method()) or single underscore (_name and _method())

class Dress():
    def __init__(self):
        self.brand = "Zara"
        self.__size = "M"
    def Details(self):
        return self.brand+" "+self.__size
    def get__size(self):
        return self.__size
    def set__size(self, t):
        self.__size = t
obj = Dress()
obj.set__size("XS") # using getter and setter
obj.get__size()
print(obj.brand)
print(obj._Dress__size) # name mangaling, through this we can acess private variables as well
print(obj.Details())



