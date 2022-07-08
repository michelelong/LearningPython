# Display program purpose message
print("This program will output a parallelogram.")

# Ask user for the length of each side
sideLength = int(input("How long do you want each side to be?\n"))

# Ask user for the character used to draw the parallelogram
character = input("Please enter the character you want it to be made of:\n")

print("Parallelogram:", end="")
# Loop until input length of side is reached
for x in range(sideLength + 1):
    # For each iteration of the outer loop, print the input character
    for y in range(x):
        print(character, end="")
    print()
# Loop until input length of side is reached again for bottom half of triangle
for i in range(sideLength - 1):
    # Print 1 space & increase by 1 for each iteration of the outer loop
    for k in range(i+1, 0, -1):
        print(" ", end="")
    # Print input characters to equal the side length - 1 & decrease by 1 for each iteration of the outer loop
    for m in range(sideLength - 1, i, -1):
        print(character, end="")
    print()