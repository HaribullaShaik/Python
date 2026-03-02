prompt = "What is your age? "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    age = input(prompt)
    if age == 'quit':
        message = 'quit'
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")