class laptop:
    
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("ram:",self.ram)
        print("processor:",self.processor)

hp=laptop()
dell=laptop()

hp.ram="4GB"
hp.processor="i3"

dell.ram="8GB"
dell.processor="i5"

print(hp.display())
print(dell.display())

