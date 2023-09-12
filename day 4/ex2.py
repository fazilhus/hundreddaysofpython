from random import choice

names = input("Give me everybody's names, separated by a comma. ").split(",")

name = choice(names)
print(name, "is going to buy the meal today!")