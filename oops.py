# Inheritance - getting properties of parent
# Encapsulation - hides specific attributes from being accessed
# Polymorphism -
# Abstraction -


class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def display(self):
        return f"Car Brand: {self.__brand}, Model: {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_desc():
        return "this is a static general description"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Toyota", "Corolla")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

# print(Car.general_desc())


class Battery:
    pass


class Engine:
    pass


class ElectricCarTwo(Battery, Engine, Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla", "Model S")
