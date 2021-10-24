import random

rock = "rock"
paper = "paper"
scissors = "scissors"
player_choice = input("Welcome to the game of Rock, Paper, Scissors!"
                      " Which will you choose? Rock, paper, or Scissors?\n").lower()
computer_choices = [rock, paper, scissors]
computer_random = random.choice(computer_choices)

if player_choice == "rock" and computer_random == paper:
    print(f"{rock} beats {scissors}!")
    if player_choice == "rock" and computer_random == scissors:
        print(f"{rock} beats {scissors}! ")
    if player_choice == 'rock' and computer_random == rock:
        print(f"{rock} beats {scissors}! ")

print(player_choice)

