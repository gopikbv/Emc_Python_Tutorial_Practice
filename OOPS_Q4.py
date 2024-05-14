class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(Employee):
    def __init__(self,name,salary,dep):
        super().__init__(name,salary)
        self.dep=dep
    def display(self):
        print(self.name,self.salary,self.dep)

e1=manager("John","10000","Ece")
e1.display()
        