from art import logo

print(logo)

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number number? "))

#add
def add(n1, n2):
  return n1 + n2

#Substraction
def sub(n1, n2):
  return n1 - n2


#Multiplication
def multiply(n1, n2):
  return n1 * n2

#division
def divide(n1, n2):
  if n2 == 0:
    return "divisor cannot be 0"
  return n1 / n2

operations = {
  "+": add,
  "-": sub,
  "*": multiply,
  "/": divide,
}

def calculator(num1, num2):
  for keys in operations:
    print (keys)

  operation_symbol = input("Please choose one of the symbols above: ")

  answer = operations[operation_symbol](num1,num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")
  return answer

answer = calculator(num1, num2)

continue_operation = True
question = input("Do you wish to continue with the answer as number 1 answer y or n: ")
if question != 'y':
    continue_operation = False

while continue_operation:
  num1 = answer
  num2 = int(input("What is the second number number? "))
  answer = calculator(num1, num2)
  question = input("Do you wish to continue with the answer as number 1 answer y or n: ")
  if question != 'y':
    continue_operation = False
