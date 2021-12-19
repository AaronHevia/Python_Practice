import rps_ascii
import random

ascii_list = [rps_ascii.rock, rps_ascii.paper, rps_ascii.scissors]

print("Welcome to Rock Paper Scissors.\n")

player_choice = input('Please choose ("R" for Rock, "P" for Paper, "S" for Scissors):  ').lower()
if player_choice == "r":
    player_choice = 0
elif player_choice == "p":
    player_choice = 1
elif player_choice == "s":
    player_choice = 2

computer_choice = random.randint(0, 2)

print("You chose:")
if player_choice == 0:
    print(ascii_list[0])
elif player_choice == 1:
    print(ascii_list[1])
elif player_choice == 2:
    print(ascii_list[2])

print("Computer chose:")
if computer_choice == 0:
    print(ascii_list[0])
elif computer_choice == 1:
    print(ascii_list[1])
elif computer_choice == 2:
    print(ascii_list[2])

if player_choice == 0 and computer_choice == 2 or player_choice == 1 and computer_choice == 0 or\
        player_choice == 2 and computer_choice == 1:
    print("You win.")
elif computer_choice == 0 and player_choice == 2 or computer_choice == 1 and player_choice == 0 or\
        computer_choice == 2 and player_choice == 1:
    print("Computer wins.")
else:
    print("It is a draw.")
