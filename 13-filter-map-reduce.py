#!/usr/local/bin/python3
from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Complete list:", lst)

print()

# Filter return object needs to be cast back to list
# Return a list of elements that are true
even_lst = list(filter(lambda e: e % 2 == 0, lst))
print("Filter list:", even_lst)

print()

# Map return object needs to be cast back to list
# Performs a function on every element in list
map_lst = list(map(lambda n: n * 2, lst))
print("Map list:", map_lst)

print()

# Reduce accumulates the elements in a list into a single value
reduce_lst = reduce(lambda x, y: x + y, lst)
print("Reduce total: ", reduce_lst)

print()

total = 0
for i in lst:
    total += i

print("Iteration total: ", total)
