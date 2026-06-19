# Python Recursion

# Recursion
# Recursion is a programming technique where a function calls itself in order to solve a problem. 
# It is often used to solve problems that can be broken down into smaller, similar subproblems.

# Recursion is when a function calls itself.
# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. 
# However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.



# Example
# A simple recursive function that counts down from 5:

def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)
countdown(5)   # Output: 5, 4, 3, 2, 1, Blastoff!


# Example
# A simple recursive function that calculates the factorial of a number:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# Base case and recursive case

# In recursion, it is important to have a base case that stops the recursion from continuing indefinitely.
# The base case is the condition under which the function stops calling itself.
# The recursive case is the part of the function that calls itself with a modified argument, moving towards the base case.

# Every recursive function must have two parts:

# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument

# Without a base case, the function would call itself forever, causing a stack overflow error.


# Example
# Identifying base case and recursive case:

def moneycount(n):
    if n <= 0:  # Base case
        print("No more money!")
    else:  # Recursive case
        print(f"You have ${n}")
moneycount(5) 

# The base case is crucial. Always make sure your recursive function has a condition that will eventually be met.


# Fibonacci Sequence
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
# The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# The sequence continues indefinitely, with each number being the sum of the two preceding ones.
#  We can use recursion to find a specific number in the sequence:

# Example
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(10))  # Output: 55



# Recursion with Lists

# Recursion can also be used to process lists.
# Recursion can be used to process lists by handling one element at a time:

# Example
# Calculate the sum of all elements in a list:

def sum_list(lst):
    if len(lst) == 0:  # Base case
        return 0
    else:  # Recursive case
        return lst[0] + sum_list(lst[1:]) # The function takes the first element of the list (lst[0]) and adds it to the result of calling sum_list on the rest of the list (lst[1:]). This continues until the list is empty, at which point it returns 0.
    
print(sum_list([1, 2, 3, 4, 5]))  # Output: 15             # 1+2+3+4+5 = 15


# Find the maximum value in a list:

def find_max(lst):
    if len(lst) == 1:  # Base case
        return lst[0]
    else:  # Recursive case
        max_of_rest = find_max(lst[1:])  # The function takes the first element of the list (lst[0]) and compares it to the maximum of the rest of the list (find_max(lst[1:])). This continues until there is only one element left in the list, at which point it returns that element as the maximum.
        return lst[0] if lst[0] > max_of_rest else max_of_rest
        
print(find_max([3, 1, 4, 1, 5, 9, 2, 6]))  # Output: 9




# Recursion Depth Limit

# Python has a recursion depth limit to prevent infinite recursion from causing a stack overflow.
# The default limit is 1000, but it can be changed using the sys module:

# Example
# Check the recursion limit:

import sys
print(sys.getrecursionlimit())  # Output: 1000 (default value)




