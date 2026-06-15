# Global Variables

# Variables that are created outside of a function
# (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.


x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()


Name = "Naresh Rana"
def func():
  print("My Name is " + Name)
func()



# If you create a variable with the same name inside a function
# this variable will be local, and can only be used inside the function.
# The global variable with the same name will remain as it was, global and with the original value.


Job = "Software Engineer"

def func():
    Job = "DevOps Engineer"
    print("My Job is " + Job )
func()

print(Job)



Location = 'Bengaluru'

def func():
    Location = 'Hyderabad'
    print('my location is ' + Location)
func()
print(Location)


Language = 'Python'
def func():
    print('my language is ' + Language)
func()

