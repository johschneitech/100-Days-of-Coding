# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height **2)
print(bmi)

if bmi <= 18.5:
  print("You are underweight")
elif bmi >= 18.5 and bmi <=25:
  print("You have a normal weight")
elif bmi >= 25 and bmi <=25:
  print("You are slightly overweight")
elif bmi >= 30 and bmi <=35:
  print("You are obese")
else:
  print("are clinically obese.")
