# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

# Derived classes
class Car(Vehicle):
    def move(self):
        print("The car is driving on the road 🚗.")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky ✈️.")

class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on the water 🚤.")

# Test the polymorphism
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    vehicle.move()
