class Vehicle:
    def rent(self, days):
        pass

class Bike(Vehicle):
    def rent(self, days):
        return days * 500

class Car(Vehicle):
    def rent(self, days):
        return days * 1500

b = Bike()
c = Car()

print("Bike Rent:", b.rent(3))
print("Car Rent:", c.rent(3))