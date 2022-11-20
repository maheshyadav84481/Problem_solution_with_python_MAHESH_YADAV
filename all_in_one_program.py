ch = (input("odd&even" "palindrom" "positive&negative""reverse string"))
num = (input("enter the element:"))
if ch == "odd&even":
   if num % 2 == 0:
        print("even")
   else:
        print("odd")
if ch =="palindrom":
    reverse = num[ : :-1]
    if (num == reverse):
      print("it is palindrom")
    else:
      print("it is not palindrom")
if ch == "positive & negative":
  if num >= 0:
    print("positive ")
  else:
    print("negative")
if ch == "reverse string":
  reverse = num[: :-1]
  print(reverse)
else:
  print(ch)  
         
        