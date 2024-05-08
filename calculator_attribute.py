"""
class calci:
    def __init__(self,n1,n2):  #with constructor
        self.a=n1
        self.b=n2
    def add(self):
        print("sum:",self.a+self.b)
    def sub(self):
        print("sub:",self.a-self.b)
    def mul(self):
        print("mul:",self.a*self.b)
    def div(self):
        print("div:",self.a/self.b)

result=calci(40,20)
result.add()
result.sub()
result.mul()
result.div()
"""

#without constructor passing value to the arguments in the function inside the class:
class calci:
    def add(self,n1,n2):
        print("sum:",n1+n2)
    def sub(self,n1,n2):
        print("sub:",n1-n2)
    def mul(self,n1,n2):
        print("mul:",n1*n2)
    def div(self,n1,n2):
        print("div:",n1/n2)

obj1=calci()
obj1.add(20,10)
obj1.sub(20,10)    
obj1.mul(20,10)
obj1.div(20,10)