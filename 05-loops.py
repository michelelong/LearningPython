#!/usr/local/bin/python3

# For loops repeats a specific number of times

# Range start defaults to zero, end of range is excluded
# range(5) is 0-4

for x in range(5):
    if x == 4: print(x) # avoids printing trailing comma
    else: print(x, end=", ")

print()

# Range start and end can both be specified
for x in range(1, 6):
    if x == 5: print(x)
    else: print(x, end=", ")

print()

# Range start, end, and increment specified
for x in range(0, 11, 2):
    if x == 10: print(x)
    else: print(x, end=", ")


# Nested loops, inner loop runs x times per each outer loop
for x in range(5):
    print()
    for y in range(x):
        print("*", end="")

print()
print()
# While repeats any number of times until the test condition fails
choice = "y"
x = 1
while choice == "y":
    print(x * 2)
    x = x + 1
    choice = input('Continue? (y/n)')

print()

# While loops can have an else that always runs when the test fails
q = 1
while q < 5:
    print("This iteration %d." % (q))
    q += 1
else:
    # retains last value in loop
    print("Else statement: ", q)

print()

# For loops can also have an else but if false it jumps to an outside variable
greet = True
for x in range(1, 6, 2):
    print("Howdy")
else:
    print("Hello")

print()

choices = ['Pizza', 'Pasta', 'Salad', 'Nachos']
# Enumerate supplies an index to each element in the list and increments
print('Your menu choices are:')
for index, item in enumerate(choices):
    # Add to the printed index so it starts at 1 instead of 0
    print("%i) %s" % (index + 1, item))

print()

list_a = [3, 4, 17, 15, 19]
list_b = [2, 9, 8, 10, 30, 40, 50, 60, 70, 80, 90]

# Zip creates pairs of elements when passed lists and stops at the end of the shortest list
for a, b in zip(list_a, list_b):
    # Compare elements of the two lists and print the larger number
    if a > b:
        print("List A: ", end="")
        print(a)
    else:
        print("List B: ", end="")
        print(b)

print()

times = 0
while True:
    times += 1
    if times == 3:
        # Skips a loop iteration
        continue
    elif times == 6:
        # Exits the loop
        break
    else:
        print(times, end=" ")

print()
