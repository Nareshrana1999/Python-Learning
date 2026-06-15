# String Format

# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# age = 26
# Text = "Naresh Rana" + age           #This will produce an error:
# print(Text)


# But we can combine strings and numbers by using f-strings or the format() method!

# F-Strings

# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string
# simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

age = 26
Text = f"Naresh Rana {age}"
print(Text)

# Placeholders and Modifiers
# A placeholder can contain variables, operations, functions, and modifiers to format the value.

# Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

Version = 3
text = f"The Python version is {Version}"
print(text)

# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon :
# followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:

# Display the price with 2 decimals:

Version = 3
text = f"The Python version is {Version:.2f}"
print(text)


# A placeholder can contain Python code, like math operations:

text = f"The Python version is {9.4/3}"
print(text)


txt = f"The price is {20 * 59} dollars"
print(txt)


# Create the name variable
name = "Python"
# Print using an f-string
print(f"I love {name}")