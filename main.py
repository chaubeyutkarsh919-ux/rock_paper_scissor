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
    return choices     
choices = get_choices()
print("line 3")
print(choices)