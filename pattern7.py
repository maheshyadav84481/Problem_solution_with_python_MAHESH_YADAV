n = int(input("enter the value of n:"))
row = 1
while(row<=n):
  value = row
  col = 1
  while(col<=row):
    print(value,end=" ")
    value = value+1
    col = col + 1
  print()  
  row = row+1