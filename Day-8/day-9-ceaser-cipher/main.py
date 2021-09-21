from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def cesear(message, shift_code, choice ):
  cipher_text = ""
  if choice == "decode":
      shift_code *= -1
  for letter in text:
    if letter not in alphabet:
      cipher_text += letter
    else:
      index_list = 0
      index_list += (alphabet.index(letter) + shift_code) % 26
      cipher_text += alphabet[index_list]
  print(cipher_text)

cesear(text, shift , direction)

end_game = input("Do you want to continue? Please answer yes or no. ").lower()

while end_game == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  cesear(text, shift , direction)
  end_game = input("Do you want to continue? Please answer yes or no. ").lower()

print("Goodbye!")
