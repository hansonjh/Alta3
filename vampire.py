#!/usr/bin/env python3

#pulling specific lines from the dracula novel 345... in /mycode
teeth = open("vamplines.txt", "w")
with open("345-0.txt", "r") as vamps:
    count = 0
    for lines in vamps:
        #print(vamps)
        #print(vamps.find("vampire")
        if "vampire" in lines.lower():
            count += 1
            print(lines, end="")
            teeth.write(lines)

teeth.close()
print(count, "times the word vampire was said.")

