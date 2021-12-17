print("Welcome to the tip calculator!\n")
bill = float(input("Please enter the total bill:  $"))
percentage = .01 * float(input("What percentage tip would you like to give?  "))
total = bill * (1 + percentage)
people = int(input("How many people will split the bill?  "))
word = "person"
if people > 1:
    word = "people"
total_per_person = round(total / people, 2)
formatted_total = "{:.2f}".format(total_per_person)
print(f"{people} {word} will pay ${formatted_total}")
