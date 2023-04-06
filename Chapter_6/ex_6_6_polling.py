favorite_languages = {
    'jen': 'python',
    'sophie': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

names = ['swarnim', 'sashi', 'anvitha', 'phil', 'ananya', 'edward']

for name in names:
    if name in favorite_languages:
        print(f"{name.title()}, thank you for taking the poll.")
    else:
        print(f"{name.title()}, please take the poll.")