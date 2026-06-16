# Python - Loop Tuples

# Loop Through a Tuple
# You can loop through the items of a tuple by using a for loop.

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) # Output: apple, banana, cherry



# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number. 
# The range() function and len() function can be used to create a suitable iterable.

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i]) # Output: apple, banana, cherry



# Using a While Loop
# You can loop through the tuple items by using a while loop.

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i]) # Output: apple, banana, cherry
  i = i + 1
