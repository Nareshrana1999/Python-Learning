# Python - Update Tuples

# Since tuples are unchangeable, you cannot change, add, or remove items after the tuple has been created.
# But there are some workarounds that can be used to change a tuple.


# change tuple values

# Convert the tuple into a list, change the list, and convert the list back into a tuple:

x = ("apple", "banana", "cherry")
y = list(x) # Convert the tuple into a list 
y[1] = "kiwi" # Change the second item
x = tuple(y) # Convert the list back into a tuple   
print(x) # Output: apple, kiwi, cherry