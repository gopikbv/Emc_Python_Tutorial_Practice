# A class have access to use attributes of more than one class
class dad():
    def phone(self):
        print("Dad's Phone")
        
class mom():
    def sweet(self):
        print("Mom's sweet")

#Inherit the class DAD & Class MOM in SON:
class son(dad,mom):
    def laptop(self):
        print("Son's laptop")

ram=son()
ram.laptop()
ram.phone()
ram.sweet()