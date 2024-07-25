#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# easypw = ""
# for let in range(1, nr_letters+1):
#   easypw += letters[random.randrange(0,len(letters))]
# for let in range(1, nr_symbols+1):
#   easypw += symbols[random.randrange(0,len(symbols))]
# for let in range(1, nr_numbers+1):
#   easypw += numbers[random.randrange(0,len(numbers))]
# print(f"Here is your password: {easypw}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# hardpw = ""
# totdig = nr_letters + nr_symbols + nr_numbers

# for turns in range(1,28): #depends on the total number of characters
#   seq = random.randrange(1,4)

#   if seq ==1: #letters
#     if nr_letters==0:
#       hardpw
#     else:
#       nr_letters -=1
#       hardpw += letters[random.randrange(0, len(letters))]
  
#   elif seq==2: #symbols
#     if nr_symbols==0:
#       hardpw
#     else:
#       nr_symbols-=1
#       hardpw += symbols[random.randrange(0, len(symbols))]
  
#   elif seq==3: #numbers
#     if nr_numbers==0:
#       hardpw
#     else:
#       nr_numbers-=1
#       hardpw += numbers[random.randrange(0, len(numbers))]

# print(f"Here is your password: {hardpw}")

#SIMPLE SOLUTION FOR HARD CHALLENGE
hardlist = []
for let in range(1, nr_letters+1):
  hardlist += letters[random.randrange(0,len(letters))]
for let in range(1, nr_symbols+1):
  hardlist += symbols[random.randrange(0,len(symbols))]
for let in range(1, nr_numbers+1):
  hardlist += numbers[random.randrange(0,len(numbers))]

random.shuffle(hardlist)
hardpw = ""
for char in hardlist:
  hardpw += char

print(f"Here is your password: {hardpw}")