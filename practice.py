available_toppings = ["pepperoni", "mushrooms", "onions", "sausage", "bacon"]
requested_toppings = ["mushrooms", "french fries", "extra cheese", "sausage"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")