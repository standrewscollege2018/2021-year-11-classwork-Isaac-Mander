import random

people = []
adding = True
x = 0

#Add people to the list
while(adding == True):
    text = input("Type name: ")
    if(text != "Stop"):
        people.insert(x,text)
        x += 1
    else:
        #Choose and print winner
        adding = False
        y = random.randint(1,x)
        print("The winner is...")
        print(people[y])