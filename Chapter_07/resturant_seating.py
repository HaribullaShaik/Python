prompt = input("How many people are in the group? ")
people = int(prompt)
if people > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")