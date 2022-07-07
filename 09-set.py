#!/usr/local/bin/python3

# Set does not allow duplicate elements, order is not guaranteed
# Set elements do not have indices, slicing, or repetition
uniqueSet = {10, 20, 30, 40, 50}
print("Returns in random order:", uniqueSet)

print()

# Add multiple elements to a set
uniqueSet.update([60, 70, 10, 20])
print("Add new elements:", uniqueSet)

# Add one new element to set
uniqueSet.add(80)

# Remove element by value
uniqueSet.remove(10)

# Remove element with no exception if element not found
uniqueSet.discard(10)

print()

# Freezing a set makes it immutable
freeze = frozenset([10, 20, 30, 40, 50])

print("Frozen set elements: ", end="")
for x in freeze:
    print(x, end=" ")
print()

if 20 in freeze:
    print("Found it in the set!")
if 80 not in freeze:
    print("Not found in the set!")

print()

setGood = {"Sam", "Dean", "Crowley"}
setBad = {"Abaddon", "Asmodeus", "Crowley"}

# Union contains all elements of two sets
setAll = setGood.union(setBad)
print("Combined sets:", setAll)
# or setAll = setGood | setBad instead of .union

# Intersection contains ONLY elements found in both sets
setInter = setGood.intersection(setBad)
print("Intersection:", setInter)
# or setInter = setGood & setBad instead of .intersection

# Difference contains elements ONLY in set one BUT NOT set two
setDiff = setGood.difference(setBad)
print("Difference:", setDiff)
# or setDiff = setGood - setBad instead of .difference

setDiff2 = setBad.difference(setGood)
print("Difference in other direction:", setDiff2)

# Symmetric Difference contains elements found in set 1 OR set 2, but NOT BOTH
setSym = setGood.symmetric_difference(setBad)
print("Symmetric Difference:", setSym)
# or setSym = setGood ^ setBad

print()

set1 = set([1, 2, 3, 4, 5])
set2 = set([2, 5])

print("Set1: ", set1)
print("Set2: ", set2)

# Subset - All elements of the smaller set are in the larger set
print("Set2 is a subset of set1: ", set2.issubset(set1))
print("Set1 is a subset of set2: ", set1.issubset(set2))

print()

# Superset - Larger set has all elements from the smaller set
print("Set1 is a superset of set2: ", set1.issuperset(set2))
print("Set2 is a superset of set1: ", set2.issuperset(set1))
