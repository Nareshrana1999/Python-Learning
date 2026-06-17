# Python Elif Statement

# elif keyword 

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
# The elif keyword allows you to check multiple expressions for True and execute a block of code as soon as one of the conditions evaluates to True.

a = 200
b = 100
if b > a:
    print("b is greater than a") # Output: (No output, condition is false)
elif a < b:
    print("a is less than b") # Output: a is less than b


# multiple elif statements

# You can have as many elif statements as you want, and the else statement is optional.
# You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true.

Score = 85
if Score >= 90:
    print("Grade: A") # Output: (No output, condition is false)
elif Score >= 80:
    print("Grade: B") # Output: Grade: B
elif Score >= 70:
    print("Grade: C") # Output: Grade: C