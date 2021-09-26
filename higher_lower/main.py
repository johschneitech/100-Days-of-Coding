from art import logo, vs
from game_data import data
import random

print(logo)

def first_part():
  # Picked the first page and create a random list to use as index 
  random_ind = random.randint(0, len(data) -1)
  first_choice = data[random_ind]
  list_index = random.sample(range(len(data)), len(data))
  list_index.remove(random_ind)
  return first_choice, list_index

def game():
  #format print statement and call compare_page function
  first_choice, list_index = first_part()
  should_continue = True
  index_list = 0 
  points = 0
  while should_continue:
    ind = list_index[index_list]
    print (f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
    print(vs)
    second_choice = data[ind]
    print (f"Compare B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    should_continue= compare_page(answer, first_choice, second_choice, should_continue)
    if should_continue:
      first_choice = second_choice
      index_list += 1
      points +=1
      print(f"You win! You have {points} points.")
  print(f"You lose! You finish with {points} points.\n Goodbye!")

def compare_page ( answer, first_choice, second_choice, should_continue):
  #Compare follower after anser and determine win or loss
  if answer == "A" and first_choice["follower_count"] > second_choice["follower_count"]: 
    should_continue = True
  elif answer == "B" and second_choice["follower_count"] > first_choice["follower_count"]:
    should_continue = True
  else:
    should_continue = False
  return should_continue
  
game()
