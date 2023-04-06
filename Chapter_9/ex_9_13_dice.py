from random import randint

class Die:
    """A simple model of a die"""

    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        """Print a random side number."""
        side_facing_up = randint(1,self.sides)
        print(f"The die is rolled and side {side_facing_up} faces up.")

six_sided_die = Die(6)
for i in range(10):
    six_sided_die.roll_die()

ten_sided_die = Die(10)
for i in range(10):
    ten_sided_die.roll_die()

twelve_sided_die = Die(12)
for i in range(10):
    twelve_sided_die.roll_die()