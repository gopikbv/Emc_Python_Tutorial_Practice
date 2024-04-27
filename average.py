Tamil=int(input("Enter Mark:"))
eng=int(input("Enter Mark:"))
maths=int(input("Enter Mark:"))
science=int(input("Enter Mark:"))
social=int(input("Enter Mark:"))
result=Tamil+eng+maths+science+social
average=result/5
if(average<35):
    print("Additional Class is required")
else:
    print("you are good to go")