#!/usr/bin/env python3

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "power": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "power": "shape shifting",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "power": "super strength",
  "archenemy": "adrenaline"}
             }

char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk):\n>")

char_stat = input("Which statistic do you want to know about? (real name, power, archenemy):\n>")

print(f"{char_name.title()}'s {char_stat} is: " + marvelchars[char_name][char_stat].title())
