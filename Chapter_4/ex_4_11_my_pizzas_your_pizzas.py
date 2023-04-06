pizza_toppings = ["pepperoni", "sausage", "olive"]
for i in pizza_toppings:
    print(f"I like {i} pizza")
print("\nI really love pizza!")

friend_pizzas = pizza_toppings[:]
pizza_toppings.append("chicken")
friend_pizzas.append("mushroom")

print("\nMy favorite pizzas are:")
for i in pizza_toppings:
    print(i)
print("\nMy friend's favorite pizzas are:")
for i in friend_pizzas:
    print(i)