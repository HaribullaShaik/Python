active = True
while active:
    message = input("Movie ticket prices are based on age. What is your age? ")
    if message == 'quit':
        break
    else:
        age = int(message)
        if age < 3:
            print("Your ticket is free!")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")