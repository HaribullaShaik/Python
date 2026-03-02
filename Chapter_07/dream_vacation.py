responses = {}
polling_status = True
while polling_status:
    vacation = input("\nWhere would you like to go on vacation? ")
    responses[vacation] = input(f"if you could visit one place in the {vacation}, where would you go? ")
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_status = False
print("\n--- Poll Results ---")
for vacation, response in responses.items():
    print(f"{vacation}: {response}")