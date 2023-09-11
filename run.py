import keyboard
import sys
from colorama import Fore, Back, Style
from input_stock_data import handle_input_date
from show_past_trades import handle_input_past_trades
from get_statistics import handle_input_statistics
from functions import line_break
from sheet_data import *

allowed_keys = {'1', '2', '3', 'esc'}

def main():
    """
    Starting point
    Prints a message to the UI to select options.
    """
    line_break()
    print("Welcome to your Stock Trading Journal!\n")
    print("Please press one of the following buttons on your keyboard to continue:\n")
    print("'1' to input your stock trading data.")
    print("'2' to display your journal entries.")
    print("'3' to display your trading statistics.\n")
    print("'ESC' to exit the program.")

def handle_input():
    """
    Handles key presses to navigate menu
    1: Input stock trading data to journal
    2: Display trading journal
    3: Display trading statistics 
    ESC: to exit the program; using quit()
    """
    while True:
        choice = keyboard.read_event().name

        if choice == 'esc':
            print("\nExiting the program.")
            line_break()
            sys.exit(0)

        if choice in allowed_keys:
            if choice == '1':
                handle_input_date()
            elif choice == '2':
                handle_input_past_trades()
            elif choice == '3':
                handle_input_statistics()

if __name__ == "__main__":
    main()
    handle_input()