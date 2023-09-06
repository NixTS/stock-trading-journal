import gspread

from google.oauth2.service_account import Credentials

import subprocess

from colorama import just_fix_windows_console
just_fix_windows_console()

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('trading-journal')

stock_data = SHEET.worksheet('stock_data')

data = stock_data.get_all_values()


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