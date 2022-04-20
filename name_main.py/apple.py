# apple.py
import banana
import requests


# lookin up charmander
url= "https://pokeapi.co/api/v2/pokemon/charmander"
resp= requests.get(url)

x= banana.peel(resp)

print(f'{x["name"]} is {x["height"]} units tall.')
