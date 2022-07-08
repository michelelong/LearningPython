#!/usr/local/bin/python3
import logging

# Default logging level is warning and above to console only
logging.basicConfig(filename="error.log", level=logging.DEBUG)

# In order of severity
# logging.critical("Very bad")
# logging.error("Bad")
# logging.warning("Not so bad")
# logging.info("Just thought you should know")
# logging.debug("What is going on")

def div(x, y):
    result = 0
    try:
        f = open("output.txt", "a")
        logging.info("Attempting division")
        result = x / y
        f.write("%i / %i = %i\n" % (x, y, result))
    # If no exception type is specified, all exception types will be caught
    # Multiple except blocks can catch multiple types
    except ZeroDivisionError as obj:
        print("Are you try to crash my program?")
        logging.error(obj)
    else:
        print("Else block only executes if no exception was thrown.")
    # Finally always executes, whether an exception was thrown or not
    finally:
        f.close()


div(4, 0)

userInput = int(input("Enter a number greater than 10: "))
# If false the assertion throws an exception, displays the message, and exits
# Assertions can be used in try/except blocks
assert userInput > 10, "You didn't follow directions."


def map(func, values):
    output_values = []
    index = 0
    while index < len(values):
        # Sets a breakpoint and drops into debugger command prompt
        print("\nh for help, exit to leave the debugger\n")
        breakpoint()
        # or run code directly in debugger with: python3 -m pdb errors.py
        output_values = func(values[index])
        index += 1
    return output_values


def add_one(val):
    return val + 1


map(add_one, list(range(5)))
