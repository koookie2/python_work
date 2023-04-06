"""A class used to represent a car."""

class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize the attributes of the Car class."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_desriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} mile on it.")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading.
        Reject the change if it attempts to roll the odometer back.
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")