# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
number_people = 0 
total_height = 0

for student in student_heights:
  number_people += 1
  total_height += student
average_height = round(total_height / number_people)

print(f"The average student height is: {average_height}.")
