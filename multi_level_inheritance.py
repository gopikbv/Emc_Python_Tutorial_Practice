class grandpa():
    def phone(self):
        print("grandpa's Phone")
        
#Inherit the class GRANDPA in DAD:
class dad(grandpa):
    def money(self):
        print("Dad's Money")

#Inherit the class DAD in SON:
class son(dad):
    def laptop(self):
        print("Son's laptop")

ram=son()
ram.laptop()
ram.money()

d1=dad()
d1.phone()
ram.phone()