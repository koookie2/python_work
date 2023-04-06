cities = {
    'chicago': {
        'country': 'US',
        'population': '2.7 million',
        'fact': 'It is the third largest city in the US',
        },

    'houston': {
        'country': 'US',
        'population': '2.3 million',
        'fact': '145 languages are spoken in it',
        },

    'philadelphia': {
        'country': 'US',
        'population': '1.6 million',
        'fact': 'It has the oldest inhabited road in the US',
        },

    }

for city, city_info in cities.items():
    print(f"\n{city.title()}'s information:")
    
    for key, info in city_info.items():
        print(f"\t{key.title()} - {info}")