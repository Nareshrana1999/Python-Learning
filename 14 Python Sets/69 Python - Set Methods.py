# Python - Set Methods

# Set Methods
# Python has a set of built-in methods that you can use on sets.

# Method                            Description                                                                             
# add()                             Adds an element to the set
# clear()                           Removes all the elements from the set
# copy()                            Returns a copy of the set
# difference()                      Returns a set containing the difference between two or more sets
# difference_update()               Removes the items in this set that are also included in another, specified set
# discard()                         Remove the specified item
# intersection()                    Returns a set, that is the intersection of two other sets
# intersection_update()             Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()                      Returns whether two sets have a intersection or not
# issubset()                        Returns whether another set contains this set or not
# issuperset()                      Returns whether this set contains another set or not
# pop()                             Removes an element from the set
# remove()                          Removes the specified element
# symmetric_difference()            Returns a set with the symmetric differences of two sets
# symmetric_difference_update()     Inserts the symmetric differences from this set and another
# union()                           Return a set containing the union of sets



# Python Sets Code Challenge

# Challenge: Sets Basics
# Test your understanding of creating, adding, removing, and checking set items.

# Instructions

# 1. Create a set called colors with the values "red", "green", "blue"
# 2. Print the set
# 3. Add "yellow" to the set using add()
# 4. Remove "green" from the set using discard()
# 5. Print the number of items using len()


# Create the set
colors = {"red", "green", "blue"}
# Print the set
print(colors)
# Add "yellow"
colors.add("yellow")
# Remove "green"
colors.discard("green")
# Print the number of items
print(len(colors))


