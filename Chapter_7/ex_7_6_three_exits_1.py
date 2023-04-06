prompt = "\nPlease enter the pizza toppings you want:"
prompt += "\n(Enter 'quit' when you are finished.) "

toppings = ""

while toppings != 'quit':
    toppings = input(prompt)
    
    if toppings != 'quit':
        print(f"\nI'd love to eat a pizza with {toppings}")