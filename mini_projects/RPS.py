#!/usr/bin/env python3

#Rock, Paper, Scissors

#Game rules: This is rock, paper, scissors... (rock beats scissors, scissors beats paper, paper beats rock[somehow...])

import random

while True:

    your_item = input("Choose your weapon (rock, paper, scissors): ").lower()

    weapon = ["rock", "paper", "scissors"]

#Random weapon for opponent
    opponent = random.choice(weapon)

#Let the match begin
    print(f"\nYou chose {your_item}, opponent chose {opponent}.\n")

    if your_item == opponent:
        print("Stalemate. You both live another day!")
    elif your_item == 'rock':
        if opponent == 'paper':
            print("A piece of paper covered you, for some reason, YOU LOSE!")
        else:
            print("I heard a crunch, YOU WIN!")
    elif your_item == 'paper':
        if opponent == 'scissors':
            print("I heard a slice, YOU LOSE!")
        else:
            print("Paper champion, YOU WIN!")
    elif your_item == 'scissors':
        if opponent == 'rock':
            print("A crushing blow, YOU LOSE!")
        else:
            print("Scissors master, YOU WIN!")


    one_more_round = input("Challenge another opponent? (y/n): ").lower()
    if one_more_round.lower() != "y":
        break
