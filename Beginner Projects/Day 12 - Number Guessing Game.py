#IMPORTS
from art import logo
import random
from replit import clear

#NUMBERS 1-100
numlist = []
for num in range(1,101):
    numlist.append(num)

#THE NUMBER TO BE GUESSED
def choose_num():
    return random.choice(numlist)
    
#GAME START
def game_start():
    print(f"Let's play\n{logo}")
    #CHOOSING DIFFICULTY AND LIFELINE
    difficulty= input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if difficulty=="easy":
        return 10
    if difficulty=="hard":
        return 5

#ASSESSMENT OF GUESS
def assess(guess):
    if guess==the_chosen_one:
        return True
    else:
        if guess>the_chosen_one:
            print("\nYour guess was TOO HIGH!")
        elif guess<the_chosen_one:
            print("\nYour guess was TOO LOW!")
        return False

#START GAME
restart=True
while restart==True:  
    lifeline = game_start()
    the_chosen_one = choose_num() 
    right_guess=False
    while right_guess==False and lifeline!=0:
        print(f"You have {lifeline} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        assessment = assess(guess) 
        if assessment==True:
            right_guess=True
        else:
            lifeline-=1
            
#END GAME / FINAL RESULT
    if guess==the_chosen_one:
        print(f"\nYou got it! The number was {the_chosen_one}.")
    else:
        print(f"\nOh no, you've run out of guesses. You lose :(")
#PLAY AGAIN
    if input("Do you want to play again? Type 'y' or 'n': ") == "n":
        restart=False
    else:
        clear()

print("\n\n---Game Over---")