#Classes to be used in Final Project
#Creators of this document: J Hanson & Dalton McKinzie

#!/usr/bin/env python3

class Player:
    def __init__(self):
        self.hp = 50
        self.att = 0
        self.speed = 50
    def bean(self):
        self.hp == 50
    def sword(self):
        damage= 100 + self.att
        Buu.hp -= damage

class Villain:
    def __init__(self):
        self.hp = 100
        self.att = 40
        self.speed = 50

Goku= Player()
Buu= Villain()
