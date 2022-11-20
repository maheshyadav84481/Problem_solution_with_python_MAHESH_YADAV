'''n = int(input("enter the value:"))
r = 1
while r <= n:
    c = 1
    al = 65 - r + n
    while c <= r:
        print(chr(al),end="")
        al = al + 1
        c = c + 1
    r = r + 1
    print()'''
n = int(input("enter the element:"))
r = 1
while r<=n:
    c = 1
    al =  65
    while c<=n:
        print(chr(al),end="")
        al = al + 1
        c = c+1
    r = r+1
    print()
