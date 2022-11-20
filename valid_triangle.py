a = int(input("enter the value of a:"))
b = int(input("enter the value of b:"))
c = int(input("enter the value of c:"))
if a+b>c:  
  if b+c>a:
    if c+a>b:
      print("valid triangle")
    else:
      print("invalid triangle")  
  else:
    print("invalid triangle")
else:
  print("invalid triangle")