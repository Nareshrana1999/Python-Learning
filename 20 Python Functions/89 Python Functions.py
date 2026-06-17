# Python Functions

# A function is a block of code which only runs when it is called. 
# You can pass data, known as parameters, into a function. 
# A function can return data as a result. 
# A function helps avoiding code repetition.


# Creating a Function
# In Python a function is defined using the "def" keyword,followed by a function name and parentheses:

def my_function():
  print("Hello from a function")   

# This creates a function named my_function that prints "Hello from a function" when called.
# The code inside the function must be indented. Python uses indentation to define code blocks.


# Calling a Function
# To call a function, use the function name followed by parentheses:


def my_function():
  print("Hello from a function")
my_function()   # Output: Hello from a function

def car():
    print("This is a car.")
car()   # Output: This is a car.



# You can call the same function multiple times:

def Fruit():
    print("This is a fruit.")
Fruit()   # Output: This is a fruit.
Fruit()   # Output: This is a fruit.  
Fruit()   # Output: This is a fruit.


# Function Name

# Function names follow the same rules as variable names in Python:

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)


# Valid function names:

# my_function()
# myFunction()
# my_function2()
# _my_function()
# My_Function()
# MyFunction()

# Invalid function names:

# 2my_function()
# my-function()
# my function()
# my.function()



# Why use Functions?
# Functions allow us to reuse code.
# This can save time, reduce errors, and make code easier to read and maintain.

# Example
# Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. 
# Without functions, you would have to write the same calculation code repeatedly:

# Without functions - repetitive code:

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


# With functions - reusable code:

def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius
print(fahrenheit_to_celsius(77))   # Output: 25.0
print(fahrenheit_to_celsius(95))   # Output: 35.0 
print(fahrenheit_to_celsius(50))   # Output: 10.0



# USD to INR converter:

def usd_to_inr(usd):
    inr = usd * 95
    return inr
print(usd_to_inr(10))   # Output: 950
print(usd_to_inr(50))   # Output: 4750
print(usd_to_inr(100))  # Output: 9500


# Km to Miles converter:

def KM_to_MILES(KM):
   MILES = KM * 0.621371
   return MILES
print(KM_to_MILES(1))   # Output: 0.621371
print(KM_to_MILES(5))   # Output: 3.106855
print(KM_to_MILES(10))  # Output: 6.21371


# Returning Values

# Functions can send data back to the code that called them using the return statement.
# When a function reaches a return statement, it stops executing and sends the result back:

# A function that returns a value:
def get_greeting():
  return "Hello from a function"
message = get_greeting()
print(message)  # Output: Hello from a function


# Using the return value directly:
def get_greeting():
  return "Hello from a function"
print(get_greeting())  # Output: Hello from a function


# Add Two Numbers
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print(result)   # Output: 8


# Square a Number
def square(x):
    return x * x
print(square(4))   # Output: 16



# Pass Statement
# If you have a function that you want to define but not implement yet, you can use the pass statement as a placeholder:

def my_function():
    pass















