# Python Decorators

# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

# Basic Decorator 

# A simple decorator that adds a message before and after the execution of a function: 
# Define the decorator first, then apply it with @decorator_name above the function

# Example
# A basic decorator that uppercases the return value of the decorated function.


def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "Hello, World!"

print(greet())  # Output: HELLO, WORLD!

# OR

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

# By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.
# The function changecase is the decorator.
# The function myfunction is the function that gets decorated.



# Multiple Decorators

# A decorator can be called multiple times. Just place the decorator above the function you want to decorate.

# Example

def exclamation_decorator(func):
    def wrapper():
        result = func()
        return result + "!!!"
    return wrapper

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper
@exclamation_decorator
@uppercase_decorator    
def greet():
    return "Hello, World!"
print(greet())  # Output: HELLO, WORLD!!!


# Using the @changecase decorator on two functions:

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())     # Output: HELLO SALLY
print(otherfunction())  # Output: I AM SPEED!



#  Upper and Lower Case Decorator

def both_cases(func):
    def inner():
        text = func()
        return text.upper(), text.lower()
    return inner

@both_cases
def message():
    return "Hello Sally"

upper, lower = message()

print("Upper:", upper)
print("Lower:", lower)



# Arguments in Decorators Functions

# Decorators can also accept arguments.
# Functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function:

# Example

def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")    # Output: Before the function call
        result = func(*args, **kwargs)       # greet("Sally") is called here, and the argument "Sally" is passed to the greet function
        print("After the function call")     # Output: After the function call
        return result                        # Output: Hello, Sally!
    return wrapper

@decorator_with_args
def greet(name):
    print(f"Hello, {name}!")   # Output: Hello, Sally!

greet("Sally")


# *args and **kwargs

# Sometimes the decorator function has no control over the arguments passed from decorated function, 
# to solve this problem, add (*args, **kwargs) to the wrapper function, 
# this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function


# Example
# Secure the function with *args and **kwargs arguments:

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John")) # Output: HELLO JOHN



# Decorators with Arguments

# Decorators can also accept arguments.
# To create a decorator that accepts arguments, you need to add an extra layer of functions.
# Decorators can accept their own arguments by adding another wrapper level.

# Example
# A decorator factory that takes an argument and transforms the casing based on the argument value.

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction()) # Output: hello linus


# Multiple Decorators

# A function can be decorated with multiple decorators, and the order of decorators matters.

# You can use multiple decorators on one function.
# This is done by placing the decorator calls on top of each other.
# Decorators are called in the reverse order, starting with the one closest to the function.


# Example
# One decorator for upper case, and one for adding a greeting:


def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction()) # Output: HELLO TOBIAS HAVE A GOOD DAY!




# Preserving Function Metadata

# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.

# When you decorate a function, the original function's metadata (like its name, docstring, etc.) is lost.
# To preserve the original function's metadata, you can use the functools.wraps decorator inside your


# Example
# Normally, a function's name can be returned with the __name__ attribute:

def myfunction():
  return "Have a great day!"

print(myfunction.__name__) # Output: myfunction

# But, when a function is decorated, the metadata of the original function is lost.

# Example
# Try returning the name from a decorated function and you will not get the same result:

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__) # Output: myinner (not myfunction)






