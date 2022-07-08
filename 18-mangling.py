#!/usr/bin/python3

# Mangling is a visual warning to developers only! There is no real private or
# protected like there is in languages like Java
# __variable is "private", two underscores in front of variable name
# _variable "protected", one underscore in front of variable name

class Employee():
    def __init__(self, name):
        super().__init__()
        self.__name = name

emp = Employee("Steve")
print(emp._Employee__name)

# Mangled variable is still accessible outside the class despite being "private"
emp._Employee__name = "Travis"
print(emp._Employee__name)
