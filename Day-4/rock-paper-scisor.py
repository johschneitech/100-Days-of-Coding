rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# print(rock)

import random


list_posibilities = [rock, paper, scissors]


computer_choice = list_posibilities[random.randint(0, len(list_posibilities)-1)]

player_choice = input("Please choose between rock, paper, or scissors ")

if player_choice == "rock":
  print("You choose rock \n", rock)
  if computer_choice == list_posibilities[0]:
    print("The compute chooses rock \n ",  computer_choice)
    print("Tie Game!")
  elif computer_choice == list_posibilities[1]:
    print("The compute chooses paper \n ",  computer_choice)
    print("You lose!")
  else:
    print("The compute chooses scissors \n ",  computer_choice)
    print("You win!")

elif player_choice == "paper":
  print("You choose paper \n", paper)
  if computer_choice == list_posibilities[0]:
    print("The compute chooses rock \n ",  computer_choice)
    print("You win!")
  elif computer_choice == list_posibilities[1]:
    print("The compute chooses paper \n ",  computer_choice)
    print("Tie Game!")
  else:
    print("The compute chooses scissors \n ",  computer_choice)
    print("You lo!")

elif player_choice == "scissors":
  print("You choose scissors \n", scissors)
  if computer_choice == list_posibilities[0]:
    print("The compute chooses rock \n ",  computer_choice)
    print("You loose!")
  elif computer_choice == list_posibilities[1]:
    print("The compute chooses paper \n ",  computer_choice)
    print("You win!")
  else:
    print("The compute chooses scissors \n ",  computer_choice)
    print("Tie game!")

else:
  print("Wrong choise!")
  
