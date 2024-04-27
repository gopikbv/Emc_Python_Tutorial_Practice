mark=int(input("Enter the mark:"))
if (mark<35):
    print("Poor student")
elif(mark>=35) and (mark<70):
    print("Average student")
elif(mark>=70) and (mark<=100):
    print("good student")
else:
    print("Invalid Input")