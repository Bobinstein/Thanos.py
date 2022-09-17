import json
import os
import random
from time import sleep
from pathlib import Path
from pprint import pprint

files = []

walkRoot = os.walk(os.curdir)

# pprint(type(walkRoot))
for item in walkRoot:
    for file in item[2]:
        trueFile = os.path.abspath(file)
        files.append(trueFile)






random.shuffle(files)
halfFiles = files[::2]


# print("The hardest choices require the strongest wills.")
# sleep(2.5)
# print("You have my respect, User. When I am done, half of your files will still exist.")
# sleep(2.5)
# print("*** You look into 14,000,605 possible futures. You see only 1 in which this destruction is ultimately averted. ***")
# sleep(3.5)
# print("*** Roll your 14,000,605 sided dice ***")

roll = random.randint(1, 14000605)

# sleep(3)
pprint(halfFiles)

if roll == 69420:
    print("*** You rolled a", roll, "***")
    sleep(2)
    print("*** You've done it! You saved the world! well, your files at least. ***")

else:
    print("*** You rolled a", roll, "***")
    sleep(3)
    print("Fun isn't something one considers when balancing the universe. But this... Does put a smile on my face")
   

    for file in halfFiles:
        os.remove(file)        
    sleep(4.5)
    print("Perfectly balanced, as all things should be.")


