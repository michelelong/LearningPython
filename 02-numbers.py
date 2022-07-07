#!/usr/local/bin/python3
from math import sqrt

age = 45
print(type(age))

decimal = 5.4
print(type(decimal))

# Represent equations or expressions
algebra = 3 + 5j
print(type(algebra))

binary = 0B1010
print("Binary 0B1010 = %s" % (binary))

hexadecimal = 0Xff
print("Hexadecimal = %s" % (hexadecimal))

octal = 0O1010
print("Octal = %s" % (octal))

# Adding an integer and a float results in a float
print(age + decimal)

# Cast float to integer
print(age + int(decimal))

# Subtraction
print(age - 5)

# Multiplication
print(age * 3)

# Division
print(age / 2)

# Integer (Floor) Division
print(7 // 2)

# Float Division, if either number is a float the answer will be a float
print(age / 2.5)

# Modulo (Remainder after division)
print(age % 2)

# Square root method imported from the math module
print(sqrt(5))

# Insert comma separators for floating point and limit to 2 decimal places
print("${0:,.2f}".format(13459.87))  #0: is a positional argument
# followed by conversion to comma separated two decimals places

# Insert comma separators for integer
print(format(123456, ',d'))

# % multiplies decimal by 100 and displays with a % sign
print(format(0.5, '.0%'))
