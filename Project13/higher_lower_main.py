from helper_functions import clear_console
from higher_lower_game_data import data
import higher_lower_art as art
import random


def retrieve_person(person):
    """Retrieves a random person from database."""
    retrieved_person = random.choice(data)
    while retrieved_person == person:
        retrieved_person = random.choice(data)
    return retrieved_person


def ask(person1, person2):
    """Asks the user to choose who has more followers and returns the option chosen."""
    print(f"Compare A:  {person1['name']} - {person1['description']} from {person1['country']}")
    print(art.vs)
    print(f"Against B:  {person2['name']} - {person2['description']} from {person2['country']}")
    choice = input("Who has more followers? Type 'A' or 'B':  ").upper()
    if choice == "A":
        return person1
    elif choice == "B":
        return person2


def compare(person1, person2):
    """Returns the person with the higher number of followers.  Comparison is made between 2 people."""
    p1_followers = person1["follower_count"]
    p2_followers = person2["follower_count"]
    if p1_followers > p2_followers:
        return person1
    else:
        return person2


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


person_a = {}
person_a = retrieve_person(person_a)


def run(person):
    person_b = retrieve_person(person)
    correct_answer = compare(person, person_b)
    choice = ask(person, person_b)
    result(choice, correct_answer)


print(art.logo)
run(person_a)
input("'Enter' to exit.")
