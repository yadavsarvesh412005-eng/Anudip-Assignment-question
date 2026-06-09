# 6. Car class and sort by mileage

class Car:
    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

def sort_cars(cars):
    return sorted(cars, key=lambda c: c.mileage)

c1 = Car("BMW", 15)
c2 = Car("Swift", 25)
c3 = Car("Audi", 18)

for car in sort_cars([c1, c2, c3]):
    print(car.name, car.mileage)