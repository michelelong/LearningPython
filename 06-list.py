#!/usr/local/bin/python3

names = ["John", "Mary", "Sam", "Michele", "Dean", "Charlie"]
# Prints entire list with no need to iterate
print(names)

# The len() function get the list length
print("Length of the list:", len(names))

# List elements are directly accessible by index
print("Name at index 2:" + names[2])

print()

# Slice list with [start:end]
# end is excluded, [0:2] is 0-1
print("Slice elements zero and one:", names[0:2])

# Slice list with [start:end:increment]
# -1 indicates the end of list
print("Slice whole list incrementing by 2:", names[0:-1:2])

print()
# Reverse method changes the original list
names.reverse()
print("Reverse list:", names)

print()
additions = ["Dolly", "Maxwell", "Clyde"]
print("New list:", additions)

# Edit element at specific index
additions[1] = "Max"
print("Edit list element:", additions)

# Add element to end of list
additions.append("Romeo")
additions.append("Daisy")
print("Add list elements:", additions)

# Insert element at index
additions.insert(1, "Jack")
print("Insert list element:", additions)

# Remove first occurence of element
additions.remove("Max")
print("Remove list element:", additions)

# Remove element at index
del additions[1]
print("Remove list element:", additions)

# Remove element at index
additions.pop(1)
print("Remove list element:", additions)

print()

# Create a nested list
everyone = [names, additions]
print("Both lists are nested inside a new one: ")
print(everyone)

# Access first nested list, second element
print("Second element of the first nested list:", everyone[0][1])

# Access second nested list, third element
print("Third element of the second nested list:", everyone[1][2])

print()

# Return index of element
print("The index is:", names.index("Michele"))

print()

nums = [2, 1, 3, 5, 4]
# Edit array to sort elements in ascending order
nums.sort()
print("Ascending sort:", nums)

# Sort elements in descending order
nums.sort(reverse=True)
print("Descending sort:", nums)

print()

# Function returns length of a given string
def myFunc(e):
    return len(e)

# Sort list by function return value (passed element length)
names.sort(key=myFunc)
print("Sort by name length:", names)

print()

dataList = [("Andrew", 35, "Student"), ("Ali", 58, "Teacher"), ("Clyde", 11, "Dog")]
# A variable needs to represent each value in the tuple
facts = [name + " is " + str(age) + " years old and is a " + job + "." for name, age, job in dataList if job == "Dog"]
print(facts)

print()

# List comprehension generates a list according to specified logic
uppercaseNames = [name.upper() for name in names]
print("Uppercased names: ", uppercaseNames)

# List comprehension based on range
num_lst = [i for i in range(1, 11)]
print("One to ten: ", num_lst)

# List comprehension based on range with if condition
evens_to_20 = [e for e in range(21) if e % 2 == 0]
print("Evens up to 20: ", evens_to_20)

# List comprehension based on range with if/or condition
threes_or_fives = [x for x in range(1, 16) if (x % 3) == 0 or (x % 5) == 0]
print("Divisible by 3 or 5: ", threes_or_fives)

# List comprehension based on range with if/and condition
threes_and_fives = [x for x in range(1, 101) if (x % 3) == 0 and (x % 5) == 0]
print("Divisible by 3 and 5: ", threes_and_fives)

print()

common_nums = [] # Empty list
for i in evens_to_20: # Iterate over the list
    if i in threes_or_fives: # Check if list contains same element
        common_nums.append(i) # Add element to the empty list

print("Which numbers are in both lists? ", common_nums)

# The same as above, but done with list comprehension
common_nums.clear() # Reset list to empty
common_nums = [i for i in evens_to_20 if i in threes_or_fives]
print("Which numbers are in both lists? ", common_nums)
