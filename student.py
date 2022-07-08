#!/usr/local/bin/python3

# This is a helper class for 25-serialize.py
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getInfo(self):
        print("ID: %i\nName: %s" % (self.id, self.name))
