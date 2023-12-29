import random
from words import words
import string

def getValidWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def playHangman(x):
    word = getValidWord(words)
    wordLetters = set(word) # Creates a küme
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    health = x

    while len(wordLetters) > 0 and health > 0:
      print("\nYou have used these letters: ",", ".join(usedLetters))
      wordList = [wordLetters if wordLetters in usedLetters else '-' for wordLetters in word]
      print("Current word: ","".join(wordList))
      userInput = input("Guess a letter: ").upper()
      if userInput in alphabet - usedLetters:
          usedLetters.add(userInput)
          if userInput in word:
            wordLetters.remove(userInput)
          else:
             health-=1
             print(f"You lost one health. New Health: {health}")
      elif userInput in usedLetters:
        print("You've already guessed that letter.")
      else:
        print("Invalid character.")
    
    if len(wordLetters) == 0:
       return print(f"You won the game! The word was {word}.")
    else:
       return print(f"You lost the game, the word was {word}.")

playHangman(15)
