# Polymorphism -> Method overriding
class Animal():
    def sound(self):
        print("Animal makes sound")
class dog(Animal):
    def sound(self):
        print("Dog barks")
class Bird(Animal):
    def sound(self):
        print("Bird Sing")

Dog=dog()
Dog.sound()

bird=Bird()
bird.sound()