favorite_number = {
    "Alice": [7, 14],
    "Bob": [42, 84],
    "Charlie": [3.14, 6.28],
}
for name, numbers in favorite_number.items():
    print(f"{name}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")
