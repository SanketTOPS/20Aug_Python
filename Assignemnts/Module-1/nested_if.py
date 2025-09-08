a=int(input("Enter A:"))
b=int(input("Enter B:"))

if a!=0 and b!=0: #parent - root
    if a>b: #child
        print("Sum:",a+b)
    else:
        print("Mul:",a*b)
else:
    print("Error!")

    

