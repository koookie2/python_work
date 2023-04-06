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
        self.login_attempts = 0

    def describe_user(self):
        """Prints the attributes of the user."""
        print(f"\n{self.first_name.title()} {self.last_name.title()}")
        print(f" - first name: {self.first_name}")
        print(f" - last name: {self.last_name}")
        print(f" - birthday: {self.birthday}")
        print(f" - age: {self.age}")
        print(f" - favorite number: {self.favorite_number}")
        print(f" - gender: {self.gender}")
        print(f" - login attempts: {self.login_attempts}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hi {self.first_name.title()} {self.last_name.title()}!")
    
    def number_of_login_attempts(self):
        """Prints a statement showing the number of this user's login attempts."""
        print(f"This user has tried to login {self.login_attempts} times!")

    def increment_login_attempts(self):
        """Increments the number of login attempts by 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Resets the number of login attempts to 0."""
        self.login_attempts = 0

user = User('kavin', 'wesley', '01/03/2008', 15, 5040, 'male')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.number_of_login_attempts()

user.reset_login_attempts()

user.number_of_login_attempts()