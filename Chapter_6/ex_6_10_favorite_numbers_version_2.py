favorite_numbers = {
    'dad': [0,11],
    'mom': [1,60],
    'nila': [2,12],
    'kavin': [3,5040],
    'sashi': [8,9],
    }

for person, fav_numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are {fav_numbers[0]} and {fav_numbers[1]}.")