#!/usr/bin/python3

#DBZ game play
# Created by Dalton M. and J H.

# Replace RPG starter project with this code when new instructions are live

from random import randint

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game of DragonBallZ
========
Commands:
  go [direction]
  use [item]
  teleport[rooms]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
  if "buu" in rooms[currentRoom]:
      print('You see Majin Buu ready to battle')
  if "sword" in rooms[currentRoom]:
      print('That Z Sword night come in handy')
  print("---------------------------")

#an inventory, which is initially empty
inventory = ['Dragon radar']

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
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
                  'item'  : '1 starball',
                },
            'The lookout' : {
                  'south': 'North city',
                  'item' : '3 starball',
               },
            'East city' : {
                  'north' : 'Tourney grounds',
                  'west' : 'Kame house',
                  'item'  : '7 starball',
               },
            'Tourney grounds' : {
                   'south' : 'East city',
                   'item' : '5 starball',
                   'buu'  : 'Kid buu',
               },
            'South city' : {
                  'south' : 'Satan city',
                  'north' : 'Kame house',
                  'item' : '4 starball',
               },
            'Satan city' : {
                  'north' : 'South city',
                  'item' : '6 starball',
               },
            'West city' : {
                  'east' : 'Kame house',
                  'south' : 'Forest',
                  'item' : '2 starball',
               },
            'Forest' : {
                  'north' : 'West city',
                  'sword' : 'Z sword',
            }
         }

#start the player in the Hall
currentRoom = 'Kame house'

showInstructions()

ball_count = 0

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      ball_count += 1
      #display a helpful message
      print(move[1] + ' grabbed!')
      print(ball_count)
      #delete the item from the room
      del rooms[currentRoom]['item']
    elif "sword" in rooms[currentRoom] and move[1] in rooms[currentRoom]['sword']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' picked up!')
      #delete the item from the room
      del rooms[currentRoom]['sword']  

    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  
  if move[0] == 'use':
    #check that they are allowed use this item
    if move[1] in inventory and rooms[currentRoom]['buu']:
        print('The Z Sword was very affective! This is much easier than the series looks.')
        del rooms[currentRoom]['buu']
    else:
        print('You don\'t have a weapon strong enough to defeat Buu...')
  
  ## Define how a player can win
  if currentRoom == 'The lookout' and ball_count == 7 and 'buu' not in rooms['Tourney grounds']:
    wish = input('Shenron roars! TELL ME YOUR WISH... ') #type your wish here
    print("That is out of my power, but I can give you...")
    break
  else:
      print("You must defeat Buu before making your wish!")
  

  ## If a player enters a room with a monster
  #elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
   # print('A monster has got you... GAME OVER!')
    #break
