# Python If Statement

# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the "if" keyword.

a = 2
b = 4
if b > a:
  print("b is greater than a")  # Output: b is greater than a


# The if statement evaluates a condition (an expression that results in True or False). 
# If the condition is true, the code block inside the if statement is executed. 
# If the condition is false, the code block is skipped.

# Checking if a number is positive:

number = 5
if number > 0:
  print("The number is positive.")  # Output: The number is positive.


# Indentation is very important in Python. 
# It is used to define the scope of loops, functions, and classes. 
# In the example above, the indented block of code is executed if the condition is true.


# Multiple Statements in If Block

# You can also have multiple lines of code inside the if block.

number = 10
if number > 0:
  print("The number is positive.") # Output: The number is positive. 
  print("This is another statement inside the if block.")  # Output: This is another statement inside the if block. 


Age = 27
if Age >= 18:
  print("You are an adult.")  # Output: You are an adult.
  print("You can vote.")  # Output: You can vote.



# Using Variables in Conditions

# Boolean variables can be used directly in if statements without comparison operators.

is_raining = True
if is_raining:
  print("It's raining. Don't forget to take an umbrella!")  # Output: It's raining. Don't forget to take an umbrella!



# Python can evaluate many types of values as True or False in an if statement.
# Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.
# This includes positive numbers (5), negative numbers (-3), and any non-empty string (even "False" is treated as True because it's a non-empty string).


age = 0
if age:
  print("Age is not zero.") # Output: (No output, because age is 0, which is treated as False)

