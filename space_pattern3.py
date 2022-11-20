from tkinter import E


n = int(input("enter the value:"))
row = 1
while row<=n:
  col = 1
  space = row - 1
  while space:
    print(" ",end="")
    space = space-1
    col = col + 1
  count = row
  while col<=n:
    print(count,end="")
    col = col + 1
  print()
  row = row + 1