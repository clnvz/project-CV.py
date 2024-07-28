import art
import random
from game_data import CELEB
from os import system


def pickperson():
    """Returns a random number from the dictionary"""
    return random.randint(1, len(CELEB) - 1)


def assessment(bet, win):
    """Returns True or False  if the guess is right or wrong"""
    if win == 0 and bet == "a":
        return True
    elif win == 1 and bet == "b":
        return True
    else:
        return False


PA = pickperson()
is_right = True
current_score = 0
print(f"Welcome! Let's play {art.logo}")
while is_right == True:
    PB = pickperson()
    if PA == PB:
        PB = pickperson()
    afollow = CELEB[PA]["follower_count"]
    bfollow = CELEB[PB]["follower_count"]
    winner = 0
    famous = 0
    if afollow < bfollow:
        winner = 1
        famous = PB
    else:
        famous = PA

    print(f"Compare A: {CELEB[PA]["name"]}, a {CELEB[PA]["description"]} from {CELEB[PA]["country"]}.")
    print(art.vs)
    print(f"Against B: {CELEB[PB]["name"]}, a {CELEB[PB]["description"]} from {CELEB[PB]["country"]}.")
# FOR CHECKING PURPOSES ONLY
    # print(f'{CELEB[PA]["follower_count"]} vs {CELEB[PB]["follower_count"]}')
    # print(winner)
    playerbet = input("Who has more followers? Type 'A' or 'B': ").lower()
    assess = assessment(bet=playerbet, win=winner)
    if assess == True:
        # system('cls') #This doesn't work on my laptop. Help :(
        current_score += 1
        print(f"\nYou're right! Current score: {current_score}")
        if winner == 0:
            PA = famous
        else:
            PA = PB
    else:

        is_right = False

# system('cls') #This doesn't work on my laptop. Help :(
print(f"\nSorry, that's wrong. Final score: {current_score}")