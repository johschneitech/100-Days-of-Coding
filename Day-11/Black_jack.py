############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from art import logo
import random

print(logo)

dealer_choice = random.sample(cards,2)
print(f"The dealer's first choice is {dealer_choice[0]}")
human_choice = random.sample(cards,2)
print(f"You choose: {human_choice}")

def score(card_list):
  total_score = 0
  for card in card_list:
    total_score +=card
  return total_score

dealer_score = score(dealer_choice)
human_score = score(human_choice)
print(f"first human's score {human_score}")

def swith_ace(choice_list):
  if 11 in choice_list:
    choice_list.remove(11)
    choice_list.append(1)
  newscore = score(choice_list)
  return newscore

if human_score > 21 :
  if 11 in human_choice:
    human_score = swith_ace(human_choice)
    print(f" there is an 11 in choise {human_score}")

if dealer_score > 21 :
  if 11 in dealer_choice:
    dealer_score = swith_ace(dealer_choice)
    print(f" there is an 11 in choice {dealer_score}")

if human_score < 21 and dealer_score < 21:
  continue_game = input("Do you want to draw a card? Respond yes or no. ")

  def add_one_card(choice_list):
    choice_list += random.sample(cards, 1)
    return choice_list

if continue_game == "yes":
  if human_score < 21:
    human_choice = add_one_card(human_choice)
    human_score = score(human_choice)
  print(f"Human's score after third choice is: {human_score}")

if human_score > 21 :
  if 11 in human_choice:
    human_score = swith_ace(human_choice)
  print(f" there is an 11 in choise {human_score}")

if dealer_score > 21 :
  if 11 in dealer_choice:
    dealer_score = swith_ace(dealer_choice)
  print(f" there is an 11 in choice {dealer_score}")
      
if dealer_score < 17:
  while dealer_score < 17:
    dealer_choice = add_one_card(dealer_choice)
    dealer_score = score(dealer_choice)
    print(f"Dealer's other choise is: {dealer_choice[-1]}")
  print(f"Dealer's score after chosing card: {dealer_score}")

if dealer_score > 21 :
  if 11 in dealer_choice:
    dealer_score = swith_ace(dealer_choice)
    print(f" there is an 11 in choice {dealer_score}")
  
if dealer_score == 21 and human_choice !=21:
  print(f"Dealer has a blackjack dealer score is: {dealer_score}\n and human socere is:  {human_score}")
  print("You loose!")

if human_score == 21 and dealer_choice !=21:
  print(f"Human has a blackjack dealer score is: {dealer_score}\n and human socere is:  {human_score}")
  print("You win!")

if human_score == 21 and dealer_choice ==21:
  print(f"Both human and dealer has a blackjack; dealer score is: {dealer_score}\n and human socere is:  {human_score}")
  print("You win!")

if human_score > 21 and dealer_score <21:
  print(f"Human' score is: {human_score} dealer' score is: {dealer_score}")
  print("You loose!")

if dealer_score > 21 and human_score <21:
  print(f"dealer' score is: {dealer_score} human' score is: {human_score}")
  print("You win!")
  
if dealer_score < 21 and human_score < 21:
  if dealer_score == human_score:
    print(f"Both human and dealer score the same; dealer score is: {dealer_score}/n and human socere is:  {human_score}")
    print("It's a draw!")
  elif dealer_score > human_score:
    print(f"Dealer has a higher score; dealer score is: {dealer_score}\n and human socere is:  {human_score}")
    print("You loose!")
  else:
    print(f"Human has a higher score; dealer score is: {dealer_score}\n and human socer: {human_score}")
    print("You win!") 

