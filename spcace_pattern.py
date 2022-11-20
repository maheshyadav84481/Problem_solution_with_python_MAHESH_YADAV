n = int(input("enter the value:"))
row = 1
while row<=n:
  col = 1
  space = row - 1 #space ko print karane ke liye li hai ye value.
  while space:
    print(" ",end="")
    space = space - 1
    col = col+1
  while col<=n:
    print(row,end="")  
    col = col+1
  print()  
  row = row + 1
