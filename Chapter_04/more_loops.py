foods = ["pizza", "burger", "taco", "salad"]
my_friends_foods = foods[:]
foods.append("pasta")
my_friends_foods.append("sushi")
print("my favorite foods are:")
for food in foods:
    print(f"- {food}")
print("\nmy friend's favorite foods are:")
for food in my_friends_foods:
    print(f"- {food}")
