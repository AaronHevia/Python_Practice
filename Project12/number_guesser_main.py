import os
import random
from number_guesser_art import logo


def clear_console():
    if os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
    elif os.name in ('linux', 'osx', 'posix'):
        os.system('clear')


def set_difficulty(choice):
    if choice == "easy":
        return 10
    elif choice == "medium":
        return 7
    elif choice == "hard":
        return 5


def check_guess(actual_number, guessed_number):

    if guessed_number > actual_number:
        print("\nToo high.  Guess again.")
    elif guessed_number < actual_number:
        print("\nToo low.  Guess again.")


def reduce_attempt(attempts):
    attempts -= 1
    prompt = "attempts"
    if attempts == 1:
        prompt = "attempt"
    print(f"You have {attempts} {prompt} remaining.")
    return attempts


def run():
    print(logo)
    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    difficulty = input("Choose a difficulty.  Type 'easy', 'medium', or 'hard':  ")
    attempts = set_difficulty(difficulty)
    print(f"You have {attempts} attempts to guess the number.")
    guess = int(input("Make a guess:  "))
    while attempts > 1 and guess != number:
        check_guess(number, guess)
        attempts = reduce_attempt(attempts)
        guess = int(input("Make another guess:  "))
    if attempts == 0:
        print(f"\nYou have run out of attempts.  The correct number was {number}.")
    else:
        print(f"\n{guess} is correct.  Congratulations!")


run()

while input("\nWould you like to play again?  ").lower() == "y":
    clear_console()
    run()
