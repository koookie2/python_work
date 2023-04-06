# LIST.append()   adds an elements
# LIST.insert()   inserts an element in a certain location
# del LIST   deletes an element from a list
# LIST.pop()   deletes an element from a list, but keeps that element stored as a variable
# LIST.remove()   removes a value from a list

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")