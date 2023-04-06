sandwich_orders = ['Avocado BLT', 'Pastrami', 'Bacon Turkey Bravo', 'Pastrami', 'Frontega Chicken Sandwich', 'Pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.\n")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

for order in sandwich_orders:
    print(f"The {order} is ready!")

    finished_sandwiches.append(order)

print("\nI made these sandwiches:")
for i in finished_sandwiches:
    print(f" - {i}")