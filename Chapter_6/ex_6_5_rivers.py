rivers = {
    'amazon river': 'brazil',
    'nile river': 'egypt',
    'yellow river': 'china',
    }

for river, location in rivers.items():
    print(f"The {river.title()} runs through {location.title()}.")
print()

for river in rivers.values():
    print(river.title())
print()

for location in rivers:
    print(location.title())