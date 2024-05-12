""" In python the class has the following methods or functions are used
    1).Instance Method
    2).Class Method
    3).static Method
""" 
class laptop():
    #class variable:
    chargerType="C-Type"
    def __init__(self):
        #Instance Variable:
        self.brand=""
        self.price=34000
    # Instance Method-> The parameter self points to the object of the class
    def setPrice(self,price):
        self.price=price
    def getPrice(self):
        print(self.price)
    
    #class Method:
    """def changeChargerType(cls):
        cls.chargerType="B Type"
        print("charger Type changed from C to B")"""
    
    #using Decrators:
    @classmethod
    def changeChargerType(cls):
        cls.chargerType="B Type"
        print("charger Type changed from C to B")

    #static method doesn't use the Class parameters:
    @staticmethod
    def info():
        print("This is Laptop class")


hp=laptop()
hp.getPrice()

hp.setPrice(40000)
hp.getPrice()

#class Method call
#laptop.changeChargerType(laptop)
laptop.changeChargerType()

# static method call:
hp.info()