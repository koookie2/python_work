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

class Privileges:
    """A simple attempt to model the privileges of a user."""

    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        """Print a statement showing the user's privileges."""
        print(f"These are their privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")

class Admin(User):
    """A simple attempt to model a type of user known as an admin."""

    def __init__(self, first_name, last_name, birthday, age, favorite_number, gender, *privileges):
        """
        Initialize attributes of the User class.
        Then initialize attributes specific the Admin class.
        """
        super().__init__(first_name, last_name, birthday, age, favorite_number, gender)
        self.privileges = Privileges(privileges)

admin = Admin('kavin', 'wesley', '01/03/2008', 15, 5040, 'male', 'can add post', 'can delete post', 'can ban user')
admin.privileges.show_privileges()