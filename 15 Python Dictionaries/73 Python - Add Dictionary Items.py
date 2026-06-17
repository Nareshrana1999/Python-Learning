# Python - Add Dictionary Items

# Adding Items
# You can add an item to the dictionary by using a new index key and assigning a value to it:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
thisdict["color"] = "red"
print(thisdict) # Output: brand: Ford, model: Mustang, year: 1964, color: red


# Update() Method
# The update() method will update the dictionary with the items from a given argument. The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict) # Output: brand: Ford, model: Mustang, year: 1964, color: red




# Python Dictionaries Code Challenge

# Challenge: Dictionaries Basics
# Test your understanding of creating, accessing, changing, adding, and removing dictionary items.

# Instructions

# 1. Create a dictionary called car with the keys "brand", "model", "year" and values "Ford", "Mustang", 2024
# 2. Print the value of the "model" key
# 3. Add a new key "color" with the value "red"
# 4. Remove the "brand" key using pop()
# 5. Print the dictionary



# Create the dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2024
}

# Print the value of the "model" key
print(car["model"])  # Output: Mustang

# Add a new key "color" with the value "red"
car["color"] = "red"

# Remove the "brand" key using pop()
car.pop("brand")

# Print the dictionary
print(car)  # Output: model: Mustang, year: 2024, color: red

