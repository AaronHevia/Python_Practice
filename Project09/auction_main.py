import os
from auction_art import logo


def clear_console():
    if os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
    elif os.name in ('linux', 'osx', 'posix'):
        os.system('clear')


bids = {}


def winning_bid():
    leading_bid = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > leading_bid:
            leading_bid = bids[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${leading_bid}.")


def blind_auction():
    open_bids = True
    while open_bids:
        name = input("What is your name?:  ")
        bid = float(input("What is your bid?:  $"))
        bids[name] = bid
        more_bids = input("Are there any other bidders? Type 'yes' or 'no'.  ").lower()
        clear_console()
        if more_bids == "no":
            open_bids = False
            winning_bid()


print(logo)
print("Welcome to the secret auction program.")
blind_auction()
x = input('press "x" to exit')
