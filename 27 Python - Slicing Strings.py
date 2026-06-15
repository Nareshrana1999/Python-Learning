# Slicing

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

Text = "Naresh"
print(Text[2:5])



# Slice From the Start
# By leaving out the start index, the range will start at the first character:

Text = "Slicing Strings"
print(Text[:15])



# Slice To the End
# By leaving out the end index, the range will go to the end:

Text = "Naresh Rana"
print(Text[2:])


# Negative Indexing
# Use negative indexes to start the slice from the end of the string:

Text = "Python"
print(Text[-4:-1])

# Get the characters:
# From: "t" in "Python" (position -4)
# To, but not included: "o" in "Python" (position -1):






