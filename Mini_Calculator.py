a=int(input("Enter the value of A:"))
b=int(input("Enter the value of B:"))
operation= input("Enter +/-/*//:")
if(operation=='+'):
    print("The sum is:",a+b)
elif(operation =="-"):
    print("The difference is:",a-b)
elif(operation =="*"):
    print("The Mul is:",a*b)
elif(operation =="/"):
    print("The Div is:",a/b)
else:
    print("Invalid Operation")
