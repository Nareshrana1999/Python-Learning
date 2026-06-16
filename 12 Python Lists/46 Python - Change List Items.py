# Change Item Value

# To change the value of a specific item, refer to the index number:

from xxlimited import new


fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)  # Output: apple, mango, cherry


# Change a Range of Item Values
# To change the value of items within a specific range, 
# define a list with the new values, and refer to the range of index numbers where you want to insert the new values:


fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits[1:3] = ["mango", "watermelon"]
print(fruits)  # Output: apple, mango, watermelon, orange, kiwi, melon, mango   


# If you insert more items than you replace, 
# the new items will be inserted where you specified, and the remaining items will move accordingly:

fruits = ["apple", "banana", "cherry"]
fruits[1:2] = ["watermelon", "mango"]
print(fruits)  # Output: apple, watermelon, mango, cherry


# If you insert less items than you replace,
# the new items will be inserted where you specified, and the remaining items will move accordingly:

fruits = ["apple", "banana", "cherry"]
fruits[1:3] = ["watermelon"]
print(fruits)  # Output: apple, watermelon, cherry


# Insert Items

# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:


fruits = ["apple", "banana", "cherry"]
fruits.insert(2, "watermelon")
print(fruits)  # Output: apple, banana, watermelon, cherry



