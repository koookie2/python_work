"""A set of classes that can be used to represent electric cars."""

from main_9_2_car import Car

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initailize the attributes of the Battery class."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """A simple attempt to model an electric car."""

    def __init__(self, make, model, year):
        """
        Initialize then attributes of the Car class.
        Then initialize the attributes specific to the ElectricCar class.
        """
        super().__init__(make, model, year)
        self.battery = Battery()