class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

car1 = Car("Toyota", "Camry", 2022)
print(car1.get_make())   # Output: Toyota
print(car1.get_model())  # Output: Camry
print(car1.get_year())   # Output: 2022
