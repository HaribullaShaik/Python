from random import choice

class Lottery:
    def __init__(self):
        self.possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

    def draw_ticket(self):
        winning_ticket = []
        print("Let's see what the winning ticket is...")

        # We don't want to repeat winning numbers or letters, so we'll use a
        #   while loop.
        while len(winning_ticket) < 4:
            pulled_item = choice(self.possibilities)

            # Only add the pulled item to the winning ticket if it hasn't
            #   already been pulled.
            if pulled_item not in winning_ticket:
                print(f"  We pulled a {pulled_item}!")
                winning_ticket.append(pulled_item)

        print(f"\nThe final winning ticket is: {winning_ticket}")

lottery = Lottery()
lottery.draw_ticket()