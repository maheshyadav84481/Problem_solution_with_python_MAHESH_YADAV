i = 1
a1 = 0
a2 = 1
n = int(input("enter the value of n:"))
print(a1,"\n",a2)
while i<=n:
  a3 = a1+a2
  print(a3)
  a1 = a2
  a2 = a3
  i = i+1