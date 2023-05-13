class Car:
    def __init__(self, brand, model, year, cost):
        self.brand = brand
        self.model = model
        self.year = year
        self.cost = cost

    def info(self):
        print(self.brand, self.model, self.year, self.cost)


my_car = Car("Toyota", "Supra(А80)", 1996, 4444444)
my_car.info()