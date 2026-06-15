# Python - Escape Characters

# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.


# Example
# You will get an error if you use double quotes inside a string that is surrounded by double quotes:

# txt = "We are the so-called "Vikings" from the north."


# To fix this problem, use the escape character \":

# The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)



# Single Quote
txt = 'It\'s alright.'
print(txt)


# Backslash
txt = "This will insert one \\ (backslash)."
print(txt)


# New Line
txt = "Naresh\nRana\n27"
print(txt)


# Carriage Return
txt = "Hello\rWorld!"
print(txt)


# Tab
txt = "Hello\tWorld!"
print(txt)


# Backspace
txt = "Hello \bWorld!"
print(txt)


# Octal value  \ooo
txt = "\110\145\154\154\157"
print(txt)


# Hex value \xhh
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)









