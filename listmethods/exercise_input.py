#!usr/bin/env python3

icecream= ["indentation", "spaces"]

tlgstudents= ["Akino", "Bai", "Carlos", "Dalton", "Dan", "Edith", "Ethan", "Isaiah", "J", "Jessica", "John", "Justin", "Khalil", "Nikk", "Ramesh", "Scotty", "Sergio", "Shawn"]

icecream.append(4)

number = int(input("Provide a student number between 0 and 17: "))

student = tlgstudents[number]

print(student, "always uses", icecream[2], icecream[1], "to indent.")

import secrets

student = tlgstudents

print(secrets.choice(student), "does it better though.")



"""
# the choice() function from the random module
# will choose a random element from a list
from random import choice

icecream= ["indentation", "spaces"]

tlgstudents= ["Akino", "Bai", "Carlos", "Dalton", "Dan", "Edith", "Ethan", "Isaiah", "J", "Jessica", "John", "Justin", "Khalil", "Nikk", "Ramesh", "Scotty", "Sergio", "Shawn"]

# this will add the integer 4 to the icecream list
icecream.append(4)
"""
# using """three quotes""" creates a multi-line doc string
# in other words, a string that uses line breaks instead of /n
#print("""Do one of the following:
#        - Enter a number between 0 and 17
#        - Type in a student's name
#        - Type in the word 'random'""")

# save the user's input as the variable "choice"
"""
choice= input(">")

# if the number entered by the user can be
# cleanly converted to an integer:
if choice.isdigit():
    # convert string to integer and slice the list
    # save the returned name as "name"
    name= tlgstudents[int(choice)]

# if the name chosen is actually in the list of students:
elif choice in tlgstudents:
    # assign that name as the variable "name"
    name= choice

else:
    # if none of the above is true, use the choice()
    # function to grab a random name and save it as "name"
    name= random.choice(tlgstudents)

# Use an f-string to neatly combine these elements into a sentence.
print(f"{name} always uses {icecream[2]} {icecream[1]} to indent.")
"""
