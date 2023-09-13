from pynput import keyboard
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


def on_key_release(key):
    """
    Handles key releases to navigate the menu.
    1: Input stock trading data to the journal
    2: Display trading journal
    3: Display trading statistics
    ESC: Exit the program
    """
    try:
        key_str = key.char
        if key_str in allowed_keys:
            if key_str == '1':
                handle_input_date()
            elif key_str == '2':
                handle_input_past_trades()
            elif key_str == '3':
                handle_input_statistics()
            elif key_str == 'esc':
                close_script()
    except AttributeError:
        pass


def handle_input():
    """
    Create a keyboard listener to handle key releases.
    """
    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
    handle_input()