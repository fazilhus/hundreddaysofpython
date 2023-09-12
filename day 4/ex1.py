from random import random

def heads_or_tails():
    return round(random())

heads = 0
tails = 0
for i in range(1000000):
    if heads_or_tails():
        heads += 1
    else:
        tails += 1
    
print(heads, tails)
