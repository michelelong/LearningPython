#!/usr/local/bin/python3
# Functions are defined by:
# 1) The header includes the def keyword, name of the function, and parameters
# 2) An optional docstring that explains what the function does
# 3) The body of statements the function carries out

# Function names start with a lowercase letter or underscore


def tax(bill):  # Header
    """Adds 8% tax to a restaurant bill."""  # docstring
    bill *= 1.08  # start of body
    print("Bill with tax: $%.2f" % bill)
    return bill # end of body


def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print("Bill with tip: $%.2f" % bill)
    return bill


meal_cost = 100

# Call the functions with arguments
# A function can be an argument to another function
tip(tax(meal_cost)) # Calculate tax first then tip on returned total
print()


# Accessing a global variable with the same name as a local variable
def globalScope():
    meal_cost = 200
    print("Local variable: ", meal_cost)
    print("Global variable: ", globals()['meal_cost']) # Bad idea, but there you go
    return meal_cost


globalScope()

print()

# Assign function to a variable
testScope = globalScope
# Call the variable
testScope()
print()


# Multiple values can be retured as a tuple
# Function parameters with a default value
def calc(a, b=2):
    x = a + b
    y = a * b
    z = a - b
    return x, y, z


print("Call with two arguments: ", calc(6, 3))
print("Use default value for second argument: ", calc(6))


# A recursive function calls itself until test case is true
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print("Factorial: %d" % (factorial(5)))

print()


# Function inside of a function
def display(name):
    # Inner function can not be called from outside the function
    def message():
        return "Hello, "

    result = message() + name + "." # call of inner function
    return result

print(display("Michele")) # call outer function with argument

print()

# A lambda is an anonymous function
# Lamda format: lambdaKeyword arguments : expression
# Iterate 0-16, if divisible by 3 then add to list
my_list = range(16)
print("Lambda function: ", end="")
print(list(filter(lambda x: x % 3 == 0, my_list)))

# Above lamba is the same as the function:
# def by_three(x):
#    return x % 3 == 0

print()

# Functions can have a variable number of positional arguments and keyword arguments
def multiples(*args, **kwargs):
    print(f"{args} {kwargs}")

print("2 positional and two keyword args: ", end="")
multiples(1, 2, a=5, b=6)
print()
print("Same function with 1 positional and 1 keyword arg: ", end="")
multiples(10, a=16)
