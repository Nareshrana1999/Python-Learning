# The global Keyword

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.


def myfunc():
    global x

x = "fantastic"
myfunc()
print("Python is " + x)



def myfunc2():
    global age

age = 27
myfunc2()
print(age)


# To change the value of a global variable inside a function
# refer to the variable by using the global keyword:

Name = "Naresh"

def func():
    global Name
    Name = "Rana"
func()

print(Name)


x = "python is fantastic"

def fun():
    global x
    x = "python is not fantastic"
fun()

print(x)



Age = 18
def func():
    global Age
    Age = 27
func()
print(Age)

