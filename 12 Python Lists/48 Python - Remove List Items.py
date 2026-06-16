# Python - Remove List Items

# Remove Specified Item
# The remove() method removes the specified item.

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: apple, cherry


# If there are more than one item with the specified value, the remove() method removes the first occurrence:

fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)  # Output: apple, cherry, banana


# Remove Specified Index
# The pop() method removes the specified index, (or the last item if index is not specified):

fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)  # Output: apple, cherry


# If you do not specify the index, the pop() method removes the last item.

fruits = ["apple", "banana", "cherry"]
fruits.pop()
print(fruits)  # Output: apple, banana


# The del keyword also removes the specified index:

fruits = ["apple", "banana", "cherry"]
del fruits[0]
print(fruits)  # Output: banana, cherry


# The del keyword can also delete the list completely:
fruits = ["apple", "banana", "cherry"]
del fruits
print(fruits)  # Output: Error - fruits is not defined


# Clear the List
# The clear() method empties the list.

fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Output: []






