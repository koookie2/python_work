prompt = "\nPlease enter your age: "

while True:
    age = int(input(prompt))
    
    if age < 3:
        cost = 0
    elif age < 13:
        cost = 10
    else:
        cost = 15
    
    print(f"Your ticket costs {cost} dollars.")