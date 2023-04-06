from random import sample

LOTTERY_NUMBERS = 26, 63, 98, 74, 25, 23, 66, 76, 95, 85, 'm', 'f', 'e', 'r', 'p'
MY_TICKET = 74

winning_number = sample(LOTTERY_NUMBERS, 4)
number_of_attempts = 1

while MY_TICKET in winning_number:
    number_of_attempts += 1
    winning_number = sample(LOTTERY_NUMBERS, 4)

print(f"It took {number_of_attempts} attempts to win.")