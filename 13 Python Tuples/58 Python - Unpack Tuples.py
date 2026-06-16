# Python - Unpack Tuples

# Unpacking a tuple means that you can extract the values back into variables. This is called "unpacking".

# Unpacking a tuple

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple.

fruits = ("apple", "banana", "cherry") # packing a tuple


# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking".
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits # unpacking a tuple
print(green) # Output: apple
print(yellow) # Output: banana
print(red) # Output: cherry


# Using the Asterisk *

# If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, red, *other) = fruits # unpacking a tuple with an asterisk
print(green) # Output: apple
print(yellow) # Output: banana
print(red) # Output: cherry
print(other) # Output: ['strawberry', 'raspberry']


# if the asterisk is added to a variable name, it must be the last variable in the list,
# or Python will raise an error:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red, other) = fruits # unpacking a tuple with an asterisk
print(green) # Output: apple
print(yellow) # Output: banana
print(red) # Output: ['cherry', 'strawberry']
print(other) # Output: raspberry

