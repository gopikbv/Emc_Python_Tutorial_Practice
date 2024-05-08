class student:
    def __init__(self):
        self.name="Neo"
        self.reg_no=11301
    def display(self):
        print("Name:",self.name)
        print("Reg_No",self.reg_no)
    
#creating object for the class:
s1=student()
s2=student()

#Assigning value to the variable with respect to their object
s1.name="Neo"
s1.reg_no=11301
s1.display()

s2.name="Thor"
s2.reg_no=11302
s2.display()