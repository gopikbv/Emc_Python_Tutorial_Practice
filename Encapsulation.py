class company():
    def __init__(self):
        self.__companyName="Google" # __ is used to make the variable private to the class
                                    #It is accessed only inside the class
        self._companyName="Google"  # _ is used to protect the variable
    def display(self):
        print(self.__companyName)
c1=company()
c1.display()
print(c1._companyName)

# _ is used to protect the variable,this variable can be accessed from the class and the derived class 
#which inherits the class as parent
class B(company):
    pass
b=B()
print(b._companyName)