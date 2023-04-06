vacations = {}

polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where is your dream vacation location? ")

    vacations[name] = response

    if input("Would you like to let another person respond (yes/no) ") == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in vacations.items():
    print(f"{name.title()} would like to visit {response.title()}.")