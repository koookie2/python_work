# This is a revised version of "ex_6-7_people.py"

people = {
    'swarnim': {
        'first_name': 'swarnim',
        'last_name': 'bhatterai',
        'age': 15,
        'city': 'ashburn'
        },

    'sashi': {
        'first_name': 'sashi',
        'last_name': 'selamchela',
        'age': 14,
        'city': 'ashburn'
        },

    'anvitha': {
        'first_name': 'anvitha',
        'last_name': 'karnati',
        'age': 15,
        'city': 'ashburn'
        },

    }

for person, person_info in people.items():
    print(f"\n{person.title()}'s information:")
    
    for key, info in person_info.items():
        if info == str(info):
            print(f"\t{key.title()} - {info.title()}")
        else:
            print(f"\t{key.title()} - {info}")