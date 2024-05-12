class phone():
    #self keyword refers to the object that are created using the class:
    def __init__(self,brand,price,chargerType):
        #Instance variables are defined under constructor:
        self.brand=brand
        self.price=price
        self.chargerType=chargerType
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("chargerType:",self.chargerType)

# values for Instance variables are passed as arguments while object creation
samsung=phone("Samsung","10000","B-Type")
#calling the Instance function:
samsung.display()
print()   
#creating another object for the class phone:
redmi=phone("Redmi","5000","C-Type")
redmi.display()