# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.

print("Hello")
print('Hello')


# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)


# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

# You can use three double quotes:

text = """He said, "Hello World"."""
print(text)

# Or three single quotes:

text = '''It's a beautiful day.'''
print(text)


# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

# Get the character at position 1 (remember that the first character has the position 0):

Text = "Naresh"
print(Text[2])

