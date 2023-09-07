from functions import line_break
from sheet_data import *

import subprocess

from colorama import just_fix_windows_console
just_fix_windows_console()

def start():
    """
    Starting point
    Prints a message to the UI to select options:
    1: Input stock trading data
    2: Show past trades
    3: Get statistics 
    """

    print("Welcome to your Stock Trading Journal")
    print("Please press one of the following buttons on your keyboard to continue:\n")
    print("'1' to input you stock trading data.")
    print("'2' to see your past journal entries.")
    print("'3' to see your past trading statistics.\n")

    user_input_menu = input("Please enter your option here: ")

    if user_input_menu == "1":
        try:
            subprocess.run(["python", "input_stock_data.py"])
        except FileNotFoundError:
            print("File not found.")
    elif user_input_menu == "2":
        subprocess.run(["python", "show_past_trades.py"])
    elif user_input_menu == "3":
        subprocess.run(["python", "get_statistics.py"])
    else:
         print("Invalid input. Please enter 1, 2, or 3.")

start()