people = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
print("We found a bigger table, so we can invite more people!")
people.insert(0, "Karl")
people.insert(5, "Leo")
people.append("Mallory")
print(f"You are invited to the party, {people[0].title()}, {people[1].title()}, {people[2].title()}, {people[3].title()}, {people[4].title()}, {people[5].title()}, {people[6].title()}, {people[7].title()}, {people[8].title()}, {people[9].title()}, {people[10].title()}, {people[11].title()}, and {people[12].title()}!")