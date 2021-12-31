import os


def clear_console():
    if os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
    elif os.name in ('linux', 'osx', 'posix'):
        os.system('clear')


def close():
    input("'Enter' to exit.")

