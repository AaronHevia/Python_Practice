from coffee_menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
on = True

while on:
    items = menu.get_items()
    choice = input(f"What would you like? ({items}):  ")

    if choice == "off":
        on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)
