print("Input two numbers, and I will add them together.\n")

first_number = input("First number: ") 
try:
    first_number = int(first_number)
except ValueError:
    print("That is not a number!")
else:
    second_number = input("Second number: ")
    try:
        second_number = int(second_number)
    except ValueError:
        print("That is not a number!")
    else:
        print(f"{first_number} + {second_number} = {first_number + second_number}")