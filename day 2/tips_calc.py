"""
    khusn, 09.09.2023
    Tip Calculator
"""

print("Tip Calculator\nversion 1.0.0\n")
print("What was the total bill?", end=" ")
bill = float(input())

print("Between hom many people the bill should be split?", end=" ")
num_people = int(input())

print("What is the tip?", end=" ")
tip = int(input())

cost = (bill / num_people) * (1 + tip / 100)
print(f"{cost:.2f}$ is the total per person.")