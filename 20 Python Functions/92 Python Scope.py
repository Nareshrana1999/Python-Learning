# Python Scope

# A variable is only available from inside the region it is created. This is called scope.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# Example
from unittest import result


def my_function():
    x = 300
    print(x)   # Output: 300
my_function()


# Function Inside Function

# As explained in the example above, the variable x is not available outside the function, 
# but it is available for any function inside the function:

# Example
def my_function():
    x = 300
    def my_inner_function():
        print(x)   # Output: 300
    my_inner_function()
my_function()   



def my_result():
   num = 20
   num2 = 20
   def additionandsubtraction():
       result = num + num2
       print(result)  # Output: 40
       result2 = num - num2
       print(result2)  # Output: 0
   additionandsubtraction()
my_result()



def odd_even():
    num = 10
    def check_odd_even():
        if num % 2 == 0:
            print("Even")  # Output: Even
        else:
            print("Odd")
    check_odd_even()
odd_even()



# Global Scope

# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

# Example

x = 300      # Global variable

def my_function():
    print(x)   # Output: 300
my_function()




last_name = "Rana"  # Global variable

def name():
    first_name = "Naresh"  # Local variable
    print(f"{first_name} {last_name}")  # Output: Naresh Rana
name()



last_name = "Rana"  # Global variable

def name(*first_names):
    for first_name in first_names:
        print(f"{first_name} {last_name}")  # Output: Naresh Rana, Rohith Rana, Ram Rana
name("Naresh", "Rohith", "Ram")


# Naming Variables

# If you operate with the same variable name inside and outside of a function,
# Python will treat them as two separate variables, 
# one available in the global scope (outside the function) and one available in the local scope (inside the function):


x = 300  # Global variable

def my_function():
    x = 200  # Local variable
    print(x)  # Output: 200

my_function()

print(x)  # Output: 300



# Global Keyword

# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# Example

def my_function():
    global x
    x = 300 # Now x is a global variable
    print(x)
    
my_function()
print(x)  # Output: 300


def name():
    global last_name
    last_name = "Rana"  # Now last_name is a global variable
    print(last_name)  # Output: Rana
name()
print(last_name)  # Output: Rana


# Also, use the global keyword if you want to make a change to a global variable inside a function.

# Example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 300     # Global variable

def my_function():
    global x   # Now we can change the value of x inside the function
    x = 200    # Now x is 200
    print(x)   # Output: 200

my_function()
print(x)  # Output: 200



# Nonlocal Keyword

# The nonlocal keyword is used to work with variables inside nested functions,
# where the variable should not belong to the inner function.

# Example

def outer_function():
    x = "local"
    def inner_function():
        nonlocal x
        x = "nonlocal"
        print("Inner:", x)  # Output: Inner: nonlocal
    inner_function()
    print("Outer:", x)  # Output: Outer: nonlocal
outer_function()


def myfunc1():
  x = "Jane"        # Local variable
  def myfunc2():
    nonlocal x      # Nonlocal variable
    x = "hello"     # Change the value of x in the enclosing scope
  myfunc2()
  return x      
print(myfunc1())    # Output: hello



# The LEGB Rule

# Python resolves names using the LEGB rule, 
# which is an acronym that stands for Local, Enclosing, Global, and Built-in.

# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace


# Example

x = "global"  # Global variable

def outer_function():
    x = "enclosing"  # Enclosing variable
    def inner_function():
        x = "local"  # Local variable
        print("Inner:", x)  # Output: Inner: local
    inner_function()
    print("Outer:", x)  # Output: Outer: enclosing
outer_function()
print("Global:", x)  # Output: Global: global



num = 10  # Global variable

def outer():
    num = 20  # Enclosing variable
    def inner():
        num = 30  # Local variable
        print("Inner:", num)  # Output: Inner: 30
    inner()
    print("Outer:", num)  # Output: Outer: 20
outer()
print("Global:", num)  # Output: Global: 10