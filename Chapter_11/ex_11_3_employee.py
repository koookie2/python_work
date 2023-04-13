class Employee:
    """A simple attempt to model an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initailize the attributes of the Employee class."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Increase the salary by 'amount'."""
        self.annual_salary += amount
        print(self.annual_salary)