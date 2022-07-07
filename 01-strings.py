#!/usr/local/bin/python3

# Strings can be defined with single or double quotes
firstName = "Michele"
lastName = "Long"

# Python2 print statements do not use paratheses
print("Print a variable: ", firstName)
print("Concatenate variables: ", firstName + " " + lastName)

print()

# Specify end of line character, default is new line
print("This is the end of the line", end="!\n")
# Specify a separation character
print("Change", "separation", "character.", sep="-")

print()

# Strings are character arrays[] and can be accessed by index
print("The character at index 2 is: " + firstName[2])

age = 99
# Format string with variable substitution
# %s for string, %d for decimal, %i for integer, %f for float, and %c for character
# 02d will pad to two digits, .2f will limit decimal to two places
print("My age is %s" % age)

# String format method with placeholders
print("The {} in {} falls mainly in the {}".format('rain', 'Spain', 'plains'))

print()

# Cast the returned integer to a string for printing
print("String length: " + str(len(firstName)))

print("Uppercase function: " + lastName.upper() + " " + lastName.lower())

print()

# docstring, used to document functions
haiku = """
The old pond,
A frog jumps in:
Plop!
"""

# Escape special characters with backslash (\)
quote = 'This isn\'t flying, this is falling with style!'
print("Escaped quote:", quote)

# Slice string from 0 index to 4
print("Slice:", quote[0:5])

print()

# Search string for a substring
print("Substring 'fly' starts at index: %s" % (quote.find("fly")))
print("Number of t's in string: %s" % (quote.count("t")))

# lstrip and rstrip remove whitespace only from the beginning or only from the end
startSpace = "   Remove whitespace from the beginning and end of strings.   "
print(startSpace.strip())
