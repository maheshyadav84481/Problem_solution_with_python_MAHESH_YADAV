num = int(input("enter the value :"))
ans = 0
i = 0
while num!=0:
  mod = num % 2
  ans = mod*pow(10,i)+ans
  i = i+1
  num = int(num/2)
print(ans)
