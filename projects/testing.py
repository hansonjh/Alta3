#!/usr/bin/python3

def showInstructions():
  #Shows the menu and the command list
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  use [item]
''')

def showStatus():
  #Shows the player's status
  print('**********************')
  print("Current health is " + str(health))
  print('You are in the ' + currentRoom)
  #Shows the players current inventory list
  print('Inventory : ' + str(inventory))
  #Shows an item if there is one in the current room
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("**********************")

#Shows player starting health
health = 30

#shows player inventory, starts out empty
inventory = []

#A dictionary linking one room to the other rooms that connect to it
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'south' : 'Dead End'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'candy',
            },
            'Dead End' : {}
         }


def itemfunc(item):
    if item == "potion":
        global health
        health = health + 10
        print("You have healed 10 health!!")
        inventory.remove("potion")
    if item == "candy":
        print("Eating the candy gave you a boost of energy to help you escape.")
        inventory.remove("cookie")




#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loops the script
while True:

  showStatus()

  #type 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space in the player inventory
  # get secret key is returned ["get", "key"]          
  move = move.lower().split(" ", 1)

  # type 'go' first then direction
  if move[0] == 'go':
    #check to make sure they are allowed where they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room they entered
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('Sorry but you can\'t go that way!')

  #type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and it is what they want
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #adds the item to their inventory when they pick it up
      inventory += [move[1]]
      #display a helpful message if the player is stuck
      print(move[1] + ' got!')
      #delete the item from the room after they pick it up
      del rooms[currentRoom]['item']
    #if the item isn't there to get
    else:
      #tells them they can't get the item
      print('Can\'t get ' + move[1] + '!')

  #when the player tries to use an item from their inventory
  if move[0] == "use":
      if move[1] in inventory:
          itemfunc(move[1])
      else:
          print(move[1] + " Sorry that item is not in your inventory at this time")
  

  # Defines what the player has to do to win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the secret key and magical potion... YOU WIN!')
    break

  # If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('The monster killed you...Btter luck next time... GAME OVER!')
    break
