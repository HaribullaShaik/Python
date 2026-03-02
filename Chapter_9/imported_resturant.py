from number_served import Resturant
resturant = Resturant("Pasta Palace", "Italian")
resturant.describe_restaurant()
resturant.set_number_served(50)
print(f"Number of customers served: {resturant.number_served}")
resturant.increment_number_served(20)
print(f"Number of customers served in one day of business: {resturant.number_served}")