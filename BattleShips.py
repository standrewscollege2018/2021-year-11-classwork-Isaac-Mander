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


def display_grid(a,b,c,d,e,f,g,h,i):
    print("A " + str(a))
    print("B " + str(b))
    print("C " + str(c))
    print("D " + str(d))
    print("E " + str(e))
    print("F " + str(f))
    print("G " + str(g))
    print("H " + str(h))
    print("I " + str(i))

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
display_grid(a,b,c,d,e,f,g,h,i) 