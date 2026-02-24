prompt = "Please enter the name of a pizza topping you want to add:"
prompt += "\nEnter 'quit' when you are finished. "
message = ""
while message != 'quit':
    toppings = input(prompt)
    if toppings == 'quit':
        message = 'quit'
    else:
        print(f"We will add {toppings} to your pizza.")