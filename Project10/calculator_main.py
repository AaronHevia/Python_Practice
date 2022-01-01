import sys
sys.path.insert(1, 'E:/_GitHub/Python_Practice')
from helper_functions import *
from calculator_art import logo


def add(number1, number2):
    """Returns the sum of two numbers."""
    return number1 + number2


def subtract(number1, number2):
    """Returns the difference of two numbers.  The second number is always subtracted from the first number."""
    return number1 - number2


def multiply(number1, number2):
    """Returns the product of two numbers."""
    return number1 * number2


def divide(number1, number2):
    """Returns the division of two numbers.  The first number is the dividend and the second number is the divisor."""
    return number1 / number2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def first_number():
    number = float(input("\nWhat is your first number?:  "))
    return number


def calculate(number):
    """Performs the method of operation based on the inputs provided to get a result.  Result is then passed to the
     display function."""
    operator = input("Pick a method of operation ('+', '-', '*', '/'):  ")
    second_number = float(input("What is your second number?:  "))
    function = operations[operator]
    result = function(number, second_number)
    display(number1=number, method_of_operation=operator, number2=second_number, answer=result)


def display(number1, method_of_operation, number2, answer):
    """Displays the final prompt based on inputs and asks the user if they want to continue using the answer as the
     first number of the follow-on calculation.  If not, calculator will restart."""
    clear_console()
    prompt = f"{number1} {method_of_operation} {number2} = {answer}"
    print(prompt)
    resume = input("\nType 'y' to continue calculating with answer,\n"
                   "or type 'n' to start a new calculation:  ").lower()
    if resume == "y":
        calculate(answer)
    else:
        run()


def run():
    clear_console()
    print(logo)
    calculate(first_number())


run()
