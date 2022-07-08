#!/usr/local/bin/python3
from os import path
from sys import exit

# You can open files in the following modes:
# write-only ("w"), contents will be overwritten
# write and read ("w+")
# read-only ("r"), contents can not be changed
# read, write, and append ("r+")
# append ("a"), add new data to end of file
# append and read ("a+")
# exclusive ("X"), create a new file, throws error if exists
# binary ("b"), add "b" to w, r, a, and x ("wb", "r+b", and so on)

# Open file in write only mode
# Buffer size is an optional third parameter, default is 4096 or 8092
f = open("output.txt", "w")
nums = [i for i in range(1, 10)] # 1-9

# Iterate through list and write each value to file
for item in nums:
    # Write does not automatically add a new line
    f.write(str(item) + " ")

f.write("\n") # Start a new line

# Write a list
f.writelines(["This is", " a list", " written to the same file.\n"])

# Close the opened file to flush the data buffer
f.close()

# Check if file exists before opening
if path.isfile("output.txt"):
    # Open file in read only mode
    my_file = open("output.txt", "r")
    for l in my_file: # Print each line in the file
        print(l)
else:
    exit("Unable to open file.")

# Files have a boolean closed attribute
# If the file isn't closed, then close it
if not my_file.closed:
    my_file.close()
    print("File is now closed!\n")

# The "with open" method closes the automatically when done
# Iterate through file and print each line
with open("output.txt", "r") as my_file:
    for line in my_file:
        print(line)

# The "with as" method can also be used to open and close database connections
# with sql.connect("database.db") as con:
#     name = "foobar"
#     cur = con.cursor()
#     cur.execute("INSERT INTO students (name) VALUES (?)", (name))
#     con.commit()
#     msg = "Done"

# while loop needs readline to iterate to the next line
with open("numbers.txt", "r") as test:
    total = 0
    line = test.readline()
    while line != '':
        print(line.rstrip(), end=" ")
        line = test.readline()
    test.close()

print()

# Open the numbers.txt file, add the number on each line to the total
with open("numbers.txt", "r") as test:
    total = 0
    for line in test:
        total += int(line) # convert text from file to integer
    print("The total is", total)
