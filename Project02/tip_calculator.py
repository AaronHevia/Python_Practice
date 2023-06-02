def greeting() -> None:
    """
    Prints a greeting to the user for the tip calculator.
    @return: None
    """
    print("Welcome to the tip calculator!\n")


def get_bill() -> float:
    """
    Asks the user for the net bill of the meal eaten.
    @rtype: float
    @return: bill
    """
    return float(input("Please enter the total bill:  $"))


percentage = .01 * float(input("What percentage tip would you like to give?  "))
total = bill * (1 + percentage)
people = int(input("How many people will split the bill?  "))
word = "person"
if people > 1:
    word = "people"
total_per_person = "{:.2f}".format(round(total / people, 2))
print(f"{people} {word} will pay ${total_per_person}")

greeting()
bill = get_bill()
