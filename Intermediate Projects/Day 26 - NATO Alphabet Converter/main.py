import pandas as pd

# Create a dictionary in this format: {"A": "Alfa", "B": "Bravo", ..}
df = pd.read_csv("nato_phonetic_alphabet.csv")
reference = {row.letter:row.code for (index, row) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
result = [reference[letter] for letter in word]
print(result)
