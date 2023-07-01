from example1 import Car

class ElectricCar(Car):  # ElectricCar inherits from Car
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def get_battery_capacity(self):
        return self.battery_capacity

electric_car1 = ElectricCar("Tesla", "Model S", 2022, "100 kWh")
print(electric_car1.get_make())              # Output: Tesla (inherited from Car)
print(electric_car1.get_model())             # Output: Model S (inherited from Car)
print(electric_car1.get_year())              # Output: 2022 (inherited from Car)
print(electric_car1.get_battery_capacity())  # Output: 100 kWh
