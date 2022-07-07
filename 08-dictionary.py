#!/usr/local/bin/python3

# Dictionaries are key:value pairs
# Keys must be unique
# Any immutable object can be used as a key

# Create dictionary with dict function and keyword arguments
dictFunc = dict(Michele=5)

# Create dictionary with dict function and iteratables
tupDict = dict([("Michele", 15)])

# Create dictionary with key/value pairs
dictionary = {"Name": "Michele", "Age": 5, "Nickname": "Skell"}
print("Dictionary:", dictionary)

print()

# Update value by the key
dictionary["Nickname"] = "Shell"

# Access key value with get method
print("Updated nickname:", dictionary.get("Nickname"))

print("Lenth of dictionary:", len(dictionary))

print()

# Add new key/value to end of dictionary
dictionary["Birthday"] = "June"
print("Updated dictionary:", dictionary)

print()

# Iterate through element values by key
print("Key values: ", end=" ")
for d in dictionary:
    print(dictionary[d], end=" ")

print()
print()

# Items returns an array of tuples, each tuple is a key/value pair
# Key/value pairs are not returned in a specific order
print("List dictionary pairs:", dictionary.items())
print("List dictionary keys:", dictionary.keys())
print("List dictionary values:", dictionary.values())
print()

# Delete by key and return the value
print("Delete by key:", dictionary.pop("Age"))

# Delete last item, returns key/value tuple
print("Delete last item:", dictionary.popitem())

# Delete by key
del dictionary["Nickname"]

# Delete the entire dictionary
# Attempting to access will now cause an exception
del dictionary

