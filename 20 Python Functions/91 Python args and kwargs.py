# Python *args and **kwargs


# *args and **kwargs

# *args and **kwargs are special syntax in Python used to pass a variable number of arguments to a function.

# By default, a function must be called with the correct number of arguments.
# However, sometimes you may not know how many arguments that will be passed into your function.
# *args and **kwargs allow functions to accept a unknown number of arguments.


# Arbitrary Arguments, *args

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

# Example
def my_function(*args):
    print(args[0])  # Output: apple
    print(args[1])  # Output: banana
    print(args[2])  # Output: cherry


def my_function(*kids):
    print("The youngest child is " + kids[2])  # Output: The youngest child is Linus
my_function("Emil", "Tobias", "Linus")

# Arbitrary Arguments are often shortened to *args in Python documentation.


# What is *args?

# *args is a special syntax in Python that allows a function to accept any number of positional arguments.
# The term "args" is short for "arguments" and the asterisk (*) indicates that multiple arguments can be passed.
# Inside the function, *args is treated as a tuple, so you can iterate over it or access individual elements by index.

# Example of using *args in a function:

def my_function(*args):
    print("Number of arguments:", len(args))  # Output: Number of arguments: 3
    print("Arguments:", args)  # Output: Arguments: ('apple', 'banana', 'cherry')
    print("First argument:", args[0])  # Output: First argument: apple
    print("Last argument:", args[-1])  # Output: Last argument: cherry

my_function("apple", "banana", "cherry")


# Using *args in regular arguments

# You can combine regular parameters with *args.
# Regular parameters must come before *args:

# Example
def my_function(greeting, *names):                   
  for name in names:
    print(greeting, name)                                   # Output: Hello Emil, Hello Tobias, Hello Linus
my_function("Hello", "Emil", "Tobias", "Linus")

# In this example, "Hello" is assigned to greeting, and the rest are collected in names.


# Practical Example with *args
# *args is useful when you want to create flexible functions:

# Example
# A function that calculates the sum of any number of values:

def sum_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15


def multiply_numbers(*numbers):
   result = 1
   for number in numbers:
       result *= number
   return result

print(multiply_numbers(2, 3, 4))  # Output: 24
print(multiply_numbers(2, 3, 4, 5))  # Output: 120


def square_numbers(*numbers):
    return [number ** 2 for number in numbers]

print(square_numbers(32))  # Output: [1024]
print(square_numbers(44))  # Output: [1936]


# Example of using *args in a function to print Every family member's name with the different first name but same last names:

def family_members(last_name, *first_names):
    print("Family names:")                           
    for name in first_names:
        print(f"{name} {last_name}")

family_members("Rana", "Naresh", "Rohith", "Ram")   # Output: Family names: Naresh Rana, Rohith Rana, Ram Rana



# Write a function that accepts any number of integers using *args and prints whether each number is Odd or Even.

def odd_or_even(*numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is Even")
        else:
            print(f"{number} is Odd")
odd_or_even(1, 2, 3, 4, 5)  # Output: 1 is Odd, 2 is Even, 3 is Odd, 4 is Even, 5 is Odd



# Finding the maximum value:

def find_maximum(*numbers):
    if len(numbers) == 0:
        return None
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
print(find_maximum(10, 20, 30, 5, 15))  # Output: 30



# Arbitrary Keyword Arguments - **kwargs

# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
# This way, the function will receive a dictionary of arguments and can access the items accordingly:

# Using **kwargs to accept any number of keyword arguments:

# Example

def my_function(**kid):
  print("His first name is " + kid["fname"])  # Output: His first name is Tobias
  print("His last name is " + kid["lname"])   # Output: His last name is Refsnes
 
my_function(fname = "Tobias", lname = "Refsnes")


# Arbitrary Keyword Arguments are often shortened to **kwargs in Python documentation.

# what is **kwargs?
# **kwargs is a special syntax in Python that allows a function to accept any number of keyword arguments.
# The term "kwargs" is short for "keyword arguments" and the double asterisk (**) indicates that multiple keyword arguments can be passed.
# Inside the function, **kwargs is treated as a dictionary, so you can access the values

# Example of using **kwargs in a function:

def my_function(**myvar):
  print("Type:", type(myvar))           # Output: Type: <class 'dict'>
  print("Name:", myvar["name"])         # Output: Name: Tobias
  print("Age:", myvar["age"])           # Output: Age: 30
  print("City:", myvar["city"])         # Output: City: Bergen
  print("All data:", myvar)             # Output: All data: {'name': 'Tobias', 'age': 30, 'city': 'Bergen'}
my_function(name = "Tobias", age = 30, city = "Bergen")


def my_function(**kwargs):
    print("Number of keyword arguments:", len(kwargs))  # Output: Number of keyword arguments: 3
    print("Keyword arguments:", kwargs)  # Output: Keyword arguments: {'name': 'Alice', 'age': 30, 'city': 'New York'}
    print("Name:", kwargs.get("name"))  # Output: Name: Alice
    print("Age:", kwargs.get("age"))  # Output: Age: 30
    print("City:", kwargs.get("city"))  # Output: City: New York


# Combining *args and **kwargs

# You can use both *args and **kwargs in the same function definition.

# The order of parameters should be:   

# regular parameters, 
# *args, and then 
# **kwargs.

# Example of combining *args and **kwargs in a function:

def my_function(Title, *args, **kwargs):
    print("Title:", Title)
    print("Additional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function("My Information Title", "Hello", "World", name="Alice", age=30)     # Output: Title: My Information Title, Additional arguments: ('Hello', 'World'), Keyword arguments: {'name': 'Alice', 'age': 30}



# unpacking arguments

# You can also unpack arguments from a list or dictionary when calling a function.
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.

# Unpacking Lists with *
# If you have values stored in a list, you can use * to unpack them into individual arguments:

# Example of unpacking a list with *:

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result) # Output: 6


# Unpacking Dictionaries with **
# If you have values stored in a dictionary, you can use ** to unpack them into individual keyword arguments:

# Example of unpacking a dictionary with **:

def my_function(name, age, city):
  return f"{name} is {age} years old and lives in {city}."

person_info = {"name": "Alice", "age": 30, "city": "New York"}
result = my_function(**person_info)  # Same as: my_function(name="Alice", age=30, city="New York")
print(result)  # Output: Alice is 30 years old and lives in New York


# Remember: Use * and ** in function definitions to collect arguments, and use them in function calls to unpack arguments



# practical Example of using *args and **kwargs together:

# Example of using *args and **kwargs together in a function:

def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
display_info(name="Alice", age=30, message="Hello", greeting="World")  
