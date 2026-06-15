# Logical Operators

# Logical operators are used to combine conditional statements:

# Operator	    Description	                                                    Example
# and 	        Returns True if both statements are true	                    x < 5 and  x < 10
x = 7
print(x > 5 and x < 10)

# or	        Returns True if one of the statements is true	                x < 5 or x < 4
x = 5
print(x > 3 and x < 6)

# not	        Reverse the result, returns False if the result is true	        not(x < 5 and x < 10)
x = 7
print(not(x > 5 and x < 10))
