import sys
sys.path.insert(1, 'E:/_GitHub/Python_Practice')
from helper_functions import *


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

COIN_VALUE = {
    "penny": .01,
    "nickel": .05,
    "dime": .10,
    "quarter": .25
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def calculate_total(quarters, dimes, nickels, pennies):
    total = 0
    total += COIN_VALUE["quarter"] * quarters
    total += COIN_VALUE["dime"] * dimes
    total += COIN_VALUE["nickel"] * nickels
    total += COIN_VALUE["penny"] * pennies
    return total


quarters_in_machine = 0
dimes_in_machine = 0
nickels_in_machine = 0
pennies_in_machine = 0
machine_money = calculate_total(quarters_in_machine, dimes_in_machine, nickels_in_machine, pennies_in_machine)


def format_money(money_in_machine):
    """Returns money value in string format to show 2 decimals."""
    return "{:.2f}".format(money_in_machine)


def format_ingredients(ingredient):
    """Returns string format of ingredients to show unit of measurement."""
    if ingredient == "water" or ingredient == "milk":
        return f"{resources[ingredient]}ml"
    elif ingredient == "coffee":
        return f"{resources[ingredient]}g"


def ask():
    """Asks the user which type of coffee they would like from the choices.  Additional options are 'report' for
    resource report and 'off' for maintenance mode."""
    choice = input("What would you like? (espresso/latte/cappuccino):  ")

    if choice == "off":
        return
    elif choice == "report":
        print_report()
        ask()
    else:
        resource_check(choice)


def print_report():
    """Prints the amount of resources available in the vending machine."""
    clear_console()
    print("Current resources available:")
    for resource in resources:
        print(f"{resource}:  {format_ingredients(resource)}")
    print(f"Money:  ${format_money(machine_money)}")


def resource_check(coffee):
    """Checks to see if there is enough resources to make the coffee requested.  If there is not enough, it returns to
    asking the user again."""
    chosen_coffee = MENU[coffee]
    resource_count = 0
    for resource in chosen_coffee["ingredients"]:
        amount = chosen_coffee["ingredients"][resource]
        if amount > resources[resource]:
            resource_count += 1
            print(f"Sorry there is not enough {resource}.")

    if resource_count > 0:
        ask()
    else:
        process_coins(coffee)


def process_coins(coffee, machine_quarters=quarters_in_machine, machine_dimes=dimes_in_machine,
                  machine_nickels=nickels_in_machine, machine_pennies=pennies_in_machine):
    """Gets the price of selected coffee and calculates money inserted."""
    coffee_price = MENU[coffee]["cost"]
    print(f"{coffee} costs ${format_money(coffee_price)}.")
    print("Please insert coins:")
    quarters_inserted = int(input("How many quarters:  "))
    machine_quarters += quarters_inserted
    dimes_inserted = int(input("How many dimes:  "))
    machine_dimes += dimes_inserted
    nickels_inserted = int(input("How many nickels:  "))
    machine_nickels += nickels_inserted
    pennies_inserted = int(input("How many pennies:  "))
    machine_pennies += pennies_inserted
    total = calculate_total(quarters_inserted, dimes_inserted, nickels_inserted, pennies_inserted)
    make_transaction(coffee, total, coffee_price, quarters_inserted, dimes_inserted, nickels_inserted, pennies_inserted)


def make_transaction(coffee, money_inserted, price, quarters, nickels, dimes, pennies, machine_quarters=quarters_in_machine,
                     machine_dimes=dimes_in_machine, machine_nickels=nickels_in_machine,
                     machine_pennies=pennies_in_machine):
    """Checks that the user inserted enough coins to make the coffee otherwise will refund money inserted."""
    if money_inserted < price:
        print("Sorry.  Not enough deposited.  Money refunded.")
        machine_quarters -= quarters
        machine_dimes -= dimes
        machine_nickels -= nickels
        machine_pennies -= pennies
    elif money_inserted > price:
        change = money_inserted - price
        clear_console()
        print(f"{format_money(money_inserted)} inserted.  Here is {format_money(change)} in change.")
        make_coffee(coffee)
    else:
        clear_console()
        make_coffee(coffee)


def make_coffee(coffee, resource=resources):
    chosen_coffee = MENU[coffee]
    for resource in chosen_coffee["ingredients"]:
        amount = chosen_coffee["ingredients"][resource]
        resources[resource] -= amount
    print(f"Here is your {coffee} ☕.  Enjoy!!")
    ask()


def run():
    ask()


run()
