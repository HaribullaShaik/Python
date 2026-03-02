favorite_number = {
    "Alice": 7,
    "Bob": 42,
    "Charlie": 3.14,
}
print(f"Alice's favorite number is {favorite_number['Alice']}.")
print(f"Bob's favorite number is {favorite_number['Bob']}.")
print(f"Charlie's favorite number is {favorite_number['Charlie']}.")

favorite_number["David"] = 100
print(f"David's favorite number is {favorite_number['David']}.")