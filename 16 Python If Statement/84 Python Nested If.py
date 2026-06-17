# Python Nested If

# Nested If Statements

# You can have if statements inside if statements, this is called nested if statements.

x = 10
if x > 5:
    if x < 15:
        print("x is greater than 5 and less than 15")   # Output: x is greater than 5 and less than 15


x = 41
if x > 10:
  print("Above ten,")  # Output: Above ten,
  if x > 20:
    print("and also above 20!")  # Output: and also above 20!
  else:
    print("but not above 20.")   # Output: 


# How Nested If Statements Work

# The inner if statement is only executed if the outer if statement evaluates to True. 
# The code evaluates from the outermost condition inward.

# Checking multiple conditions with nesting:

age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive") # Output: You can drive
  else:
    print("You need a license") # Output: (No output, condition is false)
else:
  print("You are too young to drive") # Output: (No output, condition is false)



# Multiple Levels of Nesting

# You can have multiple levels of nesting, but it is generally not recommended as it can make the code harder to read and understand.
# You can nest as many levels deep as needed, but keep in mind that too many levels can make code harder to read.


# Three levels of nesting:

score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")       # Output: Pass with good standing
    else:
      print("Pass but missing assignment")   # Output: (No output, condition is false)
  else:
    print("Pass but low attendance")         # Output: (No output, condition is false)
else:
  print("Fail")                              # Output: (No output, condition is false)


# Nested If vs Logical Operators

# You can also use logical operators (and, or, not) to combine conditions instead of nesting if statements.
# Sometimes nested if statements can be simplified using logical operators like and. The choice depends on your logic.

# nested if statement:
x = 10
if x > 5:
  if x < 15:
    print("x is greater than 5 and less than 15")   # Output: x is greater than 5 and less than 15

temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!") # Output: Perfect beach weather!


# using logical operator "and":
x = 10
if x > 5 and x < 15:
  print("x is greater than 5 and less than 15")   # Output: x is greater than 5 and less than 15


temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")   # Output: Perfect beach weather!


# Both approaches produce the same result. 
# Use nested if statements when the inner logic is complex or depends on the outer condition. 
# Use and when both conditions are simple and equally important.


# Example

# Login validation with nested checks:

username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")             # Output: Login successful
    else:
      print("Account is not active")        # Output: (No output, condition is false)
  else:
    print("Password required")              # Output: (No output, condition is false)
else:
  print("Username required")                # Output: (No output, condition is false)



# Grade calculation with nested logic:

score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")                   # Output: A+ grade
  else:
    print("A grade")                    # Output: (No output, condition is false)
elif score >= 80:
  print("B grade")                      # Output: (No output, condition is false)
else:
  print("C grade or below")             # Output: (No output, condition is false)










