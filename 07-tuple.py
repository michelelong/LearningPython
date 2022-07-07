#!/usr/local/bin/python3

# Tuple is an immutable list, elements cannot be updated or removed
# Enclosed in () instead of [] like a list

# A single element tuple must end with a comma
oneName = ("Abaddon", )
# Tuple elements are accessible by index
print("First element at index 0:", oneName[0])

print()

names = ("John", "Mary", "Sam", "Jody", "Dean", "Castiel")
print("Tuple:", names)
# Negative indexes count from the last element
print("Second element from the end:", names[-2])

# The len function get the tuple length
print("Length of tuple:", len(names), "\n")

# Tuples can be sliced just like a list
# [start:end:step] with end excluded
print("Slice elements 1-3:", names[1:4])

# Slice without a stop index goes to the end of the tuple
print("Slice from third element to the end:", names[2:])

print()

# New tuple
additions = ("Charlie", "Rowena", "Crowley")

# Unpack a tuple into individual variables
b, m, c = additions
print("Unpacking a tuple:", m)

# Create a new tuple by combining two tuples
family = names + additions
print("Combine two tuples:", family)

# Delete the whole tuple
# Attempting to access it will now cause an exception
del family

# Test if tuple contains element, returns a boolean
print('Is "Jody" in the tuple?', end=" ")
print("Jody" in names)

print()

print("Repeat with multiplication:", oneName * 2)

print()

# Iterate through elements in tuple
for n in names:
    print(n)

print()

nums = (1, 2, 3, 4, 5)
# Return min or max value in tuple
print("Min and max value in the tuple:", min(nums), "and", max(nums))

print()

# Comparing tuples only works in Python 2
# cmp(numsEven, numsOdd)

numList = [1, 2, 3, 4, 5]

# Convert a list into a tuple
numTuple = tuple(numList)
