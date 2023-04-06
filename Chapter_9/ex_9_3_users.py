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

user1 = User('kavin', 'wesley', '01/03/2008', 15, 5040, 'male')
user1.describe_user()
user1.greet_user()

user2 = User('godwin', 'babu', '06/25/1972', 50, 0, 'male')
user2.describe_user()
user2.greet_user()

user3 = User('joy', 'wesley', '11/01/1973', 49, 1, 'female')
user3.describe_user()
user3.greet_user()

user4 = User('nila', 'wesley', '08/01/2010', 12, 2, 'female')
user4.describe_user()
user4.greet_user()