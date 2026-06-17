# Python Shorthand If

# You can write a shorthand 'if' statement in one line.

# One line if statement:

from importlib import simple


if 5 > 2: print("Five is greater than two.")   # Output: Five is greater than two.


# Short Hand If ... Else

# You can also have an else statement on the same line as the if statement.
# This is called a conditional expression (sometimes known as a "ternary operator").

# One line if else statement:

a = 5
b = 20
print("a is greater than b") if a > b else print("b is greater than a")   # Output: b is greater than a


# Assign a Value With If ... Else

# You can also use a one-line if/else to choose a value and assign it to a variable:

# The syntax follows this pattern:
# variable = value_if_true if condition else value_if_false

a = 5
b = 10
bigger = a if a > b else b 
print("bigger:", bigger)   # Output: bigger: 10



# Multiple Conditions on One Line
# You can also have multiple conditions on the same line using the following syntax:

# one line Three statement if else statement:

x = 5
y = 10
z = 15
bigger = x if x > y and x > z else (y if y > z else z)
print("bigger:", bigger)   # Output: bigger: 15



# When to Use Shorthand If
 
# Shorthand if statements and ternary operators should be used when:
# The condition and actions are simple
# It improves code readability
# You want to make a quick assignment based on a condition



# Example: Using Shorthand 

# Finding the maximum of two numbers:

a = 10
b = 20
maximum = a if a > b else b
print("Maximum:", maximum)   # Output: Maximum: 20


# Setting a default value:

username = ""                      # If username is empty, assign "Guest" as the default value
display_name = username if username else "Guest"
print("Display Name:", display_name)   # Output: Display Name: Guest


