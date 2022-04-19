#!/usr/bin/env python3

pokedex={"Bulbasaur":"Grass/Poison",
         "Squirtle":"Water",
         "Charmander":"Fire"}

pokedex["Pikachu"] = "Electric"

x=", ".join(pokedex.keys())

print(x)

choice= input("Name a Generation 1 starter Pokemon:\n>")

#print(pokedex[choice])

#print(pokedex.get("choice"))

# print(pokedex.get(choice), "Sorry, we don't have any record of that Pokemon!")

print(pokedex.get(choice, "Sorry, we don't have any record of that Pokemon!"))

"""print(pokedex.keys())
print(pokedex.values())
"""

#print(pokedex)
