from calendar import c


n = int(input("enter the number :"))
r = 1
while r<=n:
  c = 1
  while c<=r:
    print(chr(65+r+c+1))
    c = c + 1
  print()  
  r = r+1