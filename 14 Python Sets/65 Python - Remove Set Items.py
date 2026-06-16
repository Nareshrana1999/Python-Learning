# Python - Remove Set Items

# Remove Set Items
# To remove an item in a set, use the remove(), or the discard() method.
# The remove() method will raise an error if the specified item does not exist, and the discard() method will not raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) # Output: apple, cherry


carsset = {"Ford", "BMW", "Volvo"}
carsset.discard("BMW")
print(carsset) # Output: Ford, Volvo


# The pop() method removes a random item from the set, and returns the removed item.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()   
print(x) # Output: apple (or banana, or cherry)
print(thisset) # Output: the remaining items in the set


# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # Output: set()  


# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # this will raise an error because the set no longer exists



