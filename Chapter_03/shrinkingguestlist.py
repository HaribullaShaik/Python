people = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]
print("I can only invite two people to the party.")
people.pop()  # Remove the last person
people.pop()  # Remove the second last person
people.pop()  # Remove the third last person
people.pop()  # Remove the fourth last person
people.pop()  # Remove the fifth last person
people.pop()  # Remove the sixth last person
people.pop()  # Remove the seventh last person
people.pop()  # Remove the eighth last person
print(f"You are still invited to the party, {people[0].title()}!")
print(f"You are still invited to the party, {people[1].title()}!")
del people[0]  # Remove the first person
del people[0]  # Remove the second person
print(people)  # This should print an empty list