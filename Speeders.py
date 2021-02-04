#Speeders Task
#Tests if person has gone over the speed limit

print("Hello User")
print("")

#Variables
name = ""
speed = 0
speed_limit = 0
fine = 0
error = False

#Inputs
name = input("Offenders name: ")
speed = input("Speed of person (Integer): ")
speed_limit = input("Speed limit (Integer): ")

#Convert to float
speed = float(speed)
speed_limit = float(speed_limit)


#Calculate Fine
if(error == False):
    dif = speed - speed_limit
    if(speed < speed_limit):
        print("Under Speed limit, no fine needed")
    elif(dif > 29): fine = 180
    elif(dif >= 20): fine = 130
    elif(dif >= 10): fine = 80
    else: fine = 30
else:
    print("That is an invalid input")

#Print out Speed and Fine
if(error == False):
    print(name + " was going " + str(dif) + "kph over the speed limit of " + str(speed_limit) + "kph")
    print("The fine is $" + str(fine))