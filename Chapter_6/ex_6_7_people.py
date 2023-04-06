people = {
    'swarnim': {
        'first_name': 'swarnim',
        'last_name': 'bhatterai',
        'age': 'fifteen',
        'city': 'ashburn'
        },

    'sashi': {
        'first_name': 'sashi',
        'last_name': 'selamchela',
        'age': 'fourteen',
        'city': 'ashburn'
        },

    'anvitha': {
        'first_name': 'anvitha',
        'last_name': 'karnati',
        'age': 'fifteen',
        'city': 'ashburn'
        },

    }

for person, person_info in people.items():
    print(f"\n{person.title()}'s information:")
    
    for key, info in person_info.items():
        print(f"\t{key.title()} - {info.title()}")