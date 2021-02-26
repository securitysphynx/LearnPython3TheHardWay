user_total_clients = int(input("How many endpoints do you have? "))
user_neighborhood_size = int(input("How large can your neighborhood be? "))

def num_of_neighborhoods(total_clients, neighborhood_size):
    return total_clients/neighborhood_size

#print(f"You will have {num_of_neighborhoods(1000,20)} neighborhoods")
print(f"You will have {int(num_of_neighborhoods(user_total_clients, user_neighborhood_size))} neighborhoods.")
