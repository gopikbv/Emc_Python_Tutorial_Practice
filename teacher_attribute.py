class teacher:
    def __init__(self,r1,r2):
        self.name=r1
        self.reg_no=r2
    def display(self):
        print("Name:",self.name)
        print("Reg_no:",self.reg_no)

t1=teacher("Neo",11301)
t2=teacher("Thor",11302)

t1.display()
t2.display()
