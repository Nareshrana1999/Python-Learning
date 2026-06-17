# Python For Loops

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Example
# Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)   # Output: apple, banana, cherry


# Note: remember to indent the block of code within the for loop.
# The for loop does not require an indexing variable to set beforehand.


# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters.

# Example
# Loop through the letters in the word "banana":

for x in "banana":
    print(x)   # Output: b, a, n, a, n, a


# Breaking the Loop
# With the break statement we can stop the loop before it has looped through all the items.

# Example
# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)   # Output: apple, banana
  if x == "banana":
    break
  
# Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)   # Output: apple


# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

# Example
# Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)   # Output: apple, cherry    


# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# Example
# Using the range() function:

for x in range(6):
  print(x)   # Output: 0, 1, 2, 3, 4, 5

# Note: The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

# range() function with a parameter
for x in range(2, 6):
    print(x)   # Output: 2, 3, 4, 5


# range() function with 3 parameters
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

for x in range(2, 30, 3):
    print(x)   # Output: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29



# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# Example
# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
    print(x)   # Output: 0, 1, 2, 3, 4, 5
else:
    print("Finally finished!")   # Output: Finally finished!

# Note: The else block will NOT be executed if the loop is stopped by a break statement.


# Breaking the Loop
# The break statement can be used to stop a for loop even if the for loop has not looped through all the items:

for x in range(6):
    print(x)   # Output: 0, 1, 2, 3, 4, 5
    if x == 3:
        break
else:
    print("Finally finished!")   # This will not be executed due to the break statement



# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

# Example
# Print each adjective for every fruit:

adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adjectives:
    for y in fruits:
        print(x, y)   # Output: red apple, red banana, red cherry, big apple, big banana, big cherry, tasty apple, tasty banana, tasty cherry




# pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

# Example

for x in [0, 1, 2]:
    pass


for x in range(3):
  print(x)