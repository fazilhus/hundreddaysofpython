"""
    khusn, 09.09.2023
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

pizza_size = {"S":15, "M":20, "L":25}

cost = pizza_size[size]

if add_pepperoni == "Y":
    if size == "S":
        cost += 2
    else:
        cost += 3

if extra_cheese == "Y":
    cost += 1

print(f"Your final bill is: ${cost}.")