class Car:
    # To count how many numbers of objects are created
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description(): # static method don't need self
        return "Cars are mode of transport"


    @property
    def model(self):
        return self.__model




# Inheriting Car properties
class Electric_car(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"
    
    
    

# electric_car = Electric_car("Tesla", "Model S", "85kWh")
# print(electric_car.model)
# print(electric_car.__brand) This will throws an error coz your now trying to access private attribute
# print(electric_car.full_name())
# print(electric_car.fuel_type())
# print(isinstance(electric_car, Electric_car))
# print(isinstance(electric_car, Car))


# my_car = Car("Range Rover", "Land Rover")
# my_car.model = "Jaguar"
# print(my_car.fuel_type())
# print(my_car.general_description())
# print(Car.general_description()) # This will only accessible iff method is static

# print(my_car.model) # This will work as a property but not like function coz of @property
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# Printing total_car created
# print(Car.total_car)



# Multiple Inheritance

class Battery:
    def battery_info(self):
        return "this is battery"


class Engine:
    def engine_info(self):
        return "this is engine"


class Electric_car_two(Battery, Engine, Car):
    pass

my_new_tesla = Electric_car_two("Telsa", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())