print("Welcome to the tip calculator.")
bill = float(input("Please enter your total bill:  $"))
percentage = .01 * float(input("What percentage tip would you like to give?  "))
total = round(bill * (1 + percentage), 2)
number_of_people = int(input("How many people will split the bill?  "))
word = "person"
if number_of_people > 1:
    word = "people"
total_per_person = round(total / number_of_people, 2)
print(f"{number_of_people} {word} will pay ${total_per_person}")
