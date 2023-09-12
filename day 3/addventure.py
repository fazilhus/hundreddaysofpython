"""
    khusn, 09.09.2023
    Adventure
"""

print("Very Fair Adventure\nversion 1.0.0\n")
print("Welcome to Treasure Island. Your quest is to find The Treasure.")
print("You see a crossroad. You may go left or right.")
choice = input().lower()

if choice == "right":
    print("You fall into a well-hidden spike trap.\nYou slowly bleed out.\nGame Over.")
    exit()
elif choice != "left":
    print("Your dumb brain decides that it is a good idea to wander off the road. You get lost in a nearby field(You are dumb, Haven't I said it already?)")
    print("You are bitten by field mouse.\nYou soon die of the Black Plague.\nGame over.")
    exit()

print("After walking down the road for a few hours you find yourself on a riverbank with a pier nearby.")
print("You could to wait for a boat at the pier or You could swim right across the river.")
choice = input().lower()

if choice == "swim":
    print("You are attacked by an overly aggressive shoal of trout.\nYou die.\nGame over.")
    exit()
elif choice != "wait":
    print("You decide to do neither. You wander off. You get lost.\You die of hunger.\nGame over.")
    exit()

print("On the other side of the river you see a house. You decide to explore it.")
print("You come inside the house and you see there three doors: red, yellow and blue.")
choice = input().lower()

if choice == "red":
    print("You walk inside the room behind the red door. Suddenly the door swings shut and violent fire starts.")
    print("You die of asphyxiation.\nGame Over")
elif choice == "yellow":
    print("You walk inside the room behind the yellow door.\nYou find a small, filthy chest filled with gold ingots made out of Lego.\nYou win(no).")
elif choice == "blue":
    print("You walk inside the room behind the blue door. You see an uncountable amount of parrots sitting all around the room.")
    print("They are apparently have a very cruel and dark sense of humor. They start mock you.\nYou die of embarrassment.\nGameOver.")
