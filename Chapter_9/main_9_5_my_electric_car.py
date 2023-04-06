from main_9_2_car import ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_desriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()