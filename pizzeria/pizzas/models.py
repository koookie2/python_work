from django.db import models

class Pizza(models.Model):
    """ A model to represent a pizza."""
    name = models.TextField(default=None)
    # date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.name

class Topping(models.Model):
    """A model to represent a topping on the pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField(default=None)
    # date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return self.name