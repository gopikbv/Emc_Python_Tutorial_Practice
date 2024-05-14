#Polymorphism --> The same function name is being used for different types and the key
#difference is the data type and number of arguments used in function

def add(a,b,c=0):
    print(a+b+c)

add(10,20)
add(10,20,c=30)