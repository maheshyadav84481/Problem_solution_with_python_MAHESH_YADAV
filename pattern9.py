n = int(input("enter the value of n:"))
row = 1
while row<=n:
  col = 1
  while col<=row:
    print(row-col+1,end=" ")
    col = col+1
  print()  
  row = row+1