# Python Else Statement

# The Else Keyword

# The else keyword catches anything which isn't caught by the preceding conditions.
# The else statement is executed when the if condition (and any elif conditions) evaluate to False.

age = 30
if age < 18:
    print("You are a minor.") # Output: (No output, condition is false)
elif age < 25:
    print("You are a young adult.") # Output: (No output, condition is false)
else:
    print("You are an adult.")  # Output: You are an adult.


# Else Without Elif
# You can also use the else statement without the elif statement.

# This creates a simple two-way choice: if the condition is true, execute one block; otherwise, execute the else block.

age = 20
if age < 18:
    print("You are a minor.") # Output: (No output, condition is false)
else:
    print("You are an adult.")  # Output: You are an adult.


# How the Else Statement Works

# The else statement provides a default action when none of the previous conditions are true. 
# Think of it as a "catch-all" for any scenario not covered by your if and elif statements.

# Note: The else statement must come last. You cannot have an elif after an else.

number = 10
if number < 0:
    print("The number is negative.") # Output: (No output, condition is false)
else:
    print("The number is non-negative.",number)  # Output: The number is non-negative, 10


# Complete If-Elif-Else Chain
# You can combine if, elif, and else statements to create a complete decision-making structure.

Temperature = 75
if Temperature < 60:
    print("It's cold outside.") # Output: (No output, condition is false)
elif Temperature < 80:
    print("The weather is pleasant.")  # Output: The weather is pleasant.
else:
    print("It's hot outside.") # Output: (No output, condition is false)


# Else as Fallback

# The else statement acts as a fallback that executes when none of the preceding conditions are true. 
# This makes it useful for error handling, validation, and providing default values.

# Password Validation:

password = "Securepassword@123"
if len(password) < 8:
    print("Password is too short.") # Output: (No output, condition is false)   
else:
    print("Password is valid.")  # Output: Password is valid.

    









