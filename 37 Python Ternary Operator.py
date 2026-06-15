# The Ternary Operator

# The ternary operator allows you to assign one value if a condition is true, and another if it is false:

# Assign a value to x:
# Assign the value "WEEKEND!" if the number is higher than 5, otherwise "Workday":

num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print(x)

num = 4
x = "WEEKEND!" if num > 5 else "Workday"
print(x)



# Note: The ternary operator is not an actual operator, it is a conditional expression, or a shorthand if statement.



# Instead of Elif:
# The ternary operator can be used instead of elif in longer if statements:

# Example

# Assign:
# - "Fri" if num is 5
# - "Sat" if num is 6
# - "Sun" if num is 7
# - otherwise assign "weekday":

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)