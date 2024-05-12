class dad():
    def phone(self):
        print("Dad's Phone")
#Inherit the class DAD from Class SON
class son(dad):
    def laptop(self):
        print("Son's laptop")

ram=son()
ram.laptop()
ram.phone()