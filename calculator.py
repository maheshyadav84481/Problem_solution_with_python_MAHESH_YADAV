n1=int(input("Enter your 1st number", ))
n2=int(input("Enter your 2nd number", ))
print("from below list which operation you want to perform")
print("+")
print("-")
print("*")
print("/")
print("%")
op1=input("Enter what opretion you want to do",)
if op1=="+":
    s=n1+n2
    print("sum of ",n1,"&",n2,"=",s)
    for i in range(1,100):
        x=input("If you want to perform other opretion enter 1 otherwise enter other number")
        if x=="1":
            n3=int(input("Enter number" ))
            op2=input("Enter what opretion you want to do")
            print("+")
            print("-")
            print("*")
            print("/")
            print("%")
            if op2=="+": 
                
                print(s+n3)
            elif op2=="*":
                print(s*n3)
            elif op2=="/":
                print(s/n3)
            elif op2=="-":
                print(s-n3)
            else:
                break
    else:
        print("sum: ",n1+n2)
elif op1=="*":
    s=n1*n2
    for i in range(0,100):
        x=input("If you want to perform other opretion enter 1 otherwise enter other number", )
        if x=="1":
            n3=int(input("Enter number", ))
            op2=input("Enter what opretion you want to do")
            if op2=="+":
                print(s+n3)
            elif op2=="*":
                print(s*n3)
            elif op2=="/":
                print(s/n3)
            elif op2=="-":
                print(s-n3)
        else:
            print(n1*n2)
elif op1=="/":
    s=n1/n2
    for i in range(0,100):
        x=input("If you want to perform other opretion enter 1 otherwise enter any other number", )
        if x=="1":
            n3=int(input("Enter number", ))
            op2=input("Enter what opretion you want to do")
            if op2=="+":
                print(s+n3)
            elif op2=="*":
                print(s*n3)
            elif op2=="/":
                print(s/n3)
        elif op2=="-":
            print(s-n3)
    else:
        print(n1/n2)
elif op1=="-":
    s=n1-n2
    for i in range(1,100):
        x=input("If you want to perform other opretion enter 1 otherwise enter any other number", )
        if x=="1":
            n3=int(input("Enter number", ))
            op2=input("Enter what opretion you want to do")
            if op2=="+":
                print(s+n3)
            elif op2=="*":
                print(s*n3)
            elif op2=="/":
                print(s/n3)
            elif op2=="-":
                print(s-n3)
    else:
        print(n1-n2)