import sys
sys.path.insert(1, 'E:/_GitHub/Python_Practice')
from helper_functions import *
from higher_lower_game_data import data
import higher_lower_art as art
import random


def retrieve_account(account):
    """Retrieves a random account from database."""
    retrieved_account = random.choice(data)
    while retrieved_account == account:
        retrieved_account = random.choice(data)
    return retrieved_account


def format_data(account):
    """Takes an account data and returns a printable format."""
    return f"{account['name']} - {account['description']} from {account['country']}"


def ask(account1, account2):
    """Asks the user to choose who has more followers and returns the option chosen."""
    print(f"Compare A:  {format_data(account1)}")
    print(art.vs)
    print(f"Against B:  {format_data(account2)}")
    choice = input("Who has more followers? Type 'A' or 'B':  ").upper()
    if choice == "A":
        return account1
    elif choice == "B":
        return account2


def compare(account1, account2):
    """Returns the account with the higher number of followers.  Comparison is made between 2 people."""
    p1_followers = account1["follower_count"]
    p2_followers = account2["follower_count"]
    if p1_followers > p2_followers:
        return account1
    else:
        return account2


score = 0


def result(guess, answer):
    """Prints whether the guess is right or wrong and tracks how many consecutive answers the user has gotten."""
    global score
    clear_console()
    print(art.logo)
    if guess == answer:
        score += 1
        print(f"You're right!  Current score:  {score}")
        run(answer)
    else:
        print(f"Sorry, that's wrong.  Final score:  {score}")


account_a = {}
account_a = retrieve_account(account_a)


def run(account):
    account_b = retrieve_account(account)
    choice = ask(account, account_b)
    correct_answer = compare(account, account_b)
    result(choice, correct_answer)


print(art.logo)
run(account_a)
close()
