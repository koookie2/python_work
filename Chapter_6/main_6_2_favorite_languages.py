# DICT.items()   assigns first variable the keys and second variable the values in for loop
# DICT.keys()   assigns the variable in the for loop with the dictionary keys (redundant)
# DICT.values()   assigns the variable in the for loop with the dictionary values
# set(ANY)   python builds a set using the first arguement; sets are lists that only contain unique elements
# sets also use curly brackets, but they don't have the key-value pairs dictionaries have

favorite_languages = {
    'jen': ['python', 'rust'],
    'sophie': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")