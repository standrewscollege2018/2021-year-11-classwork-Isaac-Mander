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
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)

display_grid(a,b,c,d,e,f,g,h,i)
shoot = input("Input Location e.g. (A1): ")
print(shoot[0])
print(shoot[1])

if(shoot[0] == "a"): a[int(shoot[1])-1] = 1
display_grid(a,b,c,d,e,f,g,h,i)