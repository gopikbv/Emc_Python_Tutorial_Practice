class dad():
    def money(self):
        print("Dad's Money")
class land():
    def important(self):
        print("Important land")

class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass

s1=son1()
s1.money()
s1.important()