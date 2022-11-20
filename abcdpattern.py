n = int(input("enter the value:"))
row = 1
while row<=n:
  col = 1
  while col<=n:
    print(chr(65 + col + row -2),end=" ")
    col = col+1
  print()  
  row = row+1