#!/usr/bin/env python3

def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for x in farms:
        print(x)

    for x in farms:
        if (x.get("name") == "NE Farm"):
            print(f"The animals on the NE Farm are {x['agriculture']}")
    #print(farms[0]["name"], farms[1]["name"], farms[2]["name"])
    
    name = input("Which farm do you want to look up? ").lower()

    for x in farms:
        if (x.get("name").lower() == name):
            print(f"The agriculture in {name} are: {x['agriculture']}")

if __name__ =="__main__":
    main()
