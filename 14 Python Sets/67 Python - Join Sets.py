# Python - Join Sets

# Join Sets

# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates

# Union
# The union() method returns a new set with all items from both sets.
# Join set1 and set2 into a new set:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) # Output: a, b, c, 1, 2,

# You can use the | operator instead of the union() method, and you will get the same result.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3) # Output: a, b, c, 1, 2, 3


# Join Multiple Sets

# All the joining methods and operators can be used to join multiple sets.
# When using a method, just add more sets in the parentheses, separated by commas:

# Join multiple sets with the union() method:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = {"x", "y", "z"}
set4 = {"m", "n", "o"}
set5 = set1.union(set2, set3, set4)
print(set5) # Output: a, b, c, 1, 2, 3, x, y, z, m, n, o

# Join multiple sets with the | operator:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}    
set3 = {"x", "y", "z"}
set4 = {"m", "n", "o"}  
set5 = set1 | set2 | set3 | set4
print(set5) # Output: a, b, c, 1, 2, 3, x, y, z, m, n, o

cars = {"Ford", "BMW", "Volvo"}
morecars = {"Toyota", "Honda", "Mazda"}
evenmorecars = {"Audi", "Mercedes", "Volkswagen"}
allcars = cars.union(morecars, evenmorecars)
print(allcars) # Output: Ford, BMW, Volvo, Toyota, Honda, Mazda, Audi, Mercedes, Volkswagen


# Joiin a set and a list and a tuple
# You can join a set with any iterable object, such as lists and tuples:

set1 = {"a", "b" , "c"}
list1 = [1, 2, 3]
tuple1 = ("x", "y", "z")
set2 = set1.union(list1, tuple1)
print(set2) # Output: a, b, c, 1, 2, 3, x, y, z

# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

# Update
# The update() method inserts the items in set2 into set1:
# The update() changes the original set, and does not return a new set.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) # Output: a, b, c, 1, 2, 3

# Note Both the union() and update() methods will exclude any duplicate items. 
# If an item is present in both sets, it will only be included once in the result.



# Intersection
# The intersection() method returns a set that contains the similarity between two or more sets.
set1 = {"a", "b" , "c"}
set2 = {"b", "c", "d"}
set3 = set1.intersection(set2)
print(set3) # Output: b, c

cars = {"Ford", "BMW", "Volvo"}
mycars = {"Toyota", "BMW", "Honda"}
x = cars.intersection(mycars)
print(x) # Output: BMW  


# The "&" operator can be used in place of the intersection() method.

set1 = {"a", "b" , "c"}
set2 = {"b", "c", "d"}
set3 = set1 & set2
print(set3) # Output: b, c

cars = {"Ford", "BMW", "Volvo"}
mycars = {"Toyota", "BMW", "Honda"}
x = cars & mycars
print(x) # Output: BMW


# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.


# Intersection Update
# The intersection_update() method removes the items in the set that are not present in other, specified set(s).
# The intersection_update() method updates the original set, and does not return a new set.

set1 = {"a", "b" , "c"}
set2 = {"b", "c", "d"}
set1.intersection_update(set2)
print(set1) # Output: b, c

cars = {"Ford", "BMW", "Volvo"}
mycars = {"Toyota", "BMW", "Honda"}
cars.intersection_update(mycars)
print(cars) # Output: BMW

# The values True and 1 are considered the same value. The same goes for False and 0.
# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:

set1 = {"apple", 1,  "banana", False, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3) # Output: {False, True, 'apple'}


# Difference
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"a", "b" , "c"}
set2 = {"b", "c", "d"}
set3 = set1.difference(set2)
print(set3) # Output: a 

