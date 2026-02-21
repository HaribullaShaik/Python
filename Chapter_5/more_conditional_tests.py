car = "subaru"
print(car == "subaru")
print(car == "audi")
print(car != "audi")
print(car != "subaru")
car = "Audi"
print(car.lower() == "audi")
print(car)
age_0 = 22
age_1 = 18
print(age_0 >= 21)
print(age_1 >= 21)
if age_0 >= 21:
    print("You are old enough to drink!")
else:
    print("You are not old enough to drink.")

if age_1 >= 21 and age_0 >= 21:
    print("You are both old enough to drink!")
else:
    print("One or both of you are not old enough to drink.")

if age_1 >= 21 or age_0 >= 21:
    print("At least one of you is old enough to drink!")
else:
    print("Neither of you are old enough to drink.")

add_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in add_toppings:
    print("Adding mushrooms.")
if "pepperoni" in add_toppings:
    print("Adding pepperoni.")
if "extra cheese" in add_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

add_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" not in add_toppings:
    print("Mushrooms are not in the pizza toppings list.")
else:
    print("Mushrooms are in the pizza toppings list.")