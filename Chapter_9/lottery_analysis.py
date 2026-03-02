from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

my_ticket = [1, 3, 'a', 'd']
print("Let's see what the winning ticket is...")

counter = 0
max_iterations = 10000
while True:
    counter += 1
    winning_ticket = []
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    print(f"\nThe winning ticket is: {winning_ticket}")
    if winning_ticket == my_ticket:
        print("Congratulations! You win the lottery!")
        print(f"The while loop was executed {counter} times.")
        break
    else:
        print("Sorry, you didn't win. Try again!")
    if counter >= max_iterations:
        print(f"Sorry, you didn't win after {counter} iterations. Better luck next time!")
        break  