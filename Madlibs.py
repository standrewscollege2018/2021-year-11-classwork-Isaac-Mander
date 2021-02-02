import time
import random

#Input Var
name = input("What is the name of your character: ")
wire = input("Pick a colour: ")
count = input("Choose a random number between 5-20: ")
building = input("Choose a wall type: ")

#Starting Text
print("Bomb defuser " + name + " is in a room defusing a bomb")
time.sleep(3)
print("The clock ticks down from " + count)
count = int(count)
#Countdown
rand = random.randint(-3,count - 1)
while(count > 0):
    print(count)
    count += -1
    time.sleep(1)
    #You Win
    if(count == rand):
        print("You cut the " + wire + " wire")
        print("You win")
        while(True):
            1 * 1
    #You Lose
    if(count <= 0):
        count = 0
        print("BOOM")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("The " + building + " collapses around your dead body")
    