from random import sample

LOTTERY_NUMBERS = 26, 63, 98, 74, 25, 23, 66, 76, 95, 85, 'm', 'f', 'e', 'r', 'p'

winning_numbers = sample(LOTTERY_NUMBERS, 4)

print(f"The winning numbers are {winning_numbers[0]}, {winning_numbers[1]}, {winning_numbers[2]}, and {winning_numbers[3]}.")
print(f"If you possess a ticket matching any of these 4 numbers, you have won 1000 dollars!")