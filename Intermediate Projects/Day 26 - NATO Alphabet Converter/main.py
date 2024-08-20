import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
reference = {row.letter: row.code for (index, row) in df.iterrows()}


def convert_name():
    word = input("Enter a word: ").upper()
    try:
        result = [reference[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters are allowed.")
        convert_name()
    else:
        print(result)


convert_name()
