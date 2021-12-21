import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_numbers = int(input("How many numbers would you like in your password?\n"))
number_of_characters = int(input("How many special characters would you like in your password?\n"))
total  = number_of_letters + number_of_numbers + numbe_of_characters
password = ""

while total > 0:
    choice = random.randint(0, 2)
    if number_of_letters > 0 and choice == 0:
        password += random.choice(letters)
        total -= 1
        number_of_letters -= 1
    elif number_of_numbers > 0 and choice == 1:
        password += random.choice(numbers)
        total -= 1
        number_of_numbers -= 1
    elif number_of_characters > 0 and choice == 2:
        password += random.choice(symbols)
        total -= 1
        number_of_characters -= 1

print(f"Here is your password: {password}")
