"""A set of classes used to represent a restaurant."""

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cusine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the attributes of the restaurant."""
        print(f"The restuarant's name is {self.restaurant_name}.")
        print(f"The restuarant's cuisine is {self.cuisine_type}.")

    def open_restaurant(self):
        """Print that the restaurant is open."""
        print(f"The restaurant is open!")
    
    def number_of_served(self):
        """Print a statement showing the number of people the restaurant served."""
        print(f"This restaurant has served {self.number_served} people.")

    def set_number_served(self, number_served):
        """Set the number served to the given value."""
        self.number_served = number_served
    
    def increment_number_served(self, number_served):
        """Add the given amount to the number of people served."""
        self.number_served += number_served

class IceCreamStand(Restaurant):
    """A simple attempt to model an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print(f"This ice cream stand has the following flavors:")
        for flavor in self.flavors:
            print(f" - {flavor}")