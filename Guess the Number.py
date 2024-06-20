import random

# using random.. create a game guess the number

"""GUESS THE NUMBER"""
var = random.randint(0,16)
for i in range(3):
    print("Enter a number to guess the correct answer from 0-16.")
    num = int(input())
    if num != var:
        print("Sorry, try again later.")
        print("")
    else:
        print("Kudos... good job!")
        print("")
        print(f"Answer: {var}")
        quit()
print(f"Answer: {var}")