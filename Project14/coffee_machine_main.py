import helper_functions as hf

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

COINS = {
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


def ask():
    choice = input("What would you like? (espresso/latte/cappuccino):  ")

    if choice == "off":
        return
    elif choice == "report":
        hf.clear_console()
        print_report()
        ask()
    else:
        resource_check(choice)


def print_report():
    print("Current resources available:")
    for resource in resources:
        print(f"{resource}:  {resources[resource]}")


def resource_check(coffee):
    return


def process_coins():
    return


def make_transaction():
    return


def make_coffee(coffee):
    return




def run():
    ask()



ask()

