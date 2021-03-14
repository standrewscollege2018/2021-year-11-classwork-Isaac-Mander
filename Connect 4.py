player = 1 # P1, P2

#Rows left to right
#row = [["#", "#", "#", "#", "#", "#"],["#", "#", "#", "#", "#", "#"],["#", "#", "#", "#", "#", "#"],["#", "#", "#", "#", "#", "#"],["#", "#", "#", "#", "#", "#"],["#", "#", "#", "#", "#", "#"],["#", "#", "#", "#", "#", "#"]]
r1 = ["#", "#", "#", "#", "#", "#"]
r2 = ["#", "#", "#", "#", "#", "#"]
r3 = ["#", "#", "#", "#", "#", "#"]
r4 = ["#", "#", "#", "#", "#", "#"]
r5 = ["#", "#", "#", "#", "#", "#"]
r6 = ["#", "#", "#", "#", "#", "#"]
r7 = ["#", "#", "#", "#", "#", "#"]



#Print Grid
def grid():
    #Give Access to Var
    global r1, r2, r3, r4, r5, r6, r7

    print(r1[0],r2[0],r3[0],r4[0],r5[0],r6[0],r7[0])
    print(r1[1],r2[1],r3[1],r4[1],r5[1],r6[1],r7[1])
    print(r1[2],r2[2],r3[2],r4[2],r5[2],r6[2],r7[2])
    print(r1[3],r2[3],r3[3],r4[3],r5[3],r6[3],r7[3])
    print(r1[4],r2[4],r3[4],r4[4],r5[4],r6[4],r7[4])
    print(r1[5],r2[5],r3[5],r4[5],r5[5],r6[5],r7[5])

#Place Thingy
def turn():
    global player
    print("Player " + str(player))
    text = input("What Row?: ")
    if(int_check(text) == True):
        place(int(text))
        win_check()
        


def place(row):
    global r1,r2,r3,r4,r5
    if(row == 1):
        if(r1[5] == "#"): r1[5] = str(player)
        elif(r1[4] == "#"): r1[4] = str(player)
        elif(r1[3] == "#"): r1[3] = str(player)
        elif(r1[2] == "#"): r1[2] = str(player)
        elif(r1[1] == "#"): r1[1] = str(player)
        elif(r1[0] == "#"): r1[0] = str(player)
    if(row == 2):
        if(r2[5] == "#"): r2[5] = str(player)
        elif(r2[4] == "#"): r2[4] = str(player)
        elif(r2[3] == "#"): r2[3] = str(player)
        elif(r2[2] == "#"): r2[2] = str(player)
        elif(r2[1] == "#"): r2[1] = str(player)
        elif(r2[0] == "#"): r2[0] = str(player)
    if(row == 3):
        if(r3[5] == "#"): r3[5] = str(player)
        elif(r3[4] == "#"): r3[4] = str(player)
        elif(r3[3] == "#"): r3[3] = str(player)
        elif(r3[2] == "#"): r3[2] = str(player)
        elif(r3[1] == "#"): r3[1] = str(player)
        elif(r3[0] == "#"): r3[0] = str(player)
    if(row == 4):
        if(r4[5] == "#"): r4[5] = str(player)
        elif(r4[4] == "#"): r4[4] = str(player)
        elif(r4[3] == "#"): r4[3] = str(player)
        elif(r4[2] == "#"): r4[2] = str(player)
        elif(r4[1] == "#"): r4[1] = str(player)
        elif(r4[0] == "#"): r4[0] = str(player)
    if(row == 5):
        if(r5[5] == "#"): r5[5] = str(player)
        elif(r5[4] == "#"): r5[4] = str(player)
        elif(r5[3] == "#"): r5[3] = str(player)
        elif(r5[2] == "#"): r5[2] = str(player)
        elif(r5[1] == "#"): r5[1] = str(player)
        elif(r5[0] == "#"): r5[0] = str(player)
    if(row == 6):
        if(r6[5] == "#"): r6[5] = str(player)
        elif(r6[4] == "#"): r6[4] = str(player)
        elif(r6[3] == "#"): r6[3] = str(player)
        elif(r6[2] == "#"): r6[2] = str(player)
        elif(r6[1] == "#"): r6[1] = str(player)
        elif(r6[0] == "#"): r6[0] = str(player)
    if(row == 7):
        if(r7[5] == "#"): r7[5] = str(player)
        elif(r7[4] == "#"): r7[4] = str(player)
        elif(r7[3] == "#"): r7[3] = str(player)
        elif(r7[2] == "#"): r7[2] = str(player)
        elif(r7[1] == "#"): r7[1] = str(player)
        elif(r7[0] == "#"): r7[0] = str(player)
    

#Check if int                    Error Catching
def int_check(var):
    try: 
        int(var)
        return True
    except ValueError:
        return False

#Check if winner
def win_check():
    global r1,r2,r3,r4,r5,r6,r7,player
    #Looping
    cycles = 6     # 6 by 7 grid
    row = 1
    x = 5
    if(cycles > 0):
        if(row == 7):
            if(r7[x] == str(player)):
                if(win_types(1,r7,x,player) == True): 
                    print("Player " + str(player) + " wins!")
                    grid()
                    lock()
            else:
                if(x > 0): x += -1
                else: 
                    row += 1
                    x = 5        
        if(row == 6):
            if(r6[x] == str(player)):
                if(win_types(1,r6,x,player) == True): 
                    print("Player " + str(player) + " wins!")
                    grid()
                    lock()
            else:
                if(x > 0): x += -1
                else: 
                    row += 1
                    x = 5        
        elif(row == 5):
            if(r5[x] == str(player)):
                if(win_types(1,r5,x,player) == True): 
                    print("Player " + str(player) + " wins!")
                    grid()
                    lock()
            else:
                if(x > 0): x += -1
                else: 
                    row += 1
                    x = 5
        elif(row == 4):
            if(r4[x] == str(player)):
                if(win_types(1,r4,x,player) == True): 
                    print("Player " + str(player) + " wins!")
                    grid()
                    lock()
            else:
                if(x > 0): x += -1
                else: 
                    row += 1
                    x = 5        
        elif(row == 3):
            if(r3[x] == str(player)):
                if(win_types(1,r3,x,player) == True): 
                    print("Player " + str(player) + " wins!")
                    grid()
                    lock()
            else:
                if(x > 0): x += -1
                else: 
                    row += 1
                    x = 5
        elif(row == 2):
            if(r2[x] == str(player)):
                if(win_types(1,r2,x,player) == True): 
                    print("Player " + str(player) + " wins!")
                    grid()
                    lock()
            else:
                if(x > 0): x += -1
                else: 
                    row += 1
                    x = 5        
        elif(row == 1):
            if(r1[x] == str(player)):
                if(win_types(1,r1,x,player) == True): 
                    print("Player " + str(player) + " wins!")
                    grid()
                    lock()
            else:
                if(x > 0): x += -1
                else: 
                    row += 1
                    x = 5
        
        #x += -1
        #cycles += -1
                
            
                
                
                
                
                
                
                
                
                
                

                

#Win Types   1 = Up  2 = Accross  3 = Diagonal Left  4 = Diagonal Right
def win_types(angle,row,x,player):
    #Up
    if(True):
        if((row[x] == str(player)) and (row[x-1] == str(player)) and (row[x-2] == str(player)) and (row[x-3] == str(player))):
            return True

#Lock Screen For All Input
def lock():
    while(True):
        lock = 0

while(True):
    grid()
    turn()
    if(player == 1): player = 2
    elif(player == 2): player = 1