class vehicle():
    def start(self):
        print("Vehicle started")
class car(vehicle):
    def start(self):
        print("Car started")
type=car()
type.start()

