pizzas = ["pepperoni", "margherita", "hawaiian"]
friends_pizzas = pizzas[:]
pizzas.append("cheese")
friends_pizzas.append("veggie")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")
print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(f"- {pizza}")
