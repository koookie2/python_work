# .get()   if the first arguement is not in the dictionary, then the program will assign it the second arguement

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)