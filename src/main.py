import random

list = []
with open("five_letter_words.txt", "r") as f:
  words = f.read()
  list = words.split(",")

def get_random_word():
  return random.choice(list)

def wordle():
  word = get_random_word()

  print("welcome to wordle.py!\n")
  print("guess the 5 letter word")

  tries = 6

  while tries > 0:
    guess = input(f"\n\nyou have {tries} attempts remaining.\nenter your guess:\t")

    if len(guess) != 5:
      print("\nplease enter a 5 letter word!")
      continue
    print()
    for i, c in enumerate(word):
      if c != guess[i]:
        print(f"{guess[i]}!\t", end="")
      else:
        print(f"{guess[i]}\t",end="")

    if guess == word:
      print("\nyou guess the word correctly, congrats!")
      break
  
    tries -= 1
  
  if guess != word:
    print("\nyou ran out of attempts!")
    print("\nthe correct answer is " + word)

if __name__ == "__main__":
  wordle()