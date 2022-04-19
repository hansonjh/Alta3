#!/usr/bin/env python3

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

q1_answer = input("How would you describe yourself? \na) brave \nb) studious \nc) loyal \nd) ambitious\n")
if q1_answer == "a":
  gryffindor += 1
elif q1_answer == "b":
  ravenclaw += 1
elif q1_answer == "c":
  hufflepuff += 1
elif q1_answer == "d":
  slytherin += 1
else:
  print("Sorry, I don't understand that answer.")
  
q2_answer = input("What can you be found doing on the weekends? \na) Going on adventures \nb) Doing my homework \nc) Spending time with family or friends \nd) Plotting revenge on my enemies\n")
if q2_answer == 'a':
  gryffindor += 1
elif q2_answer == 'b':
  ravenclaw += 1
elif q2_answer == 'c':
  hufflepuff +=1
elif q2_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")

q3_answer = input("What would you do if the Dark Lord was going to invade your school? \na) Fight him \nb) Look up some good defensive curses in a book \nc) Stand by my friends no matter what \nd) Help the Dark Lord invade the school as an inside spy\n")
if q3_answer == 'a':
  gryffindor += 1
elif q3_answer == 'b':
  ravenclaw += 1
elif q3_answer == 'c':
  hufflepuff +=1
elif q3_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")

q4_answer = input("If you could make a potion that would guarantee one thing, what would it be? \na) Glory \nb) Wisdom \nc) Love \nd) Power\n")
if q4_answer == 'a':
  gryffindor += 1
elif q4_answer == 'b':
  ravenclaw += 1
elif q4_answer == 'c':
  hufflepuff +=1
elif q4_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")

q5_answer = input("What would you rather be? \na) Trusted \nb) Praised \nc) Loved \nd) Feared\n")
if q5_answer == 'a':
  gryffindor += 1
elif q5_answer == 'b':
  ravenclaw += 1
elif q5_answer == 'c':
  hufflepuff +=1
elif q5_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")

q6_answer = input("If you could have a superpower, which would you choose? \na) Superstrength \nb) Read Minds \nc) Talk to Animals \nd) Change Appearance\n")
if q6_answer == 'a':
  gryffindor += 1
elif q6_answer == 'b':
  ravenclaw += 1
elif q6_answer == 'c':
  hufflepuff +=1
elif q6_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")

q7_answer = input("Which subject at Hogwarts would you be most interested in studying? \na) Broom Flying \nb) Secrets about the Castle \nc) Care of Magical Creatures \nd) Hexes/Jinks\n")
if q7_answer == 'a':
  gryffindor += 1
elif q7_answer == 'b':
  ravenclaw += 1
elif q7_answer == 'c':
  hufflepuff +=1
elif q7_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")

q8_answer = input("During the end-of-year exams, you notice that one of your classmates was using an enchanted quill. You come top of the class anyway, but they are second. What do you do? \na) Tell the professor immediately \nb) Nothing, but if I hadn't come top of the class, I'd definitely tell the professor \nc) Encourage the other student to admit what they'd done to the professor \nd) Give them a high five\n")
if q8_answer == 'a':
  gryffindor += 1
elif q8_answer == 'b':
  ravenclaw += 1
elif q8_answer == 'c':
  hufflepuff +=1
elif q8_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")

q9_answer = input("You would be most hurt if a person called you... \na) Unkind \nb) Ignorant \nc) Boring \nd) Weak\n")
if q9_answer == 'a':
  gryffindor += 1
elif q9_answer == 'b':
  ravenclaw += 1
elif q9_answer == 'c':
  hufflepuff +=1
elif q9_answer == 'd':
  slytherin +=1
else:
  print("Sorry, I don't understand that response.")
  
if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("GRYFFINDOR!!!!!!")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("RAVENCLAW!!!!!!")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("HUFFLEPUFF!!!!!!")
elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff:
    print("SLYTHERIN!!!!!!")
else:
    print("Too difficult to decide... Maybe you don't belong at Hogwarts after all.")
houses = []
if gryffindor > 0:
    houses.append("Gryffindor")
if ravenclaw > 0:
    houses.append("Ravenclaw")
if hufflepuff > 0:
    houses.append("Hufflepuff")
if slytherin > 0:
    houses.append("Slytherin")
    print("You could have been in...")
    for house in houses:
      print(house)
