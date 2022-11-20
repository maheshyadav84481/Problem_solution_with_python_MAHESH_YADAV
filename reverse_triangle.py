'''n = int(input("enter the variable:"))
r = 1
while r<=n:
    space = n - r
    c = 1
    while space:
        print(" ", end="")
        space = space - 1
        c = c+1

    while c<=n:
        print("*",end="")
        c = c+1
    x = r - 1
    while x:
        print(x,end="")
        x = x - 1

    r = r+1
    print()'''
n = int(input("enter the number :"))
row = 1
while(row<=n):
  star = n-row+1
  while(star):
    print("*",end=" ")
    star = star-1
  print()
  row = row+1
