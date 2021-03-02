#Battleships Game

#Variables
turn = 0 #P1-0  P2-1



head = [1,2,3,4,5,6,7,8,9]
a = [0,0,0,0,0,0,0,0,0]
b = [0,0,0,0,0,0,0,0,0]
c = [0,0,0,0,0,0,0,0,0]
d = [0,0,0,0,0,0,0,0,0]
e = [0,0,0,0,0,0,0,0,0]
f = [0,0,0,0,0,0,0,0,0]
g = [0,0,0,0,0,0,0,0,0]
h = [0,0,0,0,0,0,0,0,0]
i = [0,0,0,0,0,0,0,0,0]

a2 = [0,0,0,0,0,0,0,0,0]
b2 = [0,0,0,0,0,0,0,0,0]
c2 = [0,0,0,0,0,0,0,0,0]
d2 = [0,0,0,0,0,0,0,0,0]
e2 = [0,0,0,0,0,0,0,0,0]
f2 = [0,0,0,0,0,0,0,0,0]
g2 = [0,0,0,0,0,0,0,0,0]
h2 = [0,0,0,0,0,0,0,0,0]
i2 = [0,0,0,0,0,0,0,0,0]

def display_grid1(head,a,b,c,d,e,f,g,h,i):
    print("  " + str(head))
    print("A " + str(a))
    print("B " + str(b))
    print("C " + str(c))
    print("D " + str(d))
    print("E " + str(e))
    print("F " + str(f))
    print("G " + str(g))
    print("H " + str(h))
    print("I " + str(i))

def shoot1(turn):
    global a,b,c,d,e,f,g,h,i
    shoot = input("Input Location e.g. (A1): ")
    if(shoot[0] == "a"): a[int(shoot[1])-1] = 1
    if(shoot[0] == "b"): b[int(shoot[1])-1] = 1
    if(shoot[0] == "c"): c[int(shoot[1])-1] = 1
    if(shoot[0] == "d"): d[int(shoot[1])-1] = 1
    if(shoot[0] == "e"): e[int(shoot[1])-1] = 1
    if(shoot[0] == "f"): f[int(shoot[1])-1] = 1
    if(shoot[0] == "g"): g[int(shoot[1])-1] = 1
    if(shoot[0] == "h"): h[int(shoot[1])-1] = 1
    if(shoot[0] == "i"): i[int(shoot[1])-1] = 1

def display_grid2(head,a,b,c,d,e,f,g,h,i):
    print("  " + str(head))
    print("A " + str(a2))
    print("B " + str(b2))
    print("C " + str(c2))
    print("D " + str(d2))
    print("E " + str(e2))
    print("F " + str(f2))
    print("G " + str(g2))
    print("H " + str(h2))
    print("I " + str(i2))
    
def shoot2(turn):
    global a2,b2,c2,d2,e2,f2,g2,h2,i2
    shoot2 = input("Input Location e.g. (A1): ")
    if(shoot2[0] == "a"): a2[int(shoot[1])-1] = 1
    if(shoot2[0] == "b"): b2[int(shoot[1])-1] = 1
    if(shoot2[0] == "c"): c2[int(shoot[1])-1] = 1
    if(shoot2[0] == "d"): d2[int(shoot[1])-1] = 1
    if(shoot2[0] == "e"): e2[int(shoot[1])-1] = 1
    if(shoot2[0] == "f"): f2[int(shoot[1])-1] = 1
    if(shoot2[0] == "g"): g2[int(shoot[1])-1] = 1
    if(shoot2[0] == "h"): h2[int(shoot[1])-1] = 1
    if(shoot2[0] == "i"): i2[int(shoot[1])-1] = 1

shoot1(turn)
display_grid1(head,a,b,c,d,e,f,g,h,i)