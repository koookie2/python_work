class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cusine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the attributes of the restaurant."""
        print(f"The restuarant's name is {self.restaurant_name}.")
        print(f"The restuarant's cuisine is {self.cuisine_type}.")

    def open_restaurant(self):
        """Print that the restaurant is open."""
        print(f"The restaurant is open!")

restaurant = Restaurant('Chipotle', 'Mexican Grill')


print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()