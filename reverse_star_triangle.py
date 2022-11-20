n = int(input("enter the number :"))
row = 1
while(row<=n):
  star = n-row+1
  while(star):
    print("*",end=" ")
    star = star-1
  print()  
  row = row+1
