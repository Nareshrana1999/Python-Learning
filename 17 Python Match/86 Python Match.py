# Python Match

# The match statement is used to perform different actions based on different conditions.

# The Python Match Statement
# The match statement is similar to a switch statement in other programming languages.
# It allows you to compare a value against multiple patterns and execute code based on which pattern matches.

# Instead of writing many "if".."else" statements, you can use the match statement.

# The match statement selects one of many code blocks to be executed.

# Syntax

# match expression:
#  case x:
#    code block
#  case y:
#   code block
#  case z:
#    code block 


# This is how it works:

# The match expression is evaluated once.
# The value of the expression is compared with the values of each case.
# If there is a match, the associated block of code is executed.


# The example below uses the weekday number to print the weekday name:

day = 3
match day:
    case 1:
        print("Monday")         # Output: (No output, condition is false)
    case 2:
        print("Tuesday")        # Output: (No output, condition is false)
    case 3:
        print("Wednesday")      # Output: Wednesday
    case 4:
        print("Thursday")       # Output: (No output, condition is false)
    case 5:
        print("Friday")         # Output: (No output, condition is false)
    case 6:
        print("Saturday")       # Output: (No output, condition is false)
    case 7:
        print("Sunday")         # Output: (No output, condition is false)

# The match statement is a more elegant way to handle multiple conditions compared to using multiple if statements.


# Default Case or Default Value

# You can use the case "_" statement to define a default case that will be executed if no other case matches.

day = 4
match day:
    case 5:
        print("Friday")         # Output: (No output, condition is false)
    case 6:
        print("Saturday")       # Output: (No output, condition is false)
    case 7:
        print("Sunday")         # Output: (No output, condition is false)
    case _:
        print("Looking forward to the Weekend!")  # Output: Looking forward to the Weekend!

# Note: The value _ will always match, so it is important to place it as the last case like "else" to make it behave as a default case.


# Combine Values

# You can combine multiple values in a single case using the "|" operator.


day = 3
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")        # Output: Weekday
    case 6 | 7:
        print("Weekend")        # Output: (No output, condition is false)



# If Statements as Guards
# You can use if statements as guards to add additional conditions to a case.
# You can add if statements in the case evaluation as an extra condition-check:

day = 3
month = "March"
match day:
    case 1 | 2 | 3 | 4 | 5 if month == "March":
        print("Weekday in March")        # Output: Weekday in March
    case 6 | 7 if month == "March":
        print("Weekend in March")        # Output: (No output, condition is false)
    case _:
        print("Invalid day number.")  # This will be executed if no other case matches.


month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")             # Output: (No output, condition is false)
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")               # Output: A weekday in May
  case _:
    print("No match")                       # Output: (No output, condition is false)



My_car = "BMW"
mileage = 50
match My_car:
    case "BMW" if mileage < 30:
        print("Not Your Car")  # Output: (No output, condition is false)
    case "BMW" if mileage < 40:
        print("Not Your Car")  # Output: (No output, condition is false)
    case "BMW" if mileage == 50:
        print("This is Your Car")  # Output: This is Your Car
    case _:
        print("No Car found")  # Output: (No output, condition is false)
    
