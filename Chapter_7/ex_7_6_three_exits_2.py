prompt = "\nPlease enter the pizza toppings you want:"
prompt += "\n(Enter 'quit' when you are finished.) "

active = True

while active:
    toppings = input(prompt)
    
    if toppings == 'quit':
        active = False
    else:
        print(f"\nI'd love to eat a pizza with {toppings}")