salary=int(input("Enter your salary:"))
age=int(input("Enter your age:"))
if salary>=20000 or age<=25:
    amount=int(input("Enter your expected amount:"))
    if amount<=50000:
        print("Eligible for loan")
    else:
        print("Maximum loan amount is 50,000")
else:
    print("You are not eligible for loan")