#!/usr/bin/env python3
"""TLG NDE Cohort April 2022 | Trivia Game from Data File"""

from trivia import trivia
import random
import html

# GOALS
# using a for loop, return each question one at a time
# print out the question
# use a for loop to print out the "answers"
# prompt the user to make a choice

counter= 1

for x in trivia["results"]:
    print(f"{counter}. {x['question']}")
    counter += 1
    
    all_answers= x["incorrect_answers"]
    
    all_answers.append(x['correct_answer'])
    
    random.shuffle(all_answers)

    letters= ["A.","B.","C.","D."]

    bank= {}

    for letter,answers in zip(letters,all_answers):
        print(letter, answers)
        bank.update({letter:answers})


    print(bank)
    answer = input("\nPlease type out your answer >>> ")

    #if answer == x['correct_answer'] & not in x['incorrect_answers']:
    if answer == x['correct_answers']:
        print("Correct!")
    else:
        print("Wrong!")

    print()
