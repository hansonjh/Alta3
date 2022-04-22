#!/usr/bin/env python3

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# get pokedex.txt with the following command:
# wget https://raw.githubusercontent.com/csfeeser/Python/master/data%20sets/pokedex.txt


# pandas will convert your data into a special object
# called a DATAFRAME
pokedf= pd.read_csv("pokedex.txt", index_col=1)

# get rid of any duplicate pokemon
pokedf.drop_duplicates(inplace=True)

# sort the pokemon by their total stat pool
sorteddf= pokedf.sort_values(["Total"], ascending=False)

# eliminate all columns except name and speed
sorteddf.drop(sorteddf.columns.difference(["Name","Speed"]), 1, inplace=True)
print(sorteddf)

# use .head(10) to get the first 10 pokemon in the dataframe
# use .plot(kind="barh") to plot that data to a horizontal bar graph
sorteddf.head(10).plot(kind="barh")

# save that bar graph as a file in the location of your choosing
plt.savefig("/home/student/static/top10pokemon.png", bbox_inches="tight")
