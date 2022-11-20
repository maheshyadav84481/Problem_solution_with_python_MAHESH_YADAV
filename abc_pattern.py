n = int(input("enter the number:"))
row = 1
x = 0
while row<=n:
  col = 1
  while col<=n:
    print(chr(65 + x),end=" ")
    col = col+1
    x = x+1
  print()  
  row = row+1