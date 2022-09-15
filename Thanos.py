from genericpath import isfile
import os
import random
from time import sleep

files = []



for root, dirs, file in os.walk(".", topdown=False):
    if file == "Thanos.py"  or file == "README" or dirs == "Thanos.py" or dirs == ".git":
        continue
    files.append(file)
    files.append(dirs)


random.shuffle(files)
halfFiles = files[::2]


print("The hardest choices require the strongest wills.")
sleep(2.5)
print("You have my respect, User. When I am done, half of your files will still exist.")
sleep(2.5)
print("*** You look into 14,000,605 possible futures. You see only 1 in which this destruction is ultimately averted. ***")
sleep(3.5)
print("*** Roll your 14,000,605 sided dice ***")

roll = random.randint(1, 14000605)

sleep(3)

if roll == 69420:
    print("*** You rolled a", roll, "***")
    sleep(2)
    print("*** You've done it! You saved the world! well, your files at least. ***")

else:
    print("*** You rolled a", roll, "***")
    sleep(3)
    print("Fun isn't something one considers when balancing the universe. But this... Does put a smile on my face")
    for file in halfFiles:
        if not isinstance(file, list):
            try:
                if os.path.isfile(file):
                    os.remove(file)
            except Exception as e:
                print(e)
        else:
            for item in file:
                if not isinstance(item, list):
                    try:
                        if os.path.isfile(item):
                            os.remove(item)
                    except Exception as e:
                        print(e)
                else:
                    for subItem in item:
                        if not isinstance(subItem, list):
                            try:
                                if os.path.isfile(subItem):
                                    os.remove(subItem)
                            except Exception as e:
                                print(e)
                        else:
                            print("you have to keep going man!!")
      
    sleep(4.5)
    print("Perfectly balanced, as all things should be.")


