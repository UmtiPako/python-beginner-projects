import random


def rollTheDice(): # Creating a function to roll the dice anytime we want.
    diceRoll = random.randint(1,6) # the outcome of diceroll will be chosen randomly 
    return diceRoll # we return the outcome


input("Press enter to roll the die.") # Taking enter input:
print(rollTheDice()) # printing the outcome by calling the rollthedice function.


