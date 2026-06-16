# Python frozenset

# frozenset is an immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.


# Create a frozenset
# To create a frozenset, use the frozenset() function.

thisfrozenset = frozenset({"apple", "banana", "cherry"})
print(thisfrozenset) # Output: frozenset({'apple', 'banana', 'cherry'})

# frozenset() can be used on any iterable object, like lists and tuples:

thisfrozenset = frozenset(["apple", "banana", "cherry"])    # list
print(thisfrozenset) # Output: frozenset({'apple', 'banana', 'cherry'})

thisfrozenset = frozenset(("apple", "banana", "cherry"))    # tuple
print(thisfrozenset) # Output: frozenset({'apple', 'banana', 'cherry'}) 



# Frozenset Methods
# Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.

# type()
# From Python's perspective, frozensets are defined as objects with the data type 'frozenset':

thisfrozenset = frozenset({"apple", "banana", "cherry"})
print(type(thisfrozenset)) # Output: <class 'frozenset'>


# Methods                   Shortcut            Description
# union()                   |                   Returns a new frozenset containing the union of two sets
# intersection()            &                   Returns a new frozenset containing the intersection of two sets
# difference()              -                   Returns a new frozenset containing the difference of two sets
# symmetric_difference()    ^                   Returns a new frozenset containing the symmetric difference of two sets
# issubset()                <= / <              Returns True if this frozenset is a (proper) subset of another
# issuperset()              >= / >              Returns True if this frozenset is a (proper) superset of another
# isdisjoint()              isdisjoint()        Returns True if this frozenset has no elements in common with another
# copy()                    copy()              Returns a shallow copy of the frozenset


# copy()
# The copy() method returns a shallow copy of the frozenset.
set1 = frozenset({"a", "b" , "c"})
set2 = set1.copy()
print(set2) # Output: frozenset({'a', 'b', 'c'})


#Union
# The union() method returns a new frozenset that contains all the items from both sets, duplicates are excluded.
# Join set1 and set2 into a new set:
set1 = frozenset({"a", "b" , "c"})
set2 = frozenset({"d", "e", "f"})
set3 = set1.union(set2)
print(set3) # Output: frozenset({'a', 'b', 'c', 'd', 'e', 'f'})


set1 = frozenset({"a", "b" , "c"})
set2 = frozenset({"d", "e", "f"})
set3 = set1 | set2
print(set3) # Output: frozenset({'a', 'b', 'c', 'd', 'e', 'f'})


#Intersection
# The intersection() method returns a new frozenset that contains only the items that are present in both sets.
# Return a new frozenset that contains only the items that are present in both sets:
set1 = frozenset({"a", "b" , "c"})
set2 = frozenset({"c", "d", "e"})
set3 = set1.intersection(set2)
print(set3) # Output: frozenset({'c'})


set1 = frozenset({"a", "b" , "c"})
set2 = frozenset({"c", "d", "e"})
set3 = set1 & set2
print(set3) # Output: frozenset({'c'})  


#Difference
# The difference() method returns a new frozenset that contains only the items that are in the first set but not in the second set.
# Return a new frozenset that contains only the items that are in set1 but not in set2:
set1 = frozenset({"a", "b" , "c"})
set2 = frozenset({"c", "d", "e"})
set3 = set1.difference(set2)
print(set3) # Output: frozenset({'a', 'b'})


set1 = frozenset({"a", "b" , "c"})
set2 = frozenset({"c", "d", "e"})
set3 = set1 - set2
print(set3) # Output: frozenset({'a', 'b'})


#Symmetric Difference
# The symmetric_difference() method returns a new frozenset that contains only the items that are in either set, but not in both.
# Return a new frozenset that contains only the items that are in either set1 or set2, but not in both:
set1 = frozenset({"a", "b" , "c"})
set2 = frozenset({"c", "d", "e"})
set3 = set1.symmetric_difference(set2)
print(set3) # Output: frozenset({'a', 'b', 'd', 'e'})

set1 = frozenset({"a", "b" , "c"})
set2 = frozenset({"c", "d", "e"})
set3 = set1 ^ set2
print(set3) # Output: frozenset({'a', 'b', 'd', 'e'})


# issubset()
# The issubset() method returns True if all items in the set are present in another set, otherwise it returns False.
set1 = frozenset({"a", "b" , "c"})
set2 = frozenset({"f", "e", "d", "c", "b", "a"})
x = set1.issubset(set2)
print(x) # Output: True 

set1 = frozenset({1, 2})
set2 = frozenset({1, 2, 3})
print(set1.issubset(set2)) # Output: True
print(set1 <= set2) # Output: True



# issuperset()
# The issuperset() method returns True if all items in another set are present in the set, otherwise it returns False.
set1 = frozenset({"a", "b" , "c"})  
set2 = frozenset({"f", "e", "d", "c", "b", "a"})
x = set2.issuperset(set1)
print(x) # Output: True

a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b)) # Output: True
print(a >= b) # Output: True
print(a > b) # Output: True


cars = frozenset({"Ford", "BMW", "Volvo", "Honda"})
mycars = frozenset({"Ford", "BMW", "Volvo"})
print(cars.issuperset(mycars)) # Output: True
print(cars >= mycars) # Output: True
print(cars > mycars) # Output: True


# isdisjoint()
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
set1 = frozenset({"a", "b" , "c"})
set2 = frozenset({"f", "e", "d"})
x = set1.isdisjoint(set2)
print(x) # Output: True

a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b)) # Output: True
print(a.isdisjoint(c)) # Output: False


