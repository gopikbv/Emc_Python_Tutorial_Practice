mark=int(input("Enter Mark:"))
def pass_fail(val):
    if(mark>=35) and (mark<=100):
        print("pass")
    else:
        print("Fail")
pass_fail(mark)