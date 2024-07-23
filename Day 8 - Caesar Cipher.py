alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from math import ceil
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  while shift_amount > 25:
    shift_amount -= 26
  
  for char in start_text:
#TODO-3:
    if char not in alphabet:
      end_text +=char
    
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")


#TODO-1:
from art import logo
print(logo)

#TODO-4: 
again = True
while again==True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
#TODO-2:

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  ifagain = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
  if ifagain=="yes":
    again=True
  else:
    again=False
    print("Goodbye")
