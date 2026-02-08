import random

choices = ["rock", "paper", "scissors"]

def Play_round(user_input):
    computer_pick = random.choice(choices)

    if user_input == computer_pick:
        return computer_pick, "draw"

    elif (
        (user_input == "rock" and computer_pick == "scissors") or
        (user_input == "paper" and computer_pick == "rock") or
        (user_input == "scissors" and computer_pick == "paper")
    ):
        return computer_pick, "win"

    else:
        return computer_pick, "lose"