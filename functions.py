import sys
import time
from colorama import Fore, init

init(autoreset=True)


def line_break():
    """
    Adds a line and a blank line underneath.
    For visual pleasure.
    """
    print(Fore.CYAN + "__________________________________________________\n")


def close_script():
    """
    Closes the script and ends the program
    Is displayed at the start of each file,
    in the navigation menu.
    """
    line_break()
    print(Fore.RED + "\nExiting the program.")
    line_break()
    sys.exit(0)


def back_to_menu():
    """
    Asks for input of 1 to return to the scripts menu
    Adds print and time.sleep statements
    """
    allowed_keys = ('1')

    while True:
        choice = input("Enter '1' to get back to menu: \n")

        if choice in allowed_keys:
            if choice == '1':
                line_break()
                print("Returning to menu . . .\n")
                time.sleep(2)
                print("Restarting process . . .\n")
                print("This takes only 3 seconds . . .")
                time.sleep(3)
                break
            else:
                print(Fore.RED + "Critical Error detected!")
                print(Fore.RED + "Closing program!")
                sys.exit(0)
