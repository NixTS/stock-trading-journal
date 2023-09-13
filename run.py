from colorama import Fore, init
from input_stock_data import handle_input_date
from show_past_trades import handle_input_past_trades
from get_statistics import handle_input_statistics
from functions import line_break
from sheet_data import *

init(autoreset=True)


def main():
    """
    Starting point
    Prints a message to the UI to select options.
    """
    line_break()
    print(Fore.YELLOW + "Welcome to your Stock Trading Journal!\n\n")
    print("Please press one of the following buttons to continue:\n")
    print("'1' to input stock trading data.")
    print("'2' to display journal entries.")
    print("'3' to display trading statistics.\n")


def handle_input():
    """
    Handles key presses to navigate menu
    1: Input stock trading data to journal
    2: Display trading journal
    3: Display trading statistics 
    """
    allowed_keys = {'1', '2', '3'}

    while True:
        choice = input("Enter Navigation: \n").lower()

        if choice in allowed_keys:
            if choice == '1':
                handle_input_date()
            elif choice == '2':
                handle_input_past_trades()
            elif choice == '3':
                handle_input_statistics()
        else:
            line_break()
            print(Fore.RED + "Please enter a valid choice.")
            print(Fore.RED + "1, 2 or 3")
            main()


if __name__ == "__main__":
    main()
    handle_input()