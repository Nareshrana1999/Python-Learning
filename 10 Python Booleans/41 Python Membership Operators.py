# Membership Operators

# Membership operators are used to test if a sequence is presented in an object:



# Operator	        Description                                                                         	Example
# in 	            Returns True if a sequence with the specified value is present in the object	        x in y
# not in	        Returns True if a sequence with the specified value is not present in the object	    x not in y


# Check if "banana" is present in a list:

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("mango" in fruits)


# Check if "pineapple" is NOT present in a list:

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)
print("apple" not in fruits)


# Membership in Strings

# The membership operators also work with strings:

text = "Hello World"
print('H'in text)
print('o' in text)
print('b' not in text)

