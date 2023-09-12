"""
    khusn, 09.09.2023
"""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

true = {"t":0, "r":0, "u":0, "e":0}
love = {"l":0, "o":0, "v":0, "e":0}

for c in name1:
    if c in true.keys():
        true[c] += 1
    if c in love.keys():
        love[c] += 1

for c in name2:
    if c in true.keys():
        true[c] += 1
    if c in love.keys():
        love[c] += 1

sum_true = sum(true.values())
sum_love = sum(love.values())

number = sum_true * 10 + sum_love

if number < 10 or number > 90:
    print(f"Your score is {number}, you go together like coke and mentos.")
elif 40 < number or number < 50:
    print(f"Your score is {number}, you are alright together.")
else:
    print(f"Your score is {number}.")
