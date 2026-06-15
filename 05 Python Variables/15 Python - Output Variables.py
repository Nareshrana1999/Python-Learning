# Output Variables
# The print() function is often used to output variables.

x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma:

x = "My"
y = "Name is"
z = "Naresh Rana"
print(x,y,z)

# You can also use the + operator to output multiple variables:

x = "Hello "
y = "How are you? "
z = "I am fine"
print(x + y + z)
# Notice the space character after "Hello " and "How are you? " and "I am fine"
# without them the result would be "HelloHow are you?I am Fine".


# For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)
print(x / y)
print(x * y)
print(x - y)

# In the print() function
# when you try to combine a string and a number with the + operator
# Python will give you an error:

# x = 5
# y = "John"
# print(x + y)
# Error

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x = 27
y = "Naresh Rana"
print(x, y)