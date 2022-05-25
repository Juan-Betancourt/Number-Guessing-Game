from random import randint
from art import logo

EASY_MODE = 10
HARD_MODE = 5
#Function to check the users answer to the random number selected 

def check_answer(user_guess, answer, turns):
  """Checks answer against guess, returns the number of turns remaining."""
  if user_guess == answer:
    print(f"\nYou got it, the answer was {answer}")
  elif user_guess > answer:
    print("\nYour number is too high")
    return turns - 1
  else:
    print("\nYour number is too low")
    return turns - 1

#Make a function to set difficulty

def set_difficulty():
  level = input("\nChoose a difficulty: Type 'easy' or 'hard': ").lower()
  if level == "easy":
    return EASY_MODE
  else:
    return HARD_MODE
    
#Choosing a random number from 1 to 100
def game():
  print(logo)
  print("\nWelcome to the number guessing game!")
  print("\nI am thinking of a number between 1 and 100")
  answer = randint(1, 100)
  print(f"\nPssst, the actual answer is {answer}")
  
  turns = set_difficulty()
  
  #Repeat the guessing functionality if the player gets it wrong
  user_guess = 0
  while user_guess != answer:
    #Let the player guess a number
    print(f"\nYou have {turns} attempts remaining to guess the number.\n")
    user_guess = int(input("Guess a number: "))
    #Track the number of tokens and reduce it by 1
    turns = check_answer(user_guess, answer, turns)
    if turns == 0:
      print(f"Thank you for playing but you failed to find the number {answer}")
      return
    elif user_guess != answer:
      print("\nGuess again.")

game()