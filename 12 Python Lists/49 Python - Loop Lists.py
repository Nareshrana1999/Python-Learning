# Python - Loop Lists


# Loop Through a List
# You can loop through the list items by using a for loop:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) # Output: apple, banana, cherry



# Loop Through the Index Numbers

# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.


fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
  print(fruits[i]) # Output: apple, banana, cherry



# Looping Using a While Loop

# You can loop through the list items by using a while loop.

fruits = ["apple", "banana", "cherry"]
i = 0   
while i < len(fruits):
  print(fruits[i]) # Output: apple, banana, cherry
  i = i + 1


cars = ["Ford", "BMW", "Volvo"]
i = 2
while i < len(cars):
  print(cars[i]) # Output: Volvo
  i = i + 1


# Looping Using List Comprehension
# List comprehension offers the shortest syntax for looping through lists:

fruits = ["apple", "banana", "cherry"]
[print(x) for x in fruits] # Output: apple, banana, cherry


country = ["USA", "Canada", "Mexico"]
[print(x) for x in country] # Output: USA, Canada, Mexico





