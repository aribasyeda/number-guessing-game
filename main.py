from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns, diff):
  """Checks answer against guess. Returns the number of turns remaining"""
  if guess == answer:
    print(f"\nYou got it! The answer is {answer} 🎉")
  elif guess < answer and abs(guess - answer) > diff:
    print(f"\n🔴 Too low \n")
    return turns - 1
  elif guess > answer and abs(guess - answer) > diff:
    print(f"\n🔴 Too high \n")
    return turns - 1
  else:
    print(f"\n🟢 You're close! \n")
    return turns - 1

def set_difficulty():
  difficulty = input("👉 Choose a difficulty level. Type 'easy or 'hard':\n")
  if difficulty == "easy":
      return EASY_LEVEL_TURNS
  elif difficulty == "hard":
      return HARD_LEVEL_TURNS
  else:
    print("You did not enter 'easy' or 'hard'")

def game():
  print(logo)
  print("✨ Welcome to the number guessing game ✨")
  print("\nI'm thinking of a number between 0 and 100. Guess the number!\n")

  turns = set_difficulty()
  if turns == None:
    return
  
  answer = randint(1, 101)

  guess = 0
  while guess != answer:
    
    print(f"\nYou have ✨ {turns} ✨ attempts remaining!")
    
    guess = int(input("\n👉 Make a guess:\n"))

    turns = check_answer(guess, answer, turns, diff = 5)

    if turns == 0:
      print(f"You ran out of guesses, you lose! The answer is {answer}")
    elif guess != answer:
      print("❌ Guess again")
      
game()
