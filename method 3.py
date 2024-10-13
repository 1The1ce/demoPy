class Car:
    def __init__(self, make, fuel_level=0):
        self.__make = make
        self.__fuel_level = fuel_level

    def add_fuel(self, amount):
        if amount > 0:
            self.__fuel_level += amount
        else:
            print("Invalid fuel amount")

    def drive(self, distance):
        fuel_needed = distance / 10  # Assume 1 unit of fuel covers 10 units of distance
        if self.__fuel_level >= fuel_needed:
            self.__fuel_level -= fuel_needed
            print(f"You drove {distance} units.")
        else:
            print("Not enough fuel to drive the distance")

    def get_fuel_level(self):
        return self.__fuel_level

# Example usage
car = Car("Toyota")
car.add_fuel(50)
car.drive(100)   # Output: You drove 100 units.
print(car.get_fuel_level())  # Output: 40.0

car.drive(500)   # Output: Not enough fuel to drive the distance
print(car.get_fuel_level())  # Output: 40.0
