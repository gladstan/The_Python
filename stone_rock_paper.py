import random

# user_Pickup
user_picks = str(input("Enter the Rock/Stone/Paper/Scissors ")).lower()
if user_picks == int:
    print("Enter a string")

# Computer_Picks
rand2 = random.randint(0, 3)
val = ["stone", "rock", "scissors", "paper"]
combined = val[rand2]
if combined != user_picks:
    print(combined)
else:
    if combined == user_picks:
        print("Draw")




# elif user_picks["rock"] == combined["rock"]:
#     print("Draw")
# elif user_picks["paper"] == combined["paper"]:
#     print("Draw")
# elif user_picks["scissors"] == combined["scissors"]:
#     print("Draw")


















