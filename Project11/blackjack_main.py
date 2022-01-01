# ############## Current Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# House wins automatically from blackjack off the draw.

import sys
sys.path.insert(1, 'E:/_GitHub/Python_Practice')
from helper_functions import *
import random
from blackjack_art import logo

dealer_cards = []


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(drawn_cards):
    """Take a list of cards and return the score calculated from the cards"""

    if sum(drawn_cards) == 21:
        return 0

    if 11 in drawn_cards and sum(drawn_cards) > 21:
        drawn_cards.remove(11)
        drawn_cards.append(1)

    return sum(drawn_cards)


def compare(user_score, dealer_score, dealer_draws):
    if dealer_score == 0 and len(dealer_draws) == 2:
        return "House has Blackjack off the draw.  House wins. 😤"
    elif user_score > 21:
        return "You went over. You lose 😤"
    elif dealer_score == 0 and user_score < 21:
        return "You lose, opponent has Blackjack 😱"
    elif user_score == dealer_score:
        return "Draw 🙃"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)

    user_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {dealer_cards[0]}")

        if user_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    computer_score = calculate_score(dealer_cards)

    while computer_score != 0 and computer_score < user_score:
        dealer_cards.append(deal_card())
        computer_score = calculate_score(dealer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {dealer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score, dealer_cards))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    clear_console()
    dealer_cards = []
    play_game()

close()
