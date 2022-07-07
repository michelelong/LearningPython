#!/usr/local/bin/python3

# Get data from standard input
name = input("What is your name? ")
print("Hello, " + name)

# Input data is a string by default
# If input numbers are to be calculated, they need to be cast
num1 = int(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = num1 + num2
print(num3)

# Multiple inputs can be split into a list
lst1 = input("Enter your full name: ").split()
print(lst1)

# Split multiple inputs into separate strings
a, b, c = input("Enter your full name: ").split()
print("\nFirstname: %s\nMiddlename: %s\nLastname: %s" % (a, b, c))

# Split and cast multiple inputs into a list
lst2 = [int(x) for x in input("Enter three space separated numbers: ").split()]
print(lst2)

