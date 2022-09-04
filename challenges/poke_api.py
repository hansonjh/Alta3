#!/usr/bin/env python3
# fact gatherer for all pokemon using PokeAPI website

import requests
import wget

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    #print(pokeapi)

    print(pokeapi['sprites']['front_default'])
    imgurl = pokeapi['sprites']['front_default']

    wget.download(imgurl, '/home/student/static/')    

    print('\n', pokeapi['name'], 'has the following moves')

    for x in pokeapi['moves']:
        print(' >', x['move']['name'])
    
    print(pokeapi['name'], 'has appeared in', len(pokeapi["game_indices"]), 'games.')

    game_indices = 0

    for g in pokeapi['game_indices']:
        game_indices += 1
    print(pokeapi['name'], 'has appeared in', game_indices, 'video games') 

main()
