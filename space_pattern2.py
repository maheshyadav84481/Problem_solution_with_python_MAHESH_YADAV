n = int(input("enter the value:"))
row = 1
while row<=n:
  space = n - row
  col = 1
  while space:
    print(" ",end="")
    space = space - 1
    col = col+1
  while col<=n:
    print(row,end="")
    col = col+1
  print()  
  row = row + 1