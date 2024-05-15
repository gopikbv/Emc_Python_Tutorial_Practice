#Types of error
#compile time error-> syntax error
#logical error-> the logic is wrongly defined in the code
#Run time Error -> The program is successfully compiled and the error is occured during the runtime
#Run time Error is handled by try and exception handling in python
try:
    a=int(input())
    b=int(input())
    print(a+b)
#except Exception:
    #print("Something Fishy")
#To capture the error definition:
except Exception as e:
    print(e)