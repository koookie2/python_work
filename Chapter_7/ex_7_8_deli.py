sandwich_orders = ['Avocado BLT', 'Bacon Turkey Bravo', 'Frontega Chicken Sandwich']
finished_sandwiches = []

for order in sandwich_orders:
    print(f"The {order} is ready!")

    finished_sandwiches.append(order)

print("\nI made these sandwiches:")
for i in finished_sandwiches:
    print(f" - {i}")