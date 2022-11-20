n = int(input("enter the value of n:"))
row = 1
c = 64
while row<=n:
  col = 1
  c = c+1
  while col<=n:
    print(chr(c),end=" ")
    col = col+1
  print()  
  row = row + 1

  
