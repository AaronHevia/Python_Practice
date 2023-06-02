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
    @return: Dollar amount of the initial bill.
    """
    return float(input("Please enter the total bill:  $"))


def calculate_percentage() -> float:
    """
    Returns the decimal form of a percentage entered (i.e., 10 returns 0.1).
    @rtype: float
    @return: Percentage of tip in decimal form.
    """
    return .01 * float(input("What percentage tip would you like to give?  "))


def finalize_bill(amount, percent) -> float:
    """
    Returns the final bill with tip included (i.e., A $10 bill with a 10% tip returns 11.00)
    @param amount: float, Dollar amount to increase.
    @param percent: float, Percentage in decimal form which to increase the amount by.
    @rtype: float
    @return: Final bill including tip.
    """
    total = amount * (1 + percent)
    return total


def get_buyers() -> int:
    """
    Returns the amount of people the bill will be split amongst.
    @rtype: int
    @return: Number of people paying for the bill.
    """
    people = int(input("How many people will split the bill?  "))
    return people


def split_bill(amount, person) -> float:
    """
    Divides the dollar amount by a whole number and returns the dollar amount to be paid by each person.
    @param amount: float, Dollar amount to be split amongst buyers.
    @param person: int, Amount of people paying for the amount.
    @rtype: float
    @return: Amount to be paid by each person.
    """
    total_each = round(amount / person, 2)
    return total_each


def print_bill(person, amount) -> None:
    """
    Prints the amount to be paid by each person paying for the bill.
    @param person: int, Amount of people paying for the amount.
    @param amount: float, Dollar amount each buyer will pay.
    @return: None
    """
    word = "buyer"
    if person > 1:
        word = "buyers"

    total_per_person = "{:.2f}".format(amount)
    print(f"{person} {word} will pay ${total_per_person}")


greeting()
bill = get_bill()
percentage = calculate_percentage()
final_bill = finalize_bill(bill, percentage)
buyers = get_buyers()
total_per = split_bill(final_bill, buyers)
print_bill(buyers, total_per)
