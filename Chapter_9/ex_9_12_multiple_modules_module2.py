"""A set of classes used to represent an admin user."""

from ex_9_12_multiple_modules_module1 import User

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