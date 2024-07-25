############### Blackjack Project #####################

#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#IMPORTS
from art import logo
import random
from replit import clear

#DRAWING CARDS
def draw_one():
    """Returns a random card from the deck"""
    return cards[random.randrange(0,len(cards)-1)]
   
#PLAY GAME
def play_blackjack():
    """Start a Blackjack game. Enjoy!"""
    clear()
    print(logo)
    
#STORAGE FOR SCORES AND CARDS
    user_score = 0
    com_score = 0
    user_cards=[]
    com_cards=[]

#FIRST DRAW
    first_udraw=draw_one() #user
    user_cards.append(first_udraw)
    first_cdraw=draw_one() #com
    com_cards.append(first_cdraw)
    user_score=int(first_udraw) #tally user
    com_score=int(first_cdraw) #tally com
    
#SECOND DRAW ONWARDS      
    flag_again=True
    while flag_again==True:
        next_udraw=draw_one() #user
        user_cards.append(next_udraw)
        next_cdraw=draw_one() #com
        com_cards.append(next_cdraw)
        user_score=sum(user_cards) #tally user
        com_score=sum(com_cards)  #tally com

#COM BLACKJACK
        if user_score>21 and len(user_cards)==2:
            flag_again=False
        elif com_score==21 and len(com_cards)==2:
            flag_again=False
        else:

#USER ADVANTAGE
            if 11 in user_cards and user_score>21:
                user_cards.remove(11)
                user_cards.append(1)
                user_score=sum(user_cards)

#USER SCORE >= 21
            if user_score>=21:
                flag_again=False
#DRAW AGAIN       
            elif user_score<21:
                print(f"     Your cards: {user_cards}, current score: {user_score}")
                print(f"     Computer's first card: {com_cards[0]}")
                draw_again = input("Type 'y' to get another card, type 'n' to pass: ")
                if draw_again=="y":
                    flag_again=True
                elif draw_again=="n":
                    flag_again=False
    
#COMPUTER HIDDEN ADVANTAGE
    com_advantage=True
    while com_score<17:
        if 11 in com_cards and com_score>21:
            com_cards.remove(11)
            com_cards.append(1)
            com_score=sum(com_cards)
            
        next_cdraw=draw_one() #com
        com_cards.append(next_cdraw)
        com_score=sum(com_cards)
        if com_score>=17:
            com_advantage=False
        
#FINAL RESULT
    print(f"     Your final hand: {user_cards}, final score: {user_score}")
    print(f"     Computer's final hand: {com_cards}, final score: {com_score}")

    if user_score<com_score and com_score<22 or user_score>21:
        if com_score==21 and len(com_cards)==2:
            print("Computer got a BLACKJACK !!! You lose")
        elif user_score>21:
            print("Bust! You lose")
        else:
            print("You lose")
    elif user_score>com_score and user_score<22 or com_score>21:
        if user_score==21:
            if len(user_cards)==2:
                print("BLACKJACK !!! You win")
            else:
                print("You win")
        else:
            print("You win")
    elif user_score==com_score:
        print("It's a draw")

#PLAY AGAIN?
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
        play_blackjack()

#START
if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_blackjack()
