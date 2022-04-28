#!/usr/bin/python3

#DBZ game play
#FINAL PROJECT
# Created by Dalton M. and J H.

'''
*** TO DO ***
> Add help option to show instructions (222 - 223)
> Add description of each room (line 216 - 220)
> Add fancy banners?...
> move action print to status
> health system (199 - 202)
> attack system
> make getting DB a bit trickier
> create classes--stored in class.py doc
'''
import random
import dice
import sys
import os

def rolldice(min,max):
    print("Rolling dice...")
    global rollnum
    rollnum= random.randint(min,max)
   # input('What is you guess bewteen 1 and 6? ')

#global rollnum

#def damageroll(min, max):
#    while True:
#        global dmgroll
#        dmgroll = random.randint(min, max)
#damageroll(45, 100)

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game of DragonBallZ
=============================
Collect the Dragon Balls &
defeat Majin Buu before you
make your wish at the lookout
==============================
Commands:
  go [ex:north]
  get [item]
  use [item]
  teleport 'tele' [location]
  look
  help
  quit
  ''')

def showStatus():
    #print the player's current status
    print('---------------------------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #Print current health
    print('your current health is', health)
    #print an item or object if there is one
    if "ball" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['ball'])
    if "ball4" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['ball4']) 
    if "buu" in rooms[currentRoom]:
        print('You see Majin Buu ready to battle')
    if 'bean' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['bean'])
    if 'zsword' in rooms[currentRoom]:
        print('You see the  Zsword it might come in handy')
    print("---------------------------------------------")

#starting inventory
inventory = ['Dragon radar']

#staring health
health = 100

#a dictionary linking a room to other rooms
#also shows available items and obbjects
rooms = {

            'Kame house' : {
                  'north' : 'North city',
                  'south' : 'South city',
                  'east'  : 'East city',
                  'west'  : 'West city'
                },
            'North city' : {
                  'north' : 'The lookout',
                  'south' : 'Kame house',
                  'ball'  : '1 starball',
                },
            'The lookout' : {
                  'south': 'North city',
                  'ball' : '3 starball',
               },
            'East city' : {
                  'north' : 'Tourney grounds',
                  'west' : 'Kame house',
                  'ball'  : '7 starball',
                  'desc' : 'Welcome to East City, from here you can head north to the Tournanemt Grounds or west to Kame\'s House.' 
               },
            'Tourney grounds' : {
                  'south' : 'East city',
                  'ball' : '5 starball',
                  'buu'  : 'Kid buu',
               },
            'South city' : {
                  'south' : 'Satan city',
                  'north' : 'Kame house',
                  'ball4' : '4 starball',
                  'desc' : 'You see a conartist playing a dice game in the street. He seems to have a dragon ball with him! Beat the conartist to get the ball!'
               },
            'Satan city' : {
                  'north' : 'South city',
                  'ball' : '6 starball',
               },
            'West city' : {
                  'east' : 'Kame house',
                  'south' : 'Forest',
                  'ball' : '2 starball',
               },
            'Forest' : {
                  'north' : 'West city',
                  'zsword' : 'zsword',
            }
         }

#start at Kame's house
currentRoom = 'Kame house'

os.system('clear') #after each move/use/get/look/help then wipe the screen

showInstructions()

#ball count goes up as you collect dragon balls (7 needed to win)
ball_count = 0

#loop forever until you win
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
            if 'buu' in currentRoom:
                health -= 10
                print('Buu hit you so hard you are nearly dead, hurry and fight back')
                print(health)
            #there is no way to the new rooms then...
        else:
            print('You can\'t go that way!')

    #if they type teleport or tele first
    if move[0] == 'tele' or 'teleport':
        #to teleport they need to have the z sword in inventory
        if move[1] in rooms and 'zsword' in inventory:
            currentRoom = rooms[move[1]]
    #if they type 'get' first
    if move[0] == 'get':
        #if the room contains an item, and the item is the one they want to get
        if "ball" in rooms[currentRoom] and move[1] in rooms[currentRoom]['ball']:
            #add the item to their inventory
            inventory += [move[1]]
            ball_count += 1
            #display a message of success
            print(move[1] + ' grabbed!')
            print('you currently have', ball_count,'Dragon balls')
            #delete the item from the room
            del rooms[currentRoom]['item']
        elif "ball4" in rooms[currentRoom] and move[1] in rooms[currentRoom]["ball4"]:
            print('''Seems like a fine day in South City! You are searching around for the Dragon Balls when you see a shady man playing a dice game in the street. You walk up to him and see he has the 4 star Dragon Ball! He claims that he will only give you the Dragon Ball if you can guess the number of the die he is rolling!''')
            gamestart = input("Would you care to play a game? (y/n): ")
            if gamestart.lower() == "n":
                break #may need to be continue
            elif gamestart.lower() == "y":
                #def rolldice(min,max):
                 #   print('Rolling the die...')
                  #  global rollnum
                   # rollnum = random.randint(min,max)
                rolldice(1,6)
                print(rollnum)
                dieguess = input("Guess a number between 1 and 6! ")
                if dieguess == rollnum:
                    print("Hey! You managed to guess right and the shady man gives you the 4 star Dragon Ball")
                    inventory += [move[1]]
                    del rooms[currentRoom]["ball4"]
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
            print(move[1], 'is now in your hand, might be good to use now')
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
 
    if move[0] == 'use':
        #check that they are allowed use this item
        if move[1] in inventory and rooms[currentRoom]['buu']:
            damageroll(45, 100)
           # Goku.sword(Buu) -= dmgroll
            print('Buu took', [dmgroll], 'damage from the Zsword')

        #if move[1] in inventory and rooms[currentRoom]['buu']:
            #print('The Z Sword was very affective! This is much easier than the series looks.')
            rooms['Kame house']['bean'] = 'senzu bean'
            #delete the object from the dict
            del rooms[currentRoom]['buu']
        elif move[1] in inventory:
            health = 100
            del rooms['Kame house']['bean']
            print('You have recovered and your health is back to', health, 'Let\'s get to the lookout quickly...')
        else:
            print('You don\'t have a weapon strong enough to defeat Buu...')
    
    if move[0] == 'look':
        if 'desc' in rooms[currentRoom]:
            #print the room description
            print(rooms[currentRoom]['desc'])
        else:
            print('You don\'t see anything.')

    if move[0] == 'help':
        showInstructions()

    if move[0] in ['q', 'quit]']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
        else:
            pass

     ## Define how a player can win
    if currentRoom == 'The lookout' and ball_count == 7 and 'buu' not in rooms['Tourney grounds']:
        wish = input('***You summon Shenron***\nShenron roars! TELL ME YOUR WISH... ') #type your wish here
        print("That is out of my power, but I can can give these project makers an A+")
        break
        if currentRoom == 'The lookout' and ball_count == 7 and 'buu' in rooms['Tourney grounds']:
            print("You must defeat Buu before making your wish!")
  

