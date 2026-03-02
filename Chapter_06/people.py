person_1 = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York",    
}
person_2 = {
    "first_name": "Jane",
    "last_name": "Smith",
    "age": 25,
    "city": "Los Angeles",    
}
person_3 = {
    "first_name": "Alice",
    "last_name": "Johnson",
    "age": 28,
    "city": "Chicago",    
}
people = [person_1, person_2, person_3]
for person in people:
    print(f"{person['first_name']} {person['last_name']} is {person['age']} years old and lives in {person['city']}.")