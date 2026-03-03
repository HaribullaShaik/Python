while True:
    try:
        number_1 = int(input("Enter the first number: "))
        number_2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    else:
        result = number_1 + number_2
        print(f"The sum of {number_1} and {number_2} is: {result}")
        break