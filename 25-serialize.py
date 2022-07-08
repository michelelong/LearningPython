#!/usr/local/bin/python3
import pickle, student

# Open file for binary write
with open("student.dat", "wb") as f:
    # Create Student object and dump to binary file
    s = student.Student(123, "Michele")
    pickle.dump(s, f)

# Open file for binary readonly
with open("student.dat", "rb") as f:
    # Load object and access stored class instance
    obj = pickle.load(f)
    obj.getInfo()
