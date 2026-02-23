users = {
    "John": {"first_name": "John", "last_name": "Doe", "age": 30},
    "Jane": {"first_name": "Jane", "last_name": "Smith", "age": 25},
    "Alice": {"first_name": "Alice", "last_name": "Johnson", "age": 28},
}
for username, details in users.items():
    print(f"username: {username}")
    full_name = f"{details['first_name']} {details['last_name']}"
    age = details['age']
    print(f"Full Name: {full_name}, Age: {age}")