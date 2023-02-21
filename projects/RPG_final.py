#!/usr/bin/python3

#DBZ game play
#FINAL PROJECT
# Created by Dalton M. and J H.
#TO-DO
# Create a map as you move through the map
# Expand map
# 

# =================================== IMPORTS ================================================================
from random import randint
import random
import dice
import sys # Used for system.exit()
import os # Used for os.system("clear")
from dbz_questions import dbz_questions

# get the width ("columns") of the screen
size = os.get_terminal_size()
# convert object to list
sizelist= list(size)
# element 0 is the width in columns; multiply times whatever
# character (=,*,&,etc.) to fill the width of the screen!

def rolldice(min,max):
    print("Rolling dice...")
    global rollnum
    rollnum= random.randint(min,max)

def showInstructions():
    #print a main menu and the commands
    print('''
______                            ______       _ _  ______
|  _  \                           | ___ \     | | ||___  /
| | | |_ __ __ _  __ _  ___  _ __ | |_/ / __ _| | |   / / 
| | | | '__/ _` |/ _` |/ _ \| '_ \| ___ \/ _` | | |  / /  
| |/ /| | | (_| | (_| | (_) | | | | |_/ / (_| | | |./ /___
|___/ |_|  \__,_|\__, |\___/|_| |_\____/ \__,_|_|_|\_____/
                  __/ |                                   
                 |___/                                    
''')
    print("=" * sizelist[0])
    print('''
OBJECTIVE:
    Collect the Dragon Balls &    
    defeat Majin Buu before you   
    make your wish at the lookout!
''')
    print("=" * sizelist[0])
    print('''
Commands:                     
  go [ex:north]               
  get [item]                  
  use [item]                  
  teleport                    
  look "find ways to go"                      
  help "show instructions"                       
  quit                        
''')

# ==================================== Status show after each command ==========================================

def showStatus():
    #print the player's current status
    print("=" * sizelist[0])
    print(rooms[currentRoom]['desc'],'\n')
    #print the current inventory
    print('Inventory : ' + str(inventory),'\n')
    #Print current health
    print('your current health is', health,'\n')
    #print an item or object if there is one
    if "ball" in rooms[currentRoom]:
        print('You see the ' + rooms[currentRoom]['ball'],'\n')
    if "ball2" in rooms[currentRoom]:
        print('You see the ' + rooms[currentRoom]['ball2'],'\n')
    if "ball4" in rooms[currentRoom]:
        print('You see the ' + rooms[currentRoom]['ball4'],'\n') 
    if "buu" in rooms[currentRoom]:
        print('You see Majin Buu ready to battle!!!\n')
    if 'bean' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['bean'],'\n')
    if 'zsword' in rooms[currentRoom]:
        print('You spend some time here training with the Kai\'s, get the Zsword, this might come in handy later...\nHint: use \'get\'')
    print("=" * sizelist[0])

#starting inventory
inventory = ['Dragon radar']

#buu stats
villain = [{'name' : 'buu', 'health' : 50, 'damage' : '1d12'}]

#armory
armory = {'sword' : 
            {'damage' : '2d15'},
          'fist' :
            {'damage' : '1d6'}
            }

#staring health
health = 50

def combat():
    
    #import vars from above outside the DEF
    global health, inventory, armory, villain, currentRoom
    round = 1
    buu_health = villain[0]['health'] 

    print('Welcome to the tournament grounds! A place where only the best come to fight.')
    print('Majin Buu appears in the ring! COMBAT STARTS NOW! (in two episodes...)\n')
    
    while True:
        print('Player Health: [' + str(health) + ']')
        print('Majin Buu\'s Health: [' + str(buu_health) + ']')

        print("Type: RUN, or USE [weapon]")
        move = input('> ').lower().split() # converts move into a lower-case list to deal with each item in list separately
        buu_damage = sum(dice.roll(villain[0]['damage']))
        print("\n============================================")

        if move[0] == 'use':
            if move[1] == 'fist':
                player_damage = sum(dice.roll(armory[move[1]]['damage']))
                print(f"You punched Majin Buu for {player_damage} damage!")
            if move[1] in inventory: # checks if weapon is in your inventory
                player_damage = sum(dice.roll(armory[move[1]]['damage']))
                print(f'You sliced Majin Buu for {player_damage} damage!')
                if move[1] not in inventory:
                    print(f'There is no {move[1]} in your inventory!')

        if move[0] == 'run':
            escape_chance = randint(1,10)

            if escape_chance >= 8: #roll an 8-10 and escape
                print("You escape without him noticing!")
                break
            if escape_chance >= 5: #roll a 5-8 and escape but damaged
                print("You expose your back as you turn and fly away and Buu takes advantage.")
                print(f"Buu hits you for {buu_damage} damage!")
                health -= int(buu_damage)
                if health >= 1:
                    print('You managed to escape.')
                    break
                if health < 1:
                    print('You have been destroyed.')
                    print('\nGAME OVER')
                    sys.exit()
            if escape_chance >= 0:
                print('Majin Buu out-maneuvers you and blast\'s you! You can not escape.')

        try:
            buu_health -= int(player_damage)
        except:
            pass
        if buu_health <= 0:
            print(f'Majin buu lies dead. You are victorious!\n')
            print('It looks like Buu had a Dragon Ball hiding inside him but it rolled out..')
            rooms['Tourney grounds']['ball'] = '5 starball'
            rooms['Kame house']['bean'] = 'senzu bean'
            del rooms['Tourney grounds']['buu']
            break

        print(f'Buu hits you for {buu_damage} damage!')
        print ('=============================================\n')
        round += 1
        health -= int(buu_damage)

        if health <= 0:
            print("You have been vanquished! You are dead.")
            sys.exit()

def encounter():
    if rooms[currentRoom]['buu']:
        combat()


# ======================== DICTIONARIES / LISTS =======================================================
# a dictionary linking a room to other rooms, also shows available items and objects
rooms = {

            'Kame house' : {
                  'north' : 'North city',
                  'south' : 'South city',
                  'east'  : 'East city',
                  'west'  : 'West city',
                  'dir'   : 'From here you can go north, east, south and west.',
                  'desc'  : "Kame House is a house on a very small island in the middle of the sea.\nIt is the home of Master Roshi, and there he is looking at a naughty magazine in his beach chair...",
                },
            'North city': {
                  'north' : 'The lookout',
                  'south' : 'Kame house',
                  'ball'  : '1 starball',
                  'dir'   : 'From here you can go north and south.',
                  'desc'  : "North City, also known as Metro North, is one of the large metropolis capitals of Earth.\nIt is surrounded by mountains and a forest.\nDr. Gero's Laboratory is in the mountains south of the city.",
                },
            'The lookout': {
                  'south' : 'North city',
                  'ball'  : '3 starball',
                  'dir'   : 'From here you can go south.',
                  'desc'  : "The Lookout is an ancient platform that is in geostationary orbit in the skies of Earth,\nand directly above Korin Tower",
               },
            'East city' : {
                  'north' : 'Tourney grounds',
                  'west'  : 'Kame house',
                  'ball'  : '7 starball',
                  'dir'   : 'From here you can go north and west.',
                  'desc'  : 'Welcome to East City, there\'s not much here...', 
               },
            'Tourney grounds' : {
                  'south' : 'East city',
                  'buu'   : 'Kid buu',
                  'dir'   : 'From here you can go south.',
                  'desc'  : "The World Martial Arts Tournament originated in a festival held since long ago at the temple which now serves as the tournament grounds",
               },
            'South city' : {
                  'south' : 'Satan city',
                  'north' : 'Kame house',
                  'ball4' : '4 starball',
                  'dir'   : 'From here you can go north and south.',
                  'desc'  : 'Welcome to South city a great place to pass through. So keep heading south to move on...',
               },
            'Satan city' : {
                  'north' : 'South city',
                  'ball'  : '6 starball',
                  'dir'   : 'From here you can go north.',
                  'desc'  : 'Welcome to Satan city, if you look around you might see Hercule acting the fool.\nUnfortunatly, the only place to go is back the way you came.',
               },
            'West city' : {
                  'east'  : 'Kame house',
                  'south' : 'Forest',
                  'ball2' : '2 starball',
                  'dir'   : 'From here you can go east and south.',
                  'desc'  : 'West city is mostly known as the hometown of Bulma and the headquarters of Capsule Corporation.\nDue to its apparent wealth, the city quickly recovers from most incidents, such as being a target of Majin Buu.',
               },
            'Forest' : {
                  'north' : 'West city',
                  'zsword': 'zsword',
                  'dir'   : 'From here you can go north.',
                  'desc'  : 'You stumble into a random forest and see something shimmering as it extends from the top of a rock...'
            }
         }
tele_rooms = ['Kame house', 'North city', 'West city', 'South city', 'East city', 'Satan city', 'Forest', 'Tourney grounds', 'The lookout',]

#start at Kame's house
currentRoom = 'Kame house'

os.system('clear') #after each move/use/get/look/help then wipe the screen

showInstructions()

#ball count goes up as you collect dragon balls (7 needed to win)
ball_count = 0
grade = 0

#========================================= Game Loop ============================================

while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #so typing 'go north' would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    move = move.lower().split(" ", 1)
    os.system('clear') # clear the screen each move
    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #trying to make buu attack
            if 'buu' in rooms[currentRoom]:
                encounter()
            #there is no way to the new rooms then...
        else:
            print('You can\'t go that way!')

    #if they type teleport or tele first
    if move[0] == 'teleport' and 'sword' in inventory:
        print('Available rooms:')
        for room_names in tele_rooms:
            print('>', room_names)
        room_teleport = input('\nWhere do you want to teleport? ')
        if room_teleport in rooms.keys():
            currentRoom = room_teleport
        else:
            print('You need the Zsword to be able to teleport')

    #if they type 'get' first
    if move[0] == 'get':
        
        #if the room contains an item, and the item is the one they want to get
        if "ball" in rooms[currentRoom] and move[1] in rooms[currentRoom]['ball']:
            #add the item to their inventory
            inventory += [move[1]]
            ball_count += 1
            #display a message of success
            print(move[1] + ' grabbed!')
            print('you currently have', ball_count,'Dragon Balls')
            #delete the item from tie room
            del rooms[currentRoom]['ball']
        
        elif 'ball2' in rooms[currentRoom] and move[1] in rooms[currentRoom]["ball2"]:
            print('''You see a showman offering a Dragon Ball for anyone who can score 80% or above on a Dragon Ball quiz!''')
            #do they want to play?
            gamestart = input('Will you accept the challenge? (y/n): ')
            # make the case lower for ease
            
            if gamestart.lower() == 'n':
                continue
            else:
                #start counter for the numbering of the questions
                counter= 1

                for x in dbz_questions["results"]: #reference the document with questions
                    print(f"{counter}. {x['question']}") #prints a 1. then the question
                    counter += 1 #increase counter for each new question
                    all_answers= x["incorrect_answers"] #start a var to collect all possible answers
                    all_answers.append(x['correct_answer'])
                    random.shuffle(all_answers) #shuffle the var all answers
                    letters= ["A. ","B. ","C. ","D. "] #put letters in from of answers
                    block= {} #initialize empty var
                    for letter,answer in zip(letters,all_answers):
                        print(letter, answer)
                        block.update({letter:answer})
                   #print(block)
                    answer= input("\n>")
                    if answer == x['correct_answer'] or answer == x['correct_answer'].lower():
                        grade +=1 #this var adds to correct answers to win 4/5
                        print("Correct!")
                        print()
                    else:
                        print("That is not correct. Keep trying!")
    
                if grade >= 4: #how they win the game need 4/5 questions right
                    inventory += [move[1]] #add ball to inventory
                    ball_count += 1 #increase ball count for end game win
                    print('You got', [grade], "question(s) correct so you win this Dragon Ball! You\'re so smart!\n")
                    print(move[1] + ' grabbed!')
                    #print('you currently have', ball_count,'Dragon ball')
                    del rooms[currentRoom]['ball2']
                    continue 
                else:
                    print('That was not enough correct answers to get the ball. Use \'get\' to try again...')
        
        elif "ball4" in rooms[currentRoom] and move[1] in rooms[currentRoom]["ball4"]:
            print('''Seems like a fine day in South City! You are searching around for the Dragon Balls when you see a shady man playing a dice game in the street. You walk up to him and see he has the 4 star Dragon Ball! He claims that he will only give you the Dragon Ball if you can guess the number of the die he is rolling!''')
            gamestart = input("Would you care to play a game? (y/n): ")
            if gamestart.lower() == "n":
                continue
            elif gamestart.lower() == "y":
                rolldice(1,6)
                print(rollnum)
                dieguess = int(input("Guess a number between 1 and 6! "))
                if dieguess == rollnum:
                    print("Hey! You managed to guess right and the shady man gives you the 4 star Dragon Ball")
                    inventory += [move[1]]
                    del rooms[currentRoom]["ball4"]
                    ball_count += 1
                    print(ball_count)
                    continue
                elif dieguess != rolldice:
                    choice = input('Do you want to try again? (y/n): ')
                    if choice.lower() == 'n':
                        continue

        elif "zsword" in rooms[currentRoom] and move[1] in rooms[currentRoom]['zsword']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' picked up!')
            #delete the item from the room
            del rooms[currentRoom]['zsword']  
        
        elif 'bean' in rooms[currentRoom] and move[1] in rooms[currentRoom]['bean']:
            #add bean to inventory
            inventory += [move[1]]
            #delete the bean from dict
            del rooms[currentRoom]['bean']
            #display helpful message to mayb use it...
            print('A Senzu bean is now in your hand, it might be good to use one now')
        #otherwise, if the item isn't there to get
        
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
 
    if move[0] == 'use':
        #check that they are allowed use this item
        if move[1] == 'bean':
            health = 100
            #remove bean from inventory
            inventory.remove('bean')
            print('You have recovered and your health is back to', health, 'Let\'s get to the lookout quickly...')
    
    #used to see which way you can travel
    if move[0] == 'look':
        if 'dir' in rooms[currentRoom]:
            #print the room description
            print("=" * sizelist[0])
            print(rooms[currentRoom]['dir'])
        else:
            print('You don\'t see anything.')
    
    #This is where a player can ask for the instructions again
    if move[0] == 'help':
        showInstructions()
    
    #This is where a player can quit
    if move[0] == 'q' or move[0] == 'quit':
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() == 'y' or quit_query.lower() == 'yes':
            print("Thanks for playing!")
            sys.exit()
        if quit_query.lower() == 'n' or quit_query.lower() == 'no':
            continue

     ## Define how a player can win
    if currentRoom == 'The lookout' and ball_count == 7 and 'buu' not in rooms['Tourney grounds']:
        wish = input('***You summon Shenron***\nShenron roars! "TELL ME YOUR WISH"... ') #type your wish here
        print("That is out of my power, but I can can give these project makers passing score!")
        break
    
    if currentRoom == 'The lookout' and ball_count == 7 and 'buu' in rooms['Tourney grounds']:
        print("You must defeat Majin Buu before making your wish!")
  

