# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

first_name = name1.lower()
second_name = name2.lower()

true_count = 0

true_count += first_name.count("t")
true_count += first_name.count("r")
true_count += first_name.count("u")
true_count += first_name.count("e")

true_count += second_name.count("t")
true_count += second_name.count("r")
true_count += second_name.count("u")
true_count += second_name.count("e")

love_count = 0
love_count += first_name.count("l")
love_count += first_name.count("o")
love_count += first_name.count("v")
love_count += first_name.count("e")
love_count += second_name.count("l")
love_count += second_name.count("o")
love_count += second_name.count("v")
love_count += second_name.count("e")

true_count = str(true_count)
love_count = str(love_count)

score = true_count + love_count

score = float(score)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")

elif score >= 40 or score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
  
