n = int(input("enter the value:"))
row = 1
while row<=n:
  count = 1
  col = 1
  space = n - row
  while space:
    print(" ",end="")
    space = space-1
    col=col+1
  while col<=n:
    print(count,end="")  
    col = col+1
    count = count + 1
  x = row - 1
  while x:
    print(x,end="")  
    x = x-1
  row = row+1
  print()