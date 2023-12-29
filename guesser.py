import random # Importing random module.

def playGuesserGame(): # I created a function to play the game by calling it.
    randNum = random.randint(1,100) # Choosing the number we have to guess randomly.
    guessing = True # This boolean will be used as a rule for our while loop.
    tries = 0 # I will also give the player the number of tries it took them to guess the number.

    print("Welcome to the guesser game, you will try to guess the number I have in my mind (0 - 100).") # A warm welcome for our player.
    while guessing: # Thanks to this expression, while the guessing boolean is True (so while we are guessing), it will keep asking what's our guess.
      guess = int(input("Your guess?: ")) # It asks us what is our guess and transforms it into an integer.
      if guess < randNum: # if the guess is lower than the answer,
        print("You're below it.") # It let's us know.
      elif guess > randNum: # And vice-versa
        print("You're flying above it.")
      else: 
        guessing = False # If the guess isn't lower or higher than the answer, then it's the answer. So we can assign guessing to False and terminate the loop.
      tries+=1 # In every iteration, our tries variable will increase itself as 1.

    return print(f"You won! The number was {randNum} and you guessed it in {tries} tries.") # We will return the printing of answer and the number of tries using f-string.
    
playGuesserGame() # We can call this function to play our game.



