# we can call a function inside a funcction, and can return a function
'''
In python, functions are first class first class objects which means functions can be used or passed as
arguments.
1. A function is an instance of the Object type.
2. You can store the function in a variable.
3. You can pass the function as a parameter to another function.
4. You can return the function from a function.
5. You can store them in data structures such as hash tables, lists, …
'''

# can be treated as objects 
def shout(text): 
	return text.upper() 

print(shout('Hello')) 
yell = shout 
print(yell('Hello')) 

# can be passed as arguments to other functions 
def shout(text): 
	return text.upper() 

def whisper(text): 
	return text.lower() 

def greet(func): 
	# storing the function in a variable 
	greeting = func("""Hi, I am created by a function passed as an argument.""") 
	print (greeting) 

greet(shout) 
greet(whisper) 

# Functions can return another function 

def create_adder(x): 
	def adder(y): 
		return x+y 

	return adder 

add_15 = create_adder(15) 

print(add_15(10)) 

'''
Decorators are used to modify the behaviour of function or class. 
In Decorators, functions are taken as the argument into another function and 
then called inside the wrapper function.
'''

def executor(func):
    func("Hello World")
executor(print)

def dec(func):
    def nowexec():
        print("connection to server started")
        func()
        print("connection to server established")
    return nowexec
@dec
def aws_access():
    print("got aws access")
# aws_connected = dec(aws_access)  same as writing @dec on above def aws_access()
aws_access()