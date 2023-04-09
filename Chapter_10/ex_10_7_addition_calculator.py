def check(ordinal):
    """
    Asks the user for input until the input is numerical.
    Returns the input.
    """
    while True:
        number = input(f"{ordinal} number: ")
        try:
            number = int(number)
        except ValueError:
            if number == 'q':
                quit()
        else:
            return number


print("Input two numbers, and I will add them together.")
print("enter \"q\" to quit the program\n")

while True:
    first_number = check("First", )
    second_number = check("Second")
    print(f"{first_number} + {second_number} = {first_number + second_number}")