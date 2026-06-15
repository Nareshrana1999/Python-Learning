# Python Booleans

# Booleans represent one of two values: True or False.

# Boolean Values:
# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)


# When you run a condition in an if statement, Python returns True or False:


# Print a message based on whether the condition is True or False:

a = 20
b = 30

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")


a = 90
b = 80
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")




# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,

# Example
# Evaluate a string and a number:

print(bool("Hello"))            # any string is true
print(bool(0))                  # 0 is false
print(bool(" "))                # noting " " is false
print(bool(1))                  # 1 or above number is true


# Evaluate two variables:

a = 0
b = "Hello"
print(bool(a))
print(bool(b))


# Most Values are True

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


# Some Values are False

# In fact, there are not many values that evaluate to False,
# except empty values, such as (), [], {}, "", the number 0, and the value None.
# And of course the value False evaluates to False.

# The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# One more value, or object in this case, evaluates to False, and
# that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0                             # return 0 is false class doesn't have value

myobj = myclass()
print(bool(myobj))


class person():
    def __len__(self):
        return 10                        # return 10 is True class have value
obj = person()
print(bool(obj))



# Functions can Return a Boolean

# You can create functions that returns a Boolean Value:
# Print the answer of a function:

def function():
    return False
print(function())

def function():
    return True
print(function())


# Print "YES!" if the function returns True, otherwise print "NO!":

def myfunction():
    return True
if myfunction():
    print("Yes")
else:
    print("No")


# Python also has many built-in functions that return a boolean value,
# like the isinstance() function,
# which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))           # x have integer value so True

y = "Hello"
print(isinstance(y, int))           # y doesn't have integer value so False

a = "Hello"
print(isinstance(a, str))           # a have string value so True
