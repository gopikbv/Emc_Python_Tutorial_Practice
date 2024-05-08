#define class with variables and functions
class Goa:
    name=""
    drink=""
    def party(self):
        print("Let's do party.....")
    def beach(self):
        print("Let's Enjoy the Nature...")

#object creation
ramesh=Goa()
suresh=Goa()

#Access the Class variable:
ramesh.name="Ramesh"
print(ramesh.name)
suresh.name="Suresh"
print(suresh.name)

ramesh.drink="yes"
print("Drink:",ramesh.drink)
suresh.drink="no"
print("Drink:",suresh.drink)

#Access the function of the Class:
print(ramesh.party())
print(suresh.beach())