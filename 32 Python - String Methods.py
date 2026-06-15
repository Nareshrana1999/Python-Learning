# String Methods

# Python has a set of built-in methods that you can use on strings.
# Note: All string methods return new values. They do not change the original string.



# Method                                        Description

# capitalize()	                Converts the first character to upper case
print("hello".capitalize())

# casefold()	                Converts string into lower case
print("HELLO".casefold())

# center()	                    Returns a centered string
print("Hi".center(5))

# count()	                    Returns the number of times a specified value occurs in a string
print("Hello".count("l"))

# encode()	                    Returns an encoded version of the string
print("Hello".encode())

# endswith()	                Returns true if the string ends with the specified value
print("hello".endswith("lo"))

# startswith()	                Returns true if the string starts with the specified value
print("hello".startswith("he"))

# expandtabs()	                Sets the tab size of the string
text = "Python\tlanguage"
print(text.expandtabs(10))

# find()	                    Searches the string for a specified value and returns the position of where it was found
print("hello".find("e"))

# format()	                    Formats specified values in a string
text = "World"
print("Hello {}".format(text))

# format_map()	                Formats specified values in a string
data = {"name": "Rana", "age": 27}
text = "My name is {name} and I am {age} years old."
print(text.format_map(data))

data = {"name": "Naresh Rana", "age": 28, "location": "Bengaluru"}
print("My name is {name} and I am {age} years old. From {location} ".format(**data))

# index()	                    Searches the string for a specified value and returns the position of where it was found
text = "Python"
print(text.index("t"))

# isalnum()	                    Returns True if all characters in the string are alphanumeric
print("Python123".isalnum())

# isalpha()	                    Returns True if all characters in the string are in the alphabet
print("Python".isalpha())

# isascii()	                    Returns True if all characters in the string are ascii characters
print("Python".isascii())

# isdecimal()	                Returns True if all characters in the string are decimals
print("123".isdecimal())

# isdigit()	                    Returns True if all characters in the string are digits
print("123".isdigit())

# isidentifier()	            Returns True if the string is an identifier
print("my_var".isidentifier())

# islower()	                    Returns True if all characters in the string are lower case
print("hello".islower())

# isnumeric()	                Returns True if all characters in the string are numeric
print("123".isnumeric())

# isprintable()	                Returns True if all characters in the string are printable
print("123ABC".isprintable())

# isspace()	                    Returns True if all characters in the string are whitespaces
print("  ".isspace())

# istitle()	                    Returns True if the string follows the rules of a title
print("Hello World".istitle())

# isupper()	                    Returns True if all characters in the string are upper case
print("HELLO WORLD".isupper())

# join()	                    Joins the elements of an iterable to the end of the string
words = ["I", "Love", "Python"]
print(" ".join(words))

# ljust()	                    Returns a left justified version of the string
print("Python".ljust(10, "-"))

# lower()	                    Converts a string into lower case
print("PYTHON".lower())

# lstrip()	                    Returns a left trim version of the string
print("     Python".lstrip())
print("     Python")

# maketrans()	                Returns a translation table to be used in translations
table = str.maketrans("a", "x")
print("apple".translate(table))

# partition()	                Returns a tuple where the string is parted into three parts
text = "Python-Language"
print(text.partition("-"))

# replace()	                    Returns a string where a specified value is replaced with a specified value
print("Hello World".replace("World", "Python"))

# rfind()	                    Searches the string for a specified value and returns the last position of where it was found
print("banana".rfind("a"))

# rindex()	                    Searches the string for a specified value and returns the last position of where it was found
print("Mango".rindex("a"))

# rjust()	                    Returns a right justified version of the string
print("Python".rjust(10, "-"))

# rpartition()	                Returns a tuple where the string is parted into three parts
text = "Python-Language"
print(text.rpartition("-"))

# rsplit()	                    Splits the string at the specified separator, and returns a list
print("a,b,c".rsplit(",", 1))

# rstrip()	                    Returns a right trim version of the string
print("Python   ".rstrip())

# split()	                    Splits the string at the specified separator, and returns a list
print("Python Java C++".split())

# splitlines()	                Splits the string at line breaks and returns a list
text = "Hello\nWorld"
print(text.splitlines())

# strip()	                    Returns a trimmed version of the string
print("  Python  ".strip())

# swapcase()	                Swaps cases, lower case becomes upper case and vice versa
print("PyThOn".swapcase())

# title()	                    Converts the first character of each word to upper case
print("hello world".title())

# translate()	                Returns a translated string
table = str.maketrans("o", "0")
print("Hello".translate(table))

# upper()	                    Converts a string into upper case
print("python".upper())

# zfill()	                    Fills the string with a specified number of 0 values at the beginning
print("42".zfill(5))