# Python Dictionaries

# {:} Curly braces with colons
# Dictionaries are written with curly brackets, and have keys and values:

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Example
# Create and print a dictionary:

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict) # Output: brand: Ford, model: Mustang, year: 1964


# Dictionary Items

# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict["brand"]) # Output: Ford


# Ordered or Unordered

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.


# Changeable
# Dictionaries are changeable, meaning we can change, add or remove items after the dictionary has been created.


# Duplicate not allowed
# Dictionaries cannot have two items with the same key:

# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,          # Duplicate key, the value will be overwritten
  "year": 2020           # Duplicate key, the value will be overwritten
}
print(thisdict) # Output: brand: Ford, model: Mustang, year: 2020




