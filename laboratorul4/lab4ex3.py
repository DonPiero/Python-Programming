class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculateMileage(self):
        return self.mileage

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculateMileage(self):
        return self.mileage

class Truck(Vehicle):
    def __init__(self, make, model, year, towingCapacity):
        super().__init__(make, model, year)
        self.towingCapacity = towingCapacity

    def calculateTowingCapacity(self):
        return self.towingCapacity

car = Car("Toyota", "Supra", 2018, 30000)
motorcycle = Motorcycle("Barton", "Blade", 2021, 4000)
truck = Truck("Ford", "Raptor", 2015, 20000)

carMileage = car.calculateMileage()
motorcycleMileage = motorcycle.calculateMileage()
truckTowingCapacity = truck.calculateTowingCapacity()

print(f"Car Mileage: {carMileage} MPG.")
print(f"Motorcycle Mileage: {motorcycleMileage} MPG.")
print(f"Truck Towing Capacity: {truckTowingCapacity} LBS.")
