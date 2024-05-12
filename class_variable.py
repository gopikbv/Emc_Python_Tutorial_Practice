class phone():
    #Class Variable ---> This variable is used to represent the common thing of the class
    chargerType="C_Type"
    #self keyword refers to the object that are created using the class:
    def __init__(self,brand,price):
        #Instance variables are defined under constructor:
        # This variable is used when the attributes of the class points has multiple parameters to define
        self.brand=brand
        self.price=price
        
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("chargerType:",self.chargerType)

# values for Instance variables are passed as arguments while object creation
samsung=phone("Samsung","10000")
#calling the Instance function:
samsung.display()
print()   
#creating another object for the class phone:
redmi=phone("Redmi","5000")
redmi.display()
print() 

#creating another object for the class phone:
google=phone("Pixel","5000")
google.display()
print() 
#To modify the class variable:
phone.chargerType="B-Type"
samsung.display()
print() 
redmi.display()
print() 
google.display()
