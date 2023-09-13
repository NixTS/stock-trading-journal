import keyboard
from colorama import Fore, init

from input_stock_data import handle_input_date
from show_past_trades import handle_input_past_trades
from get_statistics import handle_input_statistics
from functions import line_break, close_script
from sheet_data import *

allowed_keys = {'1', '2', '3', 'esc'}
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
    print(Fore.RED + "'ESC' to exit the program.")


def handle_input():
    """
    Handles key presses to navigate menu
    1: Input stock trading data to journal
    2: Display trading journal
    3: Display trading statistics
    ESC: to exit the program; using sys.exit
    """
    while True:
        event = keyboard.read_event(suppress=True)
        if event.event_type == keyboard.KEY_UP:
            choice = event.name

            if choice in allowed_keys:
                if choice == '1':
                    handle_input_date()
                elif choice == '2':
                    handle_input_past_trades()
                elif choice == '3':
                    handle_input_statistics()
                elif choice == 'esc':
                    close_script()


if __name__ == "__main__":
    main()
    handle_input()
