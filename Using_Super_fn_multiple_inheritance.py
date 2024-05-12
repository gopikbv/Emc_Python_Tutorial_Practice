class A():
    def __init__(self):
        print("A")
    def display(self):
        print("Inside Class A")

# super() is used to access the methods from a parent class within a child class:
class B():
    def __init__(self):
        super().__init__()
        print("B")
        
    def display(self):
        print("Inside Class B")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("C")
        
    def display(self):
        print("Inside Class C")

obj=C()