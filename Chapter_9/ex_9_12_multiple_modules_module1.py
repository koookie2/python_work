"""A class used to represent a user."""

class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, birthday, age, favorite_number, gender):
        """Initialize user_name and cusine_type attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.age = age
        self.favorite_number = favorite_number
        self.gender = gender

    def describe_user(self):
        """Prints the attributes of the user."""
        print(f"\nThe attributes of {self.first_name.title()} {self.last_name.title()}:")
        print(f" - first name: {self.first_name}")
        print(f" - last name: {self.last_name}")
        print(f" - birthday: {self.birthday}")
        print(f" - age: {self.age}")
        print(f" - favorite number: {self.favorite_number}")
        print(f" - gender: {self.gender}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hi {self.first_name.title()} {self.last_name.title()}!")