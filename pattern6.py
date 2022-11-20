n = int(input("enter the number:"))
row = 1
count = 1
while row<=n:
  col = 1
  while col<=row:
    print(count,end=" ")
    count = count+1
    col = col+1
  print()  
  row = row+1