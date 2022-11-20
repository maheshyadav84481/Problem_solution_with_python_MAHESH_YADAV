n = int(input("enter the number:"))
row = 1
while row<=n:
  value = row
  col = 1
  while col<=n:
    c = (64+col)
    print(chr(c),end="")
    col = col+1
  print()  
  row = row + 1
  