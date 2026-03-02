pet_1 = {
    "owner": "Alice",
    "name": "Whiskers",
    "age": 3,
    "color": "tabby",
    "species": "cat"
}
pet_2 = {
    "owner": "Bob",
    "name": "Rover",
    "age": 5,
    "color": "brown",
    "species": "dog"
}
pet_3 = {
    "owner": "Charlie",
    "name": "Tweety",
    "age": 2,
    "color": "yellow",
    "species": "bird"
}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print(f"{pet['owner']} has a {pet['color']} {pet['species']} "
          f"named {pet['name']} who is {pet['age']} years old.")