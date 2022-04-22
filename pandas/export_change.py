#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Challenge Solution 01 - JSON to Excel"""

import pandas as pd

def main():

    # create a dataframe from json
    df = pd.read_csv("5movies.csv")

    df.drop_duplicates(inplace=True)

    sorteddf = df.sort_values(["Title"])

    print(sorteddf)

    # writeout dataframe to excel
    df.to_excel("5movies-translated-from-json.xlsx")

if __name__ == "__main__":
    main()

