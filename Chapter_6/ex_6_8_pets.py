pets = {
    'milo': {
        'animal': 'dog',
        'owner': 'yash',
        'age': 'unknown',
        'city': 'ashburn'
        },

    'arlo': {
        'animal': 'dog',
        'owner': 'mahi',
        'age': 'unknown',
        'city': 'ashburn'
        },

    'ahbay bird': {
        'animal': 'bird',
        'owner': 'abhay',
        'age': 'unknown',
        'city': 'ashburn'
        },

    }

for animal, animal_info in pets.items():
    print(f"\n{animal.title()}'s information:")
    
    for key, info in animal_info.items():
        print(f"\t{key.title()} - {info.title()}")