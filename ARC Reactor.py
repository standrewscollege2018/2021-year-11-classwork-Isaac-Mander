#Simulates ARC reactor made by STORK INC

#Variables
reactors = 3
power = [30,95,0,0,0,0,0,0,0,0]
config = False

run = True

#Menu
def menu():
    print("Main Menu")
    print("1] Reactor Levels")
    print("2] Total Output")
    print("3] Change Reactor Power Level")
    print("4] Config Reactors")
    #Menu Input
    menu_text = input("Selector: ")
    if(menu_text == "1") or (menu_text == "2") or (menu_text == "3") or (menu_text == "4"):
        menu_text = int(menu_text)
        print("")
        if(menu_text == 1):
            reactor_levels()
        if(menu_text == 2):
            total_output()
        if(menu_text == 3):
            power_level()
        if(menu_text == 4): 
            config_reactors()  
    else:
        print("INVALID")
        print("")

#Reactor Levels
def reactor_levels():
    #Loop for showing all Reactors
    for i in range(reactors,0,-1):
        print("Reactor" + str(reactors - i + 1))
        print(str(power[reactors - i]) + "%")
        print(str((power[reactors - i]/100) * 3000) + "XW")
        print("")

#Total Output
def total_output():
    total = 0
    i = 0
    for i in range(reactors,0,-1):
        total += ((power[i-1])*30)
    print("Total Reactor Output is " + str(total) + "XW")
    print("")

#Change Reactor Power Level
def power_level():
    #Input for reactor you want to change
    print("Avalible Reactors are 1 to " + str(reactors))
    p_text = input("What reactor do you want to change?: ")
    if(p_text == "1") or (p_text == "2") or (p_text == "3") or (p_text == "4") or (p_text == "5") or (p_text == "6") or (p_text == "7") or (p_text == "8") or (p_text == "9") or (p_text == "10") and (p_text <= reactors):
        if(int(p_text) <= reactors):
        #Change Power Levels
            print("Reactor " + p_text + " it currently at " + str(power[int(p_text)-1]) + "%")
            p2 = input("Input new power level (%): ")
            #If the input is int and equal or under 100%
            if(int_check(p2) == True):
                if(int(p2) <= 100): power[int(p_text)-1] = int(p2)
                #If invalid
                else: print("INVALID")
            #If invalid
            else: print("INVALID")
            print("")
        #If invalid
        else:
            print("INVALID")
            print("")
    #If invalid
    else:
        print("INVALID")
        print("")    

#Check if int                    Error Catching
def int_check(var):
    try: 
        int(var)
        return True
    except ValueError:
        return False    
#Credit to https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except

#Config Reactors
def config_reactors():
    global reactors
    #Input for config menu
    print("1] Config New Reactor")
    print("2] Permanently Remove Reactor")
    c_text = input("Selector: ")
    if(int_check(c_text) == True):
        #Create New Reactor
        if(c_text == "1"):
            #If no space
            if(reactors == 10):
                print()
                print("No Space")
                print()
            #If space
            else:
                reactors += 1
                power[reactors-1] = 0
                print()
                print("Added New Reactor")
                print()
        #Delete Reactor
        if(c_text == "2"):
            print("Are you sure?: Y/N")
            c2_input = input("Selector: ")
            #If Yes
            if((c2_input.upper() == "Y")):
                print("Deleted Reactor " + str(reactors))
                power[int(reactors)-1] = 0
                reactors += -1
            #If No
            elif(c2_input.upper() == "N"):
                print()
                print()
            #If not Y/N
            else:
                print("INVALID")

            
                
    else: print("INVALID")

#Run Code
reactors = 3
while(run == True):
   # var = reactors
    menu()