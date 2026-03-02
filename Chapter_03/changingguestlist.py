people = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(f"You are invited to the party, {people[0].title()}, {people[1].title()}, {people[2].title()}, and {people[3].title()}!")
print(f"Unfortunately, {people[3].title()} can't make it to the party.")
people[3] = "Frank"
print(f"Let's invite {people[3].title()} instead.")
print(f"You are invited to the party, {people[0].title()}, {people[1].title()}, {people[2].title()}, and {people[3].title()}!")
