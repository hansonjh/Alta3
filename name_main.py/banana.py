# banana.py
import requests

def peel(slappy):
    """Take all that JSON data, check to make sure it's good, 
    then convert to Python data"""

    if slappy.status_code == 200:
        return slappy.json()
    else:
       # if it's a bad response
        return False

def main(): # main should be the BULK of your code!

    url= "https://pokeapi.co/api/v2/pokemon/bulbasaur"
    resp= requests.get(url)
    pokedex= peel(resp)
    print(f'{pokedex["name"]} is {pokedex["height"]} units tall.')

# if this script is being called directly:
if __name__ == "__main__":
    main()
