from name_function import get_username

print("q to quit at any time.")
while True:
    first_name = input("Enter your first name: ")
    if first_name == 'q':
        break
    last_name = input("Enter your last name: ")
    if last_name == 'q':
        break
    print(get_username(first_name, last_name))