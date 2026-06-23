# Python range

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# Syntax: range(start, stop, step)

# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times. 
# This set of numbers has its own data type called range.

# Note: Immutable means that it cannot be modified after it is created.

# Creating a range object:

# tThe range() function can be called with 1, 2, or 3 arguments, using this syntax:
# range(start, stop, step)


# call range() with 1 argument

# The range() function can be called with a single argument, which specifies the stop value. 
# The start value defaults to 0, and the step value defaults to 1.

# Example
# Create a range of numbers from 0 to 9:

x = range(10)  # The range() function is called with a single argument 10, which specifies the stop value. The start value defaults to 0, and the step value defaults to 1. This creates a range object that represents the sequence of numbers from 0 to 9.
print(x)  # Output: range(0, 10)   # The range object is printed, which shows the start and stop values of the range.
print(list(x))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   


# call range() with 2 arguments

# The range() function can be called with two arguments, which specify the start and stop values.

# Example
# Create a range of numbers from 2 to 9:

x = range(2, 10)  # The range() function is called with two arguments 2 and 10, which specify the start and stop values. The step value defaults to 1. This creates a range object that represents the sequence of numbers from 2 to 9.
print(x)  # Output: range(2, 10)   # The range object is printed, which shows the start and stop values of the range.
print(list(x))  # Output: [2, 3, 4, 5, 6, 7, 8, 9]



# call range() with 3 arguments

# The range() function can be called with three arguments, which specify the start, stop, and step values.

# Example
# Create a range of numbers from 2 to 9, with a step of 2:

x = range(2, 10, 2)  # The range() function is called with three arguments 2, 10, and 2, which specify the start, stop, and step values. This creates a range object that represents the sequence of numbers from 2 to 9, with a step of 2.
print(x)  # Output: range(2, 10, 2)   # The range object is printed, which shows the start, stop, and step values of the range.
print(list(x))  # Output: [2, 4, 6, 8]  



# using range() 

# The range() function is commonly used in for loops to iterate over a sequence of numbers.

# Example
# Iterate over each value in a range:

for x in range(10):     # The for loop iterates over each value in the range object created by range(10), which represents the sequence of numbers from 0 to 9. For each iteration, the current value is assigned to the variable x, and the print() function is called to output the value of x.   
  print(x) # Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


# Using List to Display Ranges

# The range() function returns a range object, which is an iterable.
# To display the values in a range, we can convert the range object to a list using the list() function.

# Example
# Display the values in a range as a list:

x = range(10)  # The range() function is called with a single argument 10, which specifies the stop value. The start value defaults to 0, and the step value defaults to 1. This creates a range object that represents the sequence of numbers from 0 to 9.
print(list(x))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # The list() function is called with the range object x as an argument, which converts the range object to a list. The resulting list is printed, which shows the values in the range from 0 to 9.

# Example
# Convert different ranges to lists:

print(list(range(5)))  # Output: [0, 1, 2, 3, 4]   # The range() function is called with a single argument 5, which specifies the stop value. The start value defaults to 0, and the step value defaults to 1. This creates a range object that represents the sequence of numbers from 0 to 4. The list() function is called with the range object as an argument, which converts the range object to a list. The resulting list is printed, which shows the values in the range from 0 to 4.
print(list(range(2, 5)))  # Output: [2, 3, 4]   # The range() function is called with two arguments 2 and 5, which specify the start and stop values. The step value defaults to 1. This creates a range object that represents the sequence of numbers from 2 to 4. The list() function is called with the range object as an argument, which converts the range object to a list. The resulting list is printed, which shows the values in the range from 2 to 4.
print(list(range(2, 10, 2)))  # Output: [2, 4, 6, 8]   # The range() function is called with three arguments 2, 10, and 2, which specify the start, stop, and step values. This creates a range object that represents the sequence of numbers from 2 to 9, with a step of 2. The list() function is called with the range object as an argument, which converts the range object to a list. The resulting list is printed, which shows the values in the range from 2 to 9 with a step of 2.   



# slicing a range

# like lists, ranges can be sliced using the slice notation [start:stop:step].

# Example
# Slice a range to get every second number from 0 to 9:

x = range(10)  # The range() function is called with a single argument 10, which specifies the stop value. The start value defaults to 0, and the step value defaults to 1. This creates a range object that represents the sequence of numbers from 0 to 9.
print(list(x[::2]))  # Output: [0, 2, 4, 6, 8]   # The slice notation [::2] is used to slice the range object x, which selects every second number from the range. The list() function is called with the sliced range object as an argument, which converts the sliced range object to a list. The resulting list is printed, which shows the values in the range from 0 to 9 with a step of 2.


# Extract a subsequence from a range:

r = range(10)
print(r[2])     # Output: 2   # The slice notation [2] is used to extract the element at index 2 from the range object r, which represents the sequence of numbers from 0 to 9. The resulting value is printed, which shows the value at index 2 in the range.
print(r[:3])    # Output: range(0, 3)   # The slice notation [:3] is used to extract the subsequence from the start of the range object r up to, but not including, index 3. The resulting range object is printed, which shows the start and stop values of the subsequence.


# Note: The first print statement returns the value at index 2, and the second print statement returns a new range object, from index 0 to 3.



# Membership Testing

# We can use the "in" and "not in" operators to test if a value is present in a range.

# Example
# Test if a value is present in a range:

x = range(10)  # The range() function is called with a single argument 10, which specifies the stop value. The start value defaults to 0, and the step value defaults to 1. This creates a range object that represents the sequence of numbers from 0 to 9.
print(5 in x)   # Output: True   # The "in" operator is used to test if the value 5 is present in the range object x. The result of the membership test is printed, which shows that 5 is indeed present in the range.
print(15 in x)  # Output: False   # The "in" operator is used to test if the value 15 is present in the range object x. The result of the membership test is printed, which shows that 15 is not present in the range.  

# Example
# Test if a value is not present in a range:

x = range(10)  # The range() function is called with a single argument 10, which specifies the stop value. The start value defaults to 0, and the step value defaults to 1. This creates a range object that represents the sequence of numbers from 0 to 9.
print(5 not in x)   # Output: False   # The "not in" operator is used to test if the value 5 is not present in the range object x. The result of the membership test is printed, which shows that 5 is indeed present in the range, so the result is False.
print(15 not in x)  # Output: True   # The "not in" operator is used to test if the value 15 is not present in the range object x. The result of the membership test is printed, which shows that 15 is not present in the range, so the result is True.


# The return value is True when the number is present in the range, and False when it is not



# length of a range

# We can use the len() function to get the number of items in a range.

# Example
# Get the length of a range:

x = range(10)  # The range() function is called with a single argument 10, which specifies the stop value. The start value defaults to 0, and the step value defaults to 1. This creates a range object that represents the sequence of numbers from 0 to 9.
print(len(x))  # Output: 10   # The len() function is called with the range object x as an argument, which returns the number of items in the range. The resulting length is printed, which shows that there are 10 items in the range from 0 to 9.


r = range(0, 10, 2)     # The range() function is called with three arguments 0, 10, and 2, which specify the start, stop, and step values. This creates a range object that represents the sequence of numbers from 0 to 9, with a step of 2.
print(len(r))  # Output: 5   # The len() function is called with the range object r as an argument, which returns the number of items in the range. The resulting length is printed, which shows that there are 5 items in the range from 0 to 10 with a step of 2.
