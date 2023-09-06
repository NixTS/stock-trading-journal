from tabulate import tabulate

import re

import gspread
from google.oauth2.service_account import Credentials


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


def line_break():
    print("__________________________________________________\n")

def handle_input_past_trades():
    """
    Gives an option to either view a certain number of trade,
    todays trades, or all past trades.
    """
    line_break()
    print("Trading journal\n\n")
    print("If you want to display your past trades, please follow the instructions given to you.\n")
    print("Press '1' on your keyboard to enter a number.")
    print("Or:")
    print("Press '2', if you want see todays trades.")
    print("Or:")
    print("Press '3', if you want see all your past trades.\n")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            num_of_trades()
        elif choice == "2":
            todays_trades()
        elif choice == "3":
            all_trades()
        else:
            line_break()
            print("Invalid format, please enter '1' or '2' or '3'.")

def num_of_trades():
    """
    Enter a number to display past trades.
    If the number is higher than all past trades,
    an error message will appear with the number of all past trades
    """
    line_break()
    num_of_past_trades = input("Enter the number of last trades to display: ")

    try:
        num_of_past_trades = int(num_of_past_trades)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    total_rows_with_data = sum(1 for row in data if any(row))

    if num_of_past_trades <= 0:
        print("Invalid input. Please enter a positive number.")
        return

    if num_of_past_trades > total_rows_with_data:
        print(f"Requested {num_of_past_trades} rows, but there are only {total_rows_with_data} rows with data.")
        return

    line_break()
    headers = stock_data.row_values(1)
    last_n_rows = [row for row in reversed(data) if any(row)][:num_of_past_trades]

    print(f"Here you can see your past {num_of_past_trades} trades:\n")
    if num_of_past_trades <= total_rows_with_data:
        print(tabulate(last_n_rows, headers, tablefmt="github"))





def main():
    """
    Run all program functions
    """
    handle_input_past_trades()


main()