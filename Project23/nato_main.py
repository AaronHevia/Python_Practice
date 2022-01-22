import pandas

# Upload NATO alphabet:
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = input('Enter a word to spell in NATO format:  ').upper()
nato_spelled = [nato_dict[letter] for letter in list(word)]

print(nato_spelled)
