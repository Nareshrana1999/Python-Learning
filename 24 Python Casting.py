# Python Casting

# Specify a Variable Type
# There may be times when you want to specify a type on to a variable.
# This can be done with casting.
# Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.


# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


# Integer:

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x)
print(y)
print(z)

# Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x)
print(y)
print(z)
print(w)


# Strings:

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x)
print(y)
print(z)



#Integer:
# Converting to Integer: int()
# The int() function drops anything after the decimal point when converting a float.
# It does not round to the nearest number.

# From Float (Truncates, does NOT round)
print(int(9.99))   # Output: 9
print(int(-2.5))   # Output: -2

# From String (Must look like a whole number)
print(int("42"))   # Output: 42


# Float:
# Converting to Float:
# float()The float() function adds a decimal point to integers or extracts fractional numbers from strings.


# From Integer
print(float(7))     # Output: 7.0
# From String
print(float("3.14")) # Output: 3.14
print(float("5"))    # Output: 5.0



# String:
# Converting to String:
# str()The str() function is the safest conversion.
# It converts absolutely any integer or float into text format by wrapping it in quotes.

print(str(100))    # Output: '100'
print(str(55.23))  # Output: '55.23'


