choices = ["rock", "paper", "scissors"]
codes = {"rock": 0, "paper": 2, "scissors": 1}

from random import choice

print("Rock Paper Scissors\nversion 1.0.0")

players_choice = input("To start choose 'rock', 'paper' or 'scissors': ")

if not players_choice in codes.keys():
    print("Wrong input.")
    exit()

pl_c = codes[players_choice]
pc_c = codes[choice(choices)]

print(pl_c, pc_c)

if (pl_c + 1) % 3 == pc_c:
    print("You win!")
elif pl_c == (pc_c + 1) % 3:
    print("You lose")
else:
    print("It's a draw")
