# Kavin Wesley
# 2/27/2023
# This program stores a name that contains "\n" and "\t" into a variable, then prints that variable with no changes, no spaces to the right, no spaces to the left, and no spaces to either side

name = "  Kavin\n\tWesley  "
print(f".{name}.")
print(f".{name.lstrip()}.")
print(f".{name.rstrip()}.")
print(f".{name.strip()}.")