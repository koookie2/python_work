glossary = {
    '.append()': 'adds an element to a list',
    '.insert()': 'inserts an element into a certain location in a list',
    'del': 'deletes an element from a list',
    '.pop()': 'deletes an element from a list, but keeps that element stored as a variable',
    '.remove()': 'removes a value from a list',
    '.items()': 'assigns first variable the keys and second variable the values in for loop',
    '.keys()': 'assigns the variable in the for loop with the dictionary keys (redundant)',
    '.values()': 'assigns the variable in the for loop with the dictionary values',
    'set()': 'python builds a set using the first arguement',
    'range()': 'returns a sequence of numbers',
    }

for word, definition in glossary.items():
    print(f"{word}\n{definition}\n")