#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
from replit import clear

print(logo)
"""
This fucntion is asigning number of guess a player 
has depending on the level the player choses
"""
def pick_level():
  clear()
  level = input("Type easy for easy level and hard for hard level: ").lower()
  if level == "easy".lower():
    number_of_guess = 10
  elif level == "hard".lower():
    number_of_guess = 5
  else:
    print("You did not choose hard or easy the deafault level will be hard.")
    number_of_guess = 5
  return number_of_guess

computer_number = random.randint(0,100)
print(f"The computer number is {computer_number}")

def player_number_choice():
  all_choices =[]
  should_continue = True
  number_of_guess = pick_level()
  while should_continue:
    print(f"You have {number_of_guess} tries left") 
    number_of_guess -=1
    player_number = int(input("Please type a number between 1 and 100: "))
    all_choices.append(player_number)
    if player_number > computer_number:
      print(f"You chose {player_number}, and it  is greater than the correct number")
    elif player_number < computer_number:
      print(f"You chose {player_number}, and it is less than the correct number")
    else:
      should_continue = False
      print(f"You chose {player_number}, it's equal to the computer's choice which is: {computer_number}")
    if number_of_guess <= 0:
      should_continue = False

  return player_number, computer_number, all_choices

player_number, computer_number, list_choices= player_number_choice()

if player_number != computer_number:
  print(f"You lost, you run out of guesses and you did not guess the correct answer. Your choices were {list_choices} The correct answer was {computer_number}")
else:
  print(f"You won! You gessed the correct number as your last guess was {list_choices[-1]}, and the correct answer {computer_number}")

continue_playing = input("Do you want to continue playing? Answer yes or no: ").lower()
another_game = True

if continue_playing == "no":
  another_game = False
  print("Goodbye!")
elif continue_playing != "no" and continue_playing != "yes":
  another_game = False
  print("You gave the wrong answer. Goodbye!")
else:
  while another_game:
    print("I am happy that you want to play again. Let's go!!!")
    player_number_choice()

