n = 5
r = 1
while r<=n:
  c = 1
  space = n-r
  while space<=c:
    print(" ",end="")
    space = space - 1
    c = c+1
  while c<=n:
    print("*",end="")
    c = c+1
  print()    
  r = r+1