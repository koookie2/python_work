from django.shortcuts import render

from .models import Pizza

def index(request):
    """The home page for pizzas."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Page listing all pizzas."""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def toppings(request, pizza_id):
    """Show a single topic and all its entries."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/toppings.html', context)