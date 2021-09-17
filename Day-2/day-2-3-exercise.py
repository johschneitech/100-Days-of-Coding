# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_days = float(age) * 365
number_weeks = float(age) * 52
number_months = float(age) * 12

total_days  = 90 *365
total_weeks = 90 * 52
total_months = 90 *12

print(f"You have {total_days - number_days} days, {total_weeks - number_weeks} weeks, and {total_months - number_months} left.")
