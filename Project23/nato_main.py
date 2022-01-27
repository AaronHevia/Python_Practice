import pandas

# Upload NATO alphabet:
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input('Enter a word to spell in NATO format:  ').upper()
    try:
        nato_spelled = [nato_dict[letter] for letter in list(word)]
    except KeyError:
        print('Please spell the word with letters in the alphabet.')
        generate_phonetic()
    else:
        print(nato_spelled)


generate_phonetic()
