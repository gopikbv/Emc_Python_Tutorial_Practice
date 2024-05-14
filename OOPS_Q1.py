class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=10
        b=20
        return l*b
    
pattern=rectangle()
print(pattern.area())

form=shape()
result=form.area()
print(result)