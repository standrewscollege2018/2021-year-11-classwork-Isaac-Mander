import time
import random

spd_sound = 1481
ping_pos = [0,0]

command = 0


r1 = ["#","#","#","#","#"]
r2 = ["#","#","#","#","#"]
r3 = ["#","#","#","#","#"]
r4 = ["#","#","#","#","#"]
r5 = ["#","#","#","#","#"]

def print_grid(r1,r2,r3,r4,r5):
    print(r1)
    print()
    print(r2)
    print()
    print(r3)
    print()
    print(r4)
    print()
    print(r5)

def ping(direction,spd_sound,e1_pos,pos):
    err = random.uniform(-1.0,1.0)
    print("Ping Sent")
    if(direction == "Left") and (e1_pos[1] < pos[1]):
        time_p = pos[1] - e1_pos[1]
    elif(direction == "Right") and (e1_pos[1] > pos[1]):
        time_p = pos[1] - e1_pos[1]
    elif(direction == "Up") and (e1_pos[0] < pos[0]):
        time_p = pos[0] - e1_pos[0]
    elif(direction == "Down") and (e1_pos[0] > pos[0]):
        time_p = pos[0] - e1_pos[0]
    else: time_p = 9999
    if(time_p < 0): time_p = -time_p
    if(time_p < 10): time.sleep(time_p)
    print("Ping Recived (Sec)")
    if(time_p < 10): print(time_p + err)
    else: print(time_p)

#Shoot Torpedo
def shoot(pos,e1_pos):
    t_dir = input("Torpedo Direction: ")
    if(t_dir == "Up"):
        if(e1_pos[0] - 1 == pos[0]):
            return True
        else:
            return False      
    elif(t_dir == "Down"):
        if(e1_pos[0] + 1 == pos[0]):
            return True 
        else:
            return False      
    elif(t_dir == "Left"):
        if(e1_pos[1] +  1 == pos[1]):
            return True   
        else:
            return False      
    elif(t_dir == "Right"):
        if(e1_pos[1] - 1 == pos[1]):
            return True  
        else:
            return False      
        
    else:
        return False       
#Update Map
def update_map():
    global pos, r1,r2,r3,r4,r5,update_y
    r1 = ["#","#","#","#","#"]
    r2 = ["#","#","#","#","#"]
    r3 = ["#","#","#","#","#"]
    r4 = ["#","#","#","#","#"]
    r5 = ["#","#","#","#","#"]    
    update_y = pos[1] - 1
    if(pos[0] == 1): r1[update_y] = "S"
    if(pos[0] == 2): r2[update_y] = "S"
    if(pos[0] == 3): r3[update_y] = "S"
    if(pos[0] == 4): r4[update_y] = "S"
    if(pos[0] == 5): r5[update_y] = "S"

    print_grid(r1,r2,r3,r4,r5)


pos = [random.randint(1,5),random.randint(1,5)]
e1_pos = [random.randint(1,5),random.randint(1,5)]




#Run Code
def menu(e1_pos,pos):
    global command
    var = input()
    if(var == "Left"):
        pos[1] += -1
        command += 1
    if(var == "Right"):
        pos[1] += 1
        command += 1
    if(var == "Up"):
        pos[0] += -1
        command += 1
    if(var == "Down"):
        pos[0] += 1
        command += 1
    if(var == "Ping"):
        command += 1
        direction = input("Direction: ")
        
        if(direction == "Left") or (direction == "Right") or (direction == "Up") or (direction == "Down"): ping(direction,spd_sound,e1_pos,pos)
        else: pass
    if(var == "Map"):
        update_map()
        command += 1
    if(var == "Shoot"):
        command += 1
        if(shoot(pos,e1_pos) == True):
            e1_pos = [0,0]
            print("SUNK")
        else: print("MISS")
       # if(e1_pos[1] + 1 == pos[1]): print("Dsfd")



#Int Check
def int_check(var):
    try: 
        int(var)
        return True
    except ValueError:
        return False 

while(True):
    menu(e1_pos,pos)
    #Enemy Movement
    #print(command)
    #print("X: " + str(e1_pos[1]) + " Y: " + str(e1_pos[0]))
    if(command == 5):
        print("Enemy Moved")
        ran = random.randint(0,1)
        ran2 = random.randint(0,1)
        if(ran == 1):
            if(ran2 == 0): e1_pos[1] += 1
            if(ran2 == 1): e1_pos[1] += -1            
            if(e1_pos[1] >= 5): e1_pos[1] = 4
            if(e1_pos[1] <= 0): e1_pos[1] = 2
        elif(ran == 0):
            if(ran2 == 0): e1_pos[0] += 1
            if(ran2 == 1): e1_pos[0] += -1
            if(e1_pos[0] >= 5): e1_pos[0] = 4
            if(e1_pos[0] <= 0): e1_pos[0] = 2 
        command = 0