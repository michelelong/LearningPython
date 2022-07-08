#!/usr/local/bin/python3

# Generators are functions that return a sequence of values
def custGen(x, y):
    while x < y:
        # yield will take each value of x and return a complete range
        yield x
        x += 1

result = custGen(1, 10)

for i in result:
    print(i)
