#!/usr/local/bin/python3

# if, elif, and else
answer = input("Enter left or right: ").lower()
if answer == "left" or answer == "l":
    print("This is the Verbal Abuse Room, you heap of parrot droppings!")
elif answer == "right" or answer == "r":
    print("Of course this is the Argument Room, I've told you that already!")
else:
    print("You didn't pick left or right!")

ending = "ay"
print("\nPig Latin Translator")

userInput = input("Enter a word: ")
word = userInput.lower()
# Check string length and for non-letter characters
if len(word) > 0 and word.isalpha:
    print("%s%s%s" % (word[1:], word[0], ending))
else:
    print("Not a valid word.")

choice = int(input("Enter number 1: "))
if choice is 1:
    print("You chose 1.")
elif choice is not 1:
    print("You did not chose 1.")
