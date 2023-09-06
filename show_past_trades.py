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
    print("Press '3', if you want see all your past trades.")


    
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





def main():
    """
    Run all program functions
    """
    handle_input_past_trades()


main()