# Python - Copy Lists

# Copy a List

# You cannot copy a list simply by typing list2 = list1, 
# because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.


# Use the copy() method

# There are ways to make a copy, one way is to use the built-in List method copy().

fruits = ["apple", "banana", "cherry"]
mylist = fruits.copy()
print(mylist) # Output: apple, banana, cherry


# Use the list() method
# Another way to make a copy is to use the built-in list() method.

fruits = ["apple", "banana", "cherry"]
mylist = list(fruits)
print(mylist) # Output: apple, banana, cherry


# Use the slice Operator
# You can also use the slice operator to make a copy of a list.

fruits = ["apple", "banana", "cherry"]
mylist = fruits[:]
print(mylist) # Output: apple, banana, cherry




