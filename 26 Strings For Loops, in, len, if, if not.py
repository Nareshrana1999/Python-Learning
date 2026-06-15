# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

# Loop through the letters in the word "banana":

for x in "banana":
    print(x)

for text in "Naresh":
    print(text)


# String Length
# To get the length of a string, use the len() function.

# The len() function returns the length of a string:

Text = "Rana"
print(len(Text))


# To check if a certain phrase or character is present in a string, we can use the keyword in.

# Check if "Text" is present in the following text:

text = "Naresh Rana"
print("Rana" in text)            # Rana Text present so its "True"
print("Hello" in text)           # Hello Text not present so its "False"


# Use it in an if statement:

text = "Naresh Rana"
if "Rana" in text:
        print("Yes,'Rana' is Present", text)


# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

# Check if "expensive" is NOT present in the following text:

text = "The best things in life are free!"
print("Expensive" not in text, "'Expensive' is Not Present in",text)


# Use it in an if statement:

text = "Hello World"
if "Rana" not in text:
    print("Yes,'Rana' is Not Present", text , "Text")


car = "Mercedes, Audi, BMW, Volvo"
if "Tesla" not in car:
    print("'Tesla' is Not Present in this List", car)

