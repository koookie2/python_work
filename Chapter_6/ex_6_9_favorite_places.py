favorite_places = {
    'swarnim': ['athens', 'baltimore'],
    'sashi': ['berlin', 'new york'],
    'anvitha': ['antartica', 'cheesequake']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()}, what are your favorite places?")
    print(f"\tMy favorite places are {places[0].title()} and {places[1].title()}.")