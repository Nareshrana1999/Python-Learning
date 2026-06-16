# List

# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python
# used to store collections of data, the other 3 are Tuple, Set, and Dictionary
# all with different qualities and usage.
# Lists are created using square brackets:


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


fruits = ["apple", "banana", "cherry"]

# Create a List:

cars = ["BMW", "Mercedes", "Ford"]
print(cars)



# List Items

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Python List Items

# A list is used to store multiple items in a single variable.

# Characteristics of Lists

# ✅ Ordered
# Items keep their insertion order.

# ✅ Changeable (Mutable)
# You can add, remove, or modify items after the list is created.

# ✅ Allow Duplicates
# Multiple items can have the same value.

# ✅ Indexed
# Each item has an index starting from 0.


# Example

fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: apple, banana, cherry


# Accessing Items by Index

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana 
print(fruits[2])  # Output: cherry


# Duplicate Values Allowed

fruits = ["apple", "banana", "cherry", "apple"]
print(fruits)  # Output: apple, banana, cherry, apple


# Changing an Item

fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)  # Output: apple, mango, cherry


# List Items - Data Types
# List items can be of any data type:

mylist = ["apple", "banana", "cherry"]
mylist1 = [1, 5, 7, 9, 3]
mylist2 = [True, False, False]
print(mylist)   # Output: apple, banana, cherry
print(mylist1)  # Output: 1, 5, 7,  9, 3
print(mylist2)  # Output: True, False, False


# List Can Store Different Data Types

fruits = ["apple", "banana", "cherry", 42, True]
print(fruits)  # Output: apple, banana, cherry, 42, True


# Negative Indexing

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])  # Output: cherry
print(fruits[-2])  # Output: banana
print(fruits[-3])  # Output: apple


# List Length

fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # Output: 3


# type()
# From Python's perspective, lists are defined as objects with the data type 'list':
# <class 'list'>


# What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))  # Output: <class 'list'>


mylist1 = [1, 5, 7, 9, 3]
print(type(mylist1))  # Output: <class 'list'>



# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

#Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)  # Output: apple, banana, cherry







