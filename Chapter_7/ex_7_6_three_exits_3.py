prompt = "\nPlease enter the pizza toppings you want:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    toppings = input(prompt)
    
    if toppings == 'quit':
        break
    else:
        print(f"\nI'd love to eat a pizza with {toppings}")