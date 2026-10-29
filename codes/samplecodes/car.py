class Vehicle:
    color = "Thermalite Gray"
    def __init__(self, name, passengers):
        self.name = name
        self.passengers = passengers
    def move(self):
        print("Vehicle", self.color, self.name, "is moving.")
        print("It has", self.passengers, "passengers.")

class Car(Vehicle):
    def move(self):
        print("Car", self.color, self.name, "is moving on the road.")
        print("It has", self.passengers, "passengers.")

class Boat(Vehicle):
    def move(self):
        print("Boat", self.color, self.name, "is gliding through the water.")
        print("It has", self.passengers, "passengers.")

class Toilet:
    color = "brown"
    name = "Skibidi Toilet"
    passengers = 1
    def move(self):
        print("Toilet",self.color,self.name,"is flushing.")
        print("It has",self.passengers,"passengers. You.")

car = Car("Toyota Innova", 7)
car2 = Car("BYD Seal", 5)
car2.color = "Rainbow"
boat = Boat("Kayak", 3)
boat.color = "Black Super, Super Black"
toilet = Toilet()


vehicles = [car,car2,boat,toilet]
for i in vehicles:
    i.move()
