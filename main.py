"""
This is my first project in pythion and git as well.
"""

import random

print("line 1")
def get_choices():
    print("line 2")
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {
        "player": player_choice,
        "computer": computer_choice
    }
    if choices["player"] == choices["computer"]:
        print("It's a tie!")
    elif choices["player"] == "rock":
        if choices["computer"] == "scissors":
            print("You win!")
        else:
            print("Computer wins!")
    elif choices["player"] == "paper":
        if choices["computer"] == "rock":
            print("You win!")
        else:
            print("Computer wins!")
    elif choices["player"] == "scissors":
        if choices["computer"] == "paper":
            print("You win!")
        else:
            print("Computer wins!")
    return choices     
choices = get_choices()
print("line 3")
print(choices)

