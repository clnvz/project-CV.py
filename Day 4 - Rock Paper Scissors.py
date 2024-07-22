rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice = int(input("Let's play Rock-Paper-Scissors! Type 0 for Rock, 1 for Paper and 2 for Scissors.\n\n"))
signs = [rock, paper, scissors]
if choice >2 or choice <0:
    print("You typed an invalid number. You lose.")
else:
    print(signs[choice] + "\n\nComputer chose\n")

    compchoice = random.randint(0,2)
    print(signs[compchoice])

    if choice == compchoice:
        print("It's a draw.")
    elif choice == 0 and compchoice == 1:
        print("You lose!")
    elif choice == 1 and compchoice == 2:
        print("You lose!")
    elif choice == 2 and compchoice == 0:
        print("You lose!")
    elif choice == 0 and compchoice == 2:
        print("You won!")
    elif choice == 1 and compchoice == 0:
        print("You won!")
    elif choice == 2 and compchoice == 1:
        print("You won!")
# elif choice >2 or choice <0:
#     print("You typed an invalid number. You lose.")