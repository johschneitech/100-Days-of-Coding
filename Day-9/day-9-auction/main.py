from replit import clear

from art import logo
#HINT: You can call clear() to clear the output in the console.

print (logo)

other_user = True

bid = {}

while other_user == True:
  name = input("What is your name?: ").lower()
  price = float(input("How much do you want to pay?: $"))
  bid[name] = price

  clear()
  
  other_bidder = input("Is there any other bidder? Pleas answer yes or no: ")
  if other_bidder == "no":
    other_user = False

highest_bidder = max(bid.values())

print(f"The highest bidded pay: {highest_bidder}")
