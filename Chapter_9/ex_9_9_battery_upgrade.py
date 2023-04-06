class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize name and age attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_desriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make.title()} {self.model.title()}"
        return long_name
    
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

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initailize the battery's attributes"""
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
    
    def upgrade_battery(self):
        """Set's the battery size to 65."""
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Represent aspects of an electric car."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_car = ElectricCar('tesla', 'model 3', 2018)
my_car.battery.get_range()
my_car.battery.upgrade_battery()
my_car.battery.get_range()