# List Comprehension

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example
# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)


# With list comprehension you can do all that with just one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # Output: apple, banana, mango