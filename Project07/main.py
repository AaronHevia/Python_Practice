import sys
sys.path.insert(1, 'E:/_GitHub/Python_Practice')
from helper_functions import *
import random
import hangman_art as art
import hangman_dictionary as dictionary

chosen_word = random.choice(dictionary.word_list)

display = []
guessed_letters = []
lives = 6

for letter in chosen_word:
    display.append("_")

game_over = False
joined_display = "".join(display)

print(art.logo)

while not game_over:
    print(art.lives[lives])
    print(joined_display)
    guess = input("Guess a letter:  ").lower()
    clear_console()

    if guess in guessed_letters:
        print(f"You have already guessed the letter {guess}.  Try again.")
    else:
        guessed_letters.append(guess)

        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = guess

        joined_display = "".join(display)

        if guess not in chosen_word:
            lives -= 1
            print(f'"{guess}" is not in the word.  You lose a life.')

        if joined_display == chosen_word or lives == 0:
            game_over = True

if lives > 0:
    print(joined_display)
    print("You win.")
else:
    print(art.lives[0])
    print(f"The word was {chosen_word}.")
    print("You lose.")

x = input('press "x" to exit')
