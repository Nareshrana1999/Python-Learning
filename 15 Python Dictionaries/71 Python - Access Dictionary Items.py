# Python - Access Dictionary Items

# Access Dictionary Items
# You can access the items of a dictionary by referring to its key name, inside square brackets

from doctest import Example


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"]) # Output: Mustang
print(thisdict["year"]) # Output: 1964

# get() Method
# the get() method will also give you the same result:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict.get("model")) # Output: Mustang
print(thisdict.get("year")) # Output: 1964



# get keys
# The keys() method will return a list of all the keys in the dictionary.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.keys()) # Output: dict_keys(['brand', 'model', 'year'])

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

# Example
# Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
y = car.values()
print(x) # Output: dict_keys(['brand', 'model', 'year'])
print(y) # Output: dict_values(['Ford', 'Mustang', 1964])
car["color"] = "red"
print(x) # Output: dict_keys(['brand', 'model', 'year', 'color'])
print(y) # Output: dict_values(['Ford', 'Mustang', 1964, 'red'])


# Get Values
# The values() method will return a list of all the values in the dictionary.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict.values()) # Output: dict_values(['Ford', 'Mustang', 1964])

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

# Example
# Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
y = car.values()
print(x) # Output: dict_keys(['brand', 'model', 'year'])
print(y) # Output: dict_values(['Ford', 'Mustang', 1964])
car["color"] = "red"
print(x) # Output: dict_keys(['brand', 'model', 'year', 'color'])
print(y) # Output: dict_values(['Ford', 'Mustang', 1964, 'red'])



# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}   
print(thisdict.items()) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# The returned list is a view of the items in the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

# Example
# Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car["year"] = "1969"
print(x) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', '1969'), ('color', 'red')])

y = car.items()     
print(y) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', '1969')])
car["color"] = "red"
print(y) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', '1969'), ('color', 'red')])




# Check if Key Exists
# To determine if a specified key is present in a dictionary, use the in keyword:


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
