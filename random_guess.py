#Guess the number Game in python
import random
guesses=0
# Random number
while True:
    guesses+=1
    user = int(input("Make a Guess "))
    if user == 0:
        print("Enter a number above zero")

    rand = random.randint(1, user)
    if user == rand:
        print("You are guess is correct")
        break
    else:
        print("The number doesn't match")

print("You have made", guesses, "guesses")
print("hello")