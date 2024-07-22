import random
import hangman_art
import hangman_words
from replit import clear
display = []
lives = 6

chosen_word = random.choice(hangman_words.word_list)
#print(chosen_word)

for letter in chosen_word:
    display += "_"

print(f"{hangman_art.logo}{hangman_art.stages[6]}\nWelcome to Hangman!\n\n{' '.join(display)}")
endgame = False
while endgame == False: 
        
    guess = input("\nGuess a letter: ").lower()
    
    clear()
    
    if guess in display:
        print("\nYou've already tried that.")
    else:
        for letter in range(0,len(chosen_word)):
            if guess == chosen_word[letter]:
                display[letter] = guess
        
        print(f"\n{' '.join(display)}")
        if guess not in chosen_word:
            lives -=1
            print(f'{hangman_art.stages[lives]}\nThe letter "{guess}" is not in the word. You have {lives} lives left.')
        else:
            print(f"{hangman_art.stages[lives]}\nGreat!")
 
    if "_" not in display:
        endgame = True
        print("You won!")
    elif lives==0:
        endgame = True
        print(f'You lose.\n\nThe word was "{chosen_word}".')